import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class DistancePublisher(Node):
    def __init__(self):
        super().__init__('distance_publisher')
        self.publisher_ = self.create_publisher(Float32, 'distance_sensor/reading', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.distance = 100.0

    def timer_callback(self):
        self.distance -= random.uniform(2.0, 6.0)
        if self.distance < 5.0:
            self.distance = 100.0

        noisy_reading = self.distance + random.uniform(-1.0, 1.0)

        msg = Float32()
        msg.data = noisy_reading
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published distance: {noisy_reading:.2f} cm')

def main(args=None):
    rclpy.init(args=args)
    node = DistancePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()