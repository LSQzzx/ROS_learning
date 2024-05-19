import cv2
import rclpy
from rclpy.node import Node
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

class Camera(Node):
    
    def __init__(self, node_name):
        super().__init__(node_name)
        self.pub = self.create_publisher(Image, "camera", 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.cap = cv2.VideoCapture('http://192.168.48.1:5000')
        self.cv_bridge = CvBridge()
        
    def timer_callback(self):
        ret, frame = self.cap.read()
        
        if ret:
            self.pub.publish(self.cv_bridge.cv2_to_imgmsg(frame, 'bgr8'))
        
        self.get_logger().info('Publishing video frame')

def main(args=None):
    rclpy.init(args=args)
    node = Camera("topic_camera_node")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()