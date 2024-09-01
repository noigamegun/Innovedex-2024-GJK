import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial

class RelayController(Node):
    def __init__(self):
        super().__init__('relay_controller')
        self.subscription = self.create_subscription(
            String,
            'servo_control',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.ser = serial.Serial('/dev/ttyUSB0', 9600)  # Adjust the serial port as needed

    def listener_callback(self, msg):
        command = msg.data
        if command == 'a':
            self.ser.write(b'1')
            self.get_logger().info('Relay turned on')
        elif command == 'b':
            self.ser.write(b'0')
            self.get_logger().info('Relay turned off')

def main(args=None):
    rclpy.init(args=args)
    relay_controller = RelayController()
    rclpy.spin(relay_controller)
    relay_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
