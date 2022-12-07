import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32

class NuttxSubscriber(Node):
    def __init__(self, node):
        self.node = node
        self.subscription = self.node.create_subscription(
            Int32,
            'nuttx_int32_publisher',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.inProcess = True

    def listener_callback(self, msg):
        self.node.get_logger().info('NuttX: heard: "%d"' % msg.data)

    def stopProcess(self):
        self.node.destroy_node()
        while(self.inProcess): time.sleep(0.001)
