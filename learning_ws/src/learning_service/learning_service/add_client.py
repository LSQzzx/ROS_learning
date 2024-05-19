import sys
import rclpy
from rclpy.node import Node
from learning_interface.srv import Add

class AddClient(Node):
    
    def __init__(self, name):
        super().__init__(name)
        self.client = self.create_client(Add, 'add')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('waiting service...') 
        self.request = Add.Request()

    def send_request(self):
        self.request.a = int(sys.argv[1])
        self.request.b = int(sys.argv[2])
        self.future = self.client.call_async(self.request)

def main(args=None):
    rclpy.init(args=args)
    node = AddClient("add_client")
    node.send_request()
    
    while rclpy.ok():
        rclpy.spin_once(node)
        if node.future.done():
            try:
                response = node.future.result()
            except Exception as e:
                node.get_logger().info('service failed %r' % (e,))
            else:
                node.get_logger().info(
                    'result: %d + %d = %d' %
                    (node.request.a, node.request.b, response.sum))
            break
            
    node.destroy_node()
    rclpy.shutdown()