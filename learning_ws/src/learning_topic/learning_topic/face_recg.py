import os
import cv2
import rclpy
import face_recognition
from rclpy.node import Node
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from std_msgs.msg import String

class FaceRecg(Node):
    
    def __init__(self, node_name):
        super().__init__(node_name)
        self.sub = self.create_subscription(
            Image, 'camera', self.listener_callback, 10
        )
        self.cv_bridge = CvBridge()
        
        self.pub = self.create_publisher(String, "checkin", 10)
        self.msg = String()
        
        self.faces_path = '/home/sp1der/faces/'
        self.known_names=[] 
        self.known_encodings=[]
        for image_name in os.listdir(self.faces_path):
            load_image = face_recognition.load_image_file(self.faces_path+image_name)
            image_face_encoding = face_recognition.face_encodings(load_image)[0]
            self.known_names.append(image_name.split(".")[0])
            self.known_encodings.append(image_face_encoding)
        
    def listener_callback(self, data):
        self.get_logger().info('Receiving video')
        frame = self.cv_bridge.imgmsg_to_cv2(data, 'bgr8')
        self.face_recg(frame)
    
    def face_recg(self, frame):
        rgb_frame = cv2.resize(frame, (0, 0), fx=1, fy=1)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:         
            matches = face_recognition.compare_faces(self.known_encodings, face_encoding,tolerance=0.5)
            if True in matches:
                first_match_index = matches.index(True)
                name = self.known_names[first_match_index]
            else:
                name="unknown"
            face_names.append(name)

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            self.msg.data = name
            self.pub.publish(self.msg)
            self.get_logger().info('%s checking in' % name)
        
        cv2.imshow('frame', frame)
        cv2.waitKey(1) 
    
def main(args=None):
    rclpy.init(args=args)
    node = FaceRecg("topic_facerecg_node")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()