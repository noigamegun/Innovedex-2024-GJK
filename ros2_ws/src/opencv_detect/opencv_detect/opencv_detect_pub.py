import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import cv2
import numpy as np

class ShapeDetector(Node):
    def __init__(self):
        super().__init__('shape_detector')
        self.publisher_ = self.create_publisher(String, 'shape_detect', 10)
        self.cap = cv2.VideoCapture(0)
        self.detected_shapes = set()

    def detect_shapes(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            blurred = cv2.medianBlur(gray, 5)

            # Detect circles using Hough Circle Transform
            circles = cv2.HoughCircles(
                blurred, 
                cv2.HOUGH_GRADIENT, 
                dp=1.2, 
                minDist=100, 
                param1=100, 
                param2=60, 
                minRadius=40, 
                maxRadius=120
            )
            if circles is not None:
                circles = np.round(circles[0, :]).astype("int")
                for (x, y, r) in circles:
                    cv2.circle(frame, (x, y), r, (255, 0, 0), 2)
                    self.publish_shape('circle')

            # Detect squares using contour approximation
            edged = cv2.Canny(blurred, 50, 150)
            contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
                if len(approx) == 4:
                    x, y, w, h = cv2.boundingRect(approx)
                    aspect_ratio = float(w) / h
                    if 0.9 < aspect_ratio < 1.1 and w > 50 and h > 50:
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        self.publish_shape('square')

            cv2.imshow('Frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

    def publish_shape(self, shape):
        if shape not in self.detected_shapes:
            self.detected_shapes.add(shape)
            msg = String()
            msg.data = shape
            self.publisher_.publish(msg)
            self.get_logger().info(f'Detected and published: {shape}')
        else:
            self.detected_shapes.discard(shape)

def main(args=None):
    rclpy.init(args=args)
    shape_detector = ShapeDetector()
    shape_detector.detect_shapes()
    shape_detector.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()