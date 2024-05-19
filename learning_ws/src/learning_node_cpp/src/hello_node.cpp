#include "rclcpp/rclcpp.hpp"

class HelloNode : public rclcpp::Node
{
    public:
        HelloNode()
        : Node("node_hello_node")
        {
            while (rclcpp::ok())
            {
                RCLCPP_INFO(this->get_logger(), "Hello World");
                sleep(1);
            }
        }
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<HelloNode>());
    rclcpp::shutdown();

    return 0;
}