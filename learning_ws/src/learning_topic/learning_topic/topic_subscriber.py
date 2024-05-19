import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TopicSubscriberNode(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.sub = self.create_subscription(String, "hello", self.sub_callback, 10)
        
    def sub_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        
def main(args=None):
    rclpy.init(args=args)
    node = TopicSubscriberNode("topic_hello_subscriber")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()