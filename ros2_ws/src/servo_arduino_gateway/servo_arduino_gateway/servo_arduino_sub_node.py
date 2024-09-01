import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial

class ServoController(Node):
    def __init__(self):
        super().__init__('servo_controller')
        self.subscription = self.create_subscription(
            String,
            'servo_control',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.ser = serial.Serial('/dev/ttyUSB0', 9600)  # Adjust the serial port as needed
        self.get_logger().info('Connected to Arduino on /dev/ttyUSB0')  

    def listener_callback(self, msg):
        command = msg.data
        if command in ['a', 'b', 'c']:
            self.ser.write(command.encode())
            self.get_logger().info(f'Sent command: {command}')

def main(args=None):
    rclpy.init(args=args)
    servo_controller = ServoController()
    rclpy.spin(servo_controller)
    servo_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()