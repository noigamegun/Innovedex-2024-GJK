import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
import serial

class IRSensorPublisher(Node):

    def __init__(self):
        super().__init__('ir_sensor_publisher')
        self.publisher_ = self.create_publisher(Bool, 'ir_sensor_status', 10)
        self.serial_port = serial.Serial('/dev/ttyUSB0', 9600)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        sensor_status = self.read_ir_sensor()
        self.publisher_.publish(sensor_status)
        self.get_logger().info(f"IR Sensor Status: {sensor_status.data}")

    def read_ir_sensor(self):
        try:
            line = self.serial_port.readline().decode('utf-8').strip()
            self.get_logger().info(f"Raw sensor data: {line}")
            sensor_value = bool(int(line))
            self.get_logger().info(f"Converted sensor value: {sensor_value}")
            return Bool(data=sensor_value)
        except ValueError:
            self.get_logger().error("Failed to convert sensor data to integer")
            return Bool(data=False)

def main(args=None):
    rclpy.init(args=args)
    node = IRSensorPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()