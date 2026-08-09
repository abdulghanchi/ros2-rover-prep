# ROS2 Rover Prep

A personal project space for learning ROS2 by building small, real robotics systems — nodes, publishers/subscribers, and simulated sensor logic — rather than just following tutorials.

## Projects

### obstacle_sensor
A simulated obstacle-detection system with two ROS2 nodes: a distance sensor publisher and a safety-monitor subscriber that reacts when a rover would be too close to an obstacle. See [`obstacle_sensor/README.md`](./obstacle_sensor/README.md) for details.

## Environment

Built and tested using ROS2 Humble running in Docker (via [tiryoh/ros2-desktop-vnc](https://github.com/Tiryoh/docker-ros2-desktop-vnc)) on macOS, since ROS2 doesn't natively support Mac.
