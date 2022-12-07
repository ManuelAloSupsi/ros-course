import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32

class FreeRtosSubscriber(Node):
    def __init__(self, node):
        self.node = node
        self.subscription = self.node.create_subscription(
            Int32,
            'freertos_int32_publisher',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.inProcess = True

    def listener_callback(self, msg):
        self.node.get_logger().info('FreeRtos: heard: "%d"' % msg.data)

    def stopProcess(self):
        self.node.destroy_node()
        while(self.inProcess): time.sleep(0.001)
