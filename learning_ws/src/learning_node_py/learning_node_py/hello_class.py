import rclpy
from rclpy.node import Node
import time

class HelloClassNode(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        while rclpy.ok():
            self.get_logger().info("Hello Node")
            time.sleep(0.5)

def main(args=None):
    rclpy.init(args=args)
    node = HelloClassNode("node_hello_class")
    node.destroy_node()
    rclpy.shutdown()