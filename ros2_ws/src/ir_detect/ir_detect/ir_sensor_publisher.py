#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
import serial

class IRSensorPublisher(Node):
    def __init__(self):
        super().__init__('ir_detect')
        self.publisher_ = self.create_publisher(Bool, '/ir_sensor_status', 10)
        self.serial_port = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        self.get_logger().info("Connected to Arduino on /dev/ttyUSB0")
        self.timer = self.create_timer(0.1, self.timer_callback)  # 10 Hz

    def timer_callback(self):
        sensor_status = self.read_ir_sensor()
        self.publisher_.publish(sensor_status)
        self.get_logger().info(f"IR Sensor Status: {sensor_status.data}")

    def read_ir_sensor(self):
        try:
            line = self.serial_port.readline().decode('utf-8').strip()
            return Bool(data=bool(int(line)))
        except ValueError:
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