from setuptools import find_packages, setup

package_name = 'ros2_py_examples'

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
    maintainer='languyen',
    maintainer_email='languyen@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'simple_publisher = ros2_py_examples.simple_publisher:main',
            'simple_subscriber = ros2_py_examples.simple_subscriber:main',
            'simple_parameter = ros2_py_examples.simple_parameter:main',
            'simple_service_server = ros2_py_examples.simple_service_server:main',
            'simple_service_client = ros2_py_examples.simple_service_client:main'
        ],
    },
)
