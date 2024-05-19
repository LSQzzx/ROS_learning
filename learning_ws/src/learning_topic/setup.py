from setuptools import find_packages, setup

package_name = 'learning_topic'

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
    maintainer='sp1der',
    maintainer_email='sp1der@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'topic_hello_publisher = learning_topic.topic_publisher:main',
            'topic_hello_subscriber = learning_topic.topic_subscriber:main',
            'topic_camera_node = learning_topic.camera:main',
            'topic_facerecg_node = learning_topic.face_recg:main',
            'topic_checkin_node = learning_topic.checkin:main',
        ],
    },
)
