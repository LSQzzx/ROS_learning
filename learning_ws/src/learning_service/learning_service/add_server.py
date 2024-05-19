import rclpy
from rclpy.node import Node
from learning_interface.srv import Add

class AddServer(Node):
    
    def __init__(self, node_name):
        super().__init__(node_name)
        self.srv = self.create_service(Add, "add", self.callback)
        
    def callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info('request: a: %d b: %d' % (request.a, request.b))
        return response
    
def main(args=None):
    rclpy.init(args=args)
    node = AddServer("add_server")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()