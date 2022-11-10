from service_message.srv import Somma

import rclpy
from rclpy.node import Node


class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli = self.create_client(Somma, 'sum_values')
        
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = Somma.Request()

    def send_request(self):
        self.req.a = 1
        self.req.b = 2
        self.future = self.cli.call_async(self.req)


def main(args=None):
    rclpy.init(args=args)

    minimal_client = MinimalClientAsync()
    minimal_client.send_request()

    while rclpy.ok():
        rclpy.spin_once(minimal_client)
        if minimal_client.future.done():
            try:
                response = minimal_client.future.result()
            except Exception as e:
                minimal_client.get_logger().info(
                    'Service call failed %r' % (e,))
            else:
                minimal_client.get_logger().info(
                    'Result sum: %d + %d = %d' % (minimal_client.req.a, minimal_client.req.b, response.somma))
            break

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    try:
        main()
    
    except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
        self.get_logger().info('Program has stop...')
