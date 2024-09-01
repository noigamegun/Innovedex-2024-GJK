import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Bool
import serial

class ServoController(Node):
    def __init__(self):
        super().__init__('servo_controller')
        self.subscription_ir = self.create_subscription(
            Bool,
            'ir_sensor_status',
            self.ir_listener_callback,
            10)
        self.subscription_ir  # prevent unused variable warning
        self.subscription = self.create_subscription(
            String,
            'servo_control',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.ser = serial.Serial('/dev/ttyUSB0', 9600)  # Adjust the serial port as needed

    def ir_listener_callback(self, msg):
        if msg.data:
            self.ser.write(b'a')
            self.get_logger().info('IR Sensor detected something, Servo moved to position a')
        else:
            self.ser.write(b'b')
            self.get_logger().info('No detection, Servo moved to position b')

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
