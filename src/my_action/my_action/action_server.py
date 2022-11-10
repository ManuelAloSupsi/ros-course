import rclpy
import time
from rclpy.action import ActionServer
from rclpy.node import Node

from action_message.action import SommaFeed

class SumActionServer(Node):

    def __init__(self):
        super().__init__('somma_action_server')
        self._action_server = ActionServer(
            self,
            SommaFeed,
            'values_sum_feed',
            self.execute_callback)
            
        self.interim_result = 0

    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')
        
        feedback_msg = SommaFeed.Feedback()

        feedback_msg.msg = "I'm going to start sum..."
        
        self.interim_result = 0


        for i in range(1, goal_handle.request.ripetizioni + 1):
        
            self.interim_result += goal_handle.request.a

            feedback_msg.msg = "Iteration " + str(i) + ". Actual result = " + str(self.interim_result)

            self.get_logger().info('Feedback: {0}'.format(feedback_msg.msg))

            goal_handle.publish_feedback(feedback_msg)

            time.sleep(1)


        goal_handle.succeed()

        result = SommaFeed.Result()

        result.somma = self.interim_result

        return result

def main(args=None):
    rclpy.init(args=args)

    action_server = SumActionServer()

    while rclpy.ok():
        rclpy.spin(action_server)

    minimal_service.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt():
        print("Finished...")
