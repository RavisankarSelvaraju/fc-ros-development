from typing_extensions import Self
import rclpy
from rclpy.node import Node

class DoorSubscriber(Node):
    def __init__(self):
        super().__init__("door_subscribers")
        self.sub=self.create_subcription(
            DoorStatus,
            '/physics',
            self.door_callback,
            10
        )
    
    #def door_callback():