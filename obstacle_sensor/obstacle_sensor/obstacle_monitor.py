import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

SAFE_DISTANCE_CM = 20.0

class ObstacleMonitor(Node):
    def __init__(self):
        super().__init__('obstacle_monitor')
        self.subscription = self.create_subscription(
            Float32,
            'distance_sensor/reading',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        distance = msg.data
        if distance < SAFE_DISTANCE_CM:
            self.get_logger().warn(f'OBSTACLE DETECTED at {distance:.2f} cm! Stopping rover.')
        else:
            self.get_logger().info(f'Path clear: {distance:.2f} cm')

def main(args=None):
    rclpy.init(args=args)
    node = ObstacleMonitor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()