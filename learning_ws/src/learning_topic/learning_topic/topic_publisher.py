import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TopicPublisherNode(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.pub = self.create_publisher(String, "hello", 10)
        self.timer = self.create_timer(0.5, self.timer_callback)
        
    def timer_callback(self):
        msg = String()
        msg.data = "Hello Subscribers"
        self.pub.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = TopicPublisherNode("topic_hello_publisher")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()