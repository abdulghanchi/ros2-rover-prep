from setuptools import find_packages, setup

package_name = 'obstacle_sensor'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Abdul Ghanchi',
    maintainer_email='[email protected]',
    description='Simulated obstacle distance sensor and monitor for a Mars rover, built with ROS2.',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'distance_publisher = obstacle_sensor.distance_publisher:main',
            'obstacle_monitor = obstacle_sensor.obstacle_monitor:main',
        ],
    },
)