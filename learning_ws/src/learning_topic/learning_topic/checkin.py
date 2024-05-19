import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Checkin(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.sub = self.create_subscription(String, "checkin", self.sub_callback, 10)
        
    def sub_callback(self, msg):
        self.get_logger().info('%s checked in' % msg.data)
        
def main(args=None):
    rclpy.init(args=args)
    node = Checkin("topic_checkin_node")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()