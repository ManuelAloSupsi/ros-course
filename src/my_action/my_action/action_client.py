import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

from action_message.action import SommaFeed

class SumActionClient(Node):

    def __init__(self):
        super().__init__('somma_action_server')
        self._action_client = ActionClient(self, SommaFeed, 'values_sum_feed')
        self.get_logger().info("Initialisation OK")
        
    def send_goal(self):
        self.get_logger().info("I'm going to send goal")

        goal_msg = SommaFeed.Goal()
        
        goal_msg.a = 1
        goal_msg.ripetizioni = 4
        
        self._action_client.wait_for_server()

        self._send_goal_future = self._action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)

        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return

        self.get_logger().info('Goal accepted :)')

        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info('Result: {0}'.format(result.somma))
        rclpy.shutdown()

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info('Received feedback: {0}'.format(feedback.msg))


def main(args=None):
    rclpy.init(args=args)

    action_client = SumActionClient()

    action_client.send_goal()

    rclpy.spin(action_client)


if __name__ == '__main__':
    main()
