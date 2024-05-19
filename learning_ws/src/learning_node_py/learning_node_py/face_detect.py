import cv2
import rclpy
from rclpy.node import Node

class FaceDetectNode(Node):
    
    def __init__(self, node_name):
        super().__init__(node_name)
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.cap = cv2.VideoCapture(0)
        
        while rclpy.ok():
            ret, frame = self.cap.read()
            frame = cv2.flip(frame, 1)
            if ret:
                quit = self.detect(frame)

                if quit == 27:
                    self.cap.release()
                    cv2.destroyAllWindows()
                    break
            
    def detect(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow('Face Detection', frame)
        return cv2.waitKey(1) & 0xFF

def main(args=None):
    rclpy.init(args=args)
    node = FaceDetectNode("face_detect_node")
    node.destroy_node()
    rclpy.shutdown()
