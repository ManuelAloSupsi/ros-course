import rclpy
from rclpy.node import Node

from topic_messages.msg import Numeri


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Numeri, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Numeri()
        msg.a = 0 
        msg.b = 0 
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%d"' % msg.a)
        self.get_logger().info('Publishing: "%d"' % msg.b)
        self.get_logger().info('========================')


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
