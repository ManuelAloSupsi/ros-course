from mt_topic.subs_freertos import FreeRtosSubscriber
from mt_topic.subs_nuttx import NuttxSubscriber

import threading
import rclpy
import time

class MainNode():
    def __init__(self, debug=False):
        rclpy.init()

        # create nodes
        self.nodeFreeRtos = rclpy.create_node('freertos_node')
        self.nodeNuttX = rclpy.create_node('nuttx_node')

        # linking nodes
        self.freertos = FreeRtosSubscriber(self.nodeFreeRtos)
        self.nuttx = NuttxSubscriber(self.nodeNuttX)

        # linking nodes to thread
        executor = rclpy.executors.MultiThreadedExecutor()
        executor.add_node(self.nodeFreeRtos)
        executor.add_node(self.nodeNuttX)

        # Start (spin) all nodes simultaneously
        self.executor_thread = threading.Thread(target=executor.spin, daemon=True)
        self.executor_thread.start()
        
    def stopExecution(self):
        rclpy.shutdown()

        self.freertos.inProcess = False
        self.nuttx.inProcess = False

        self.freertos.stopProcess()
        self.nuttx.stopProcess()

        self.executor_thread.join()
        
def main():
    mainNode = MainNode()

    try:
        while rclpy.ok():
            time.sleep(0.5)
            
    except KeyboardInterrupt:
        # Stop thread
        mainNode.stopExecution()
        print("Exit")
    
