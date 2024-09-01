import tkinter as tk
import rclpy
import serial

from std_msgs.msg import String, Int16, Float32, Bool
from rclpy.node import Node

class MainGui(Node):

    circle_count = 0
    square_count = 0

    def __init__(self):
        super().__init__('main_gui')
        self.root = tk.Tk()
        self.root.title("Control Panel")

        self.squarecount = tk.Label(self.root, text="Square Count: 0")
        self.squarecount.grid(row=0, column=0, columnspan=3)

        self.circlecount = tk.Label(self.root, text="Circle Count: 0")
        self.circlecount.grid(row=1, column=0, columnspan=3)

        self.start_button = tk.Button(self.root, text="Start", command=self.start)
        self.start_button.grid(row=2, column=0)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop)
        self.stop_button.grid(row=2, column=2)

        self.get_logger().info('GUI started.')

        self.shape_subscriber = self.create_subscription(
            String,
            'shape_detect',
            self.shape_callback,    
            10 
        )

        self.ir_subscriber = self.create_subscription(
            Bool,
            'ir_sensor_status',
            self.ir_callback,
            10
        )
        
        self.shape_detected = False
        self.updatecount()
        
    def ir_callback(self, msg):
        # Check what shape is detected and add to count
        if msg.data == False:
            self.get_logger().info("IR Sensor Status: Object Detected")
            self.shape_detected = True
        

    def shape_callback(self, msg):
        if self.shape_detected:
            shape = msg.data
            if shape == "square":
                self.square_count += 1
            elif shape == "circle":
                self.circle_count += 1
            else:
                self.get_logger().info(f"Invalid shape: {shape}")
            
            self.get_logger().info(f"Square Count: {self.square_count}, Circle Count: {self.circle_count}")
            self.shape_detected = False  # Reset the flag after processing

    def start(self):
        # Start the robot
        self.get_logger().info('Starting the robot')

    def stop(self):
        # Stop the robot
        self.get_logger().info('Stopping the robot')

    def updatecount(self):
        # Update the square and circle count labels
        self.squarecount.config(text="Square Count: " + str(self.square_count))
        self.circlecount.config(text="Circle Count: " + str(self.circle_count))
        self.root.after(100, self.updatecount)


def main(args=None):
    rclpy.init(args=args)
    main_gui = MainGui()
    main_gui.root.mainloop()
    rclpy.spin(main_gui)
