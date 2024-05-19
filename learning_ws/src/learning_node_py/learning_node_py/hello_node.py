import rclpy
from rclpy.node import Node
import time

def main(args=None):
    rclpy.init(args=args)
    node = Node("node_hello_node")
    
    while rclpy.ok():
        node.get_logger().info("Hello Node")
        time.sleep(0.5)
    
    node.destroy_node()
    rclpy.shutdown()