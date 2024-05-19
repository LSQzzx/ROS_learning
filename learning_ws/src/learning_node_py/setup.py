from setuptools import find_packages, setup

package_name = 'learning_node_py'

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
            'node_hello_node = learning_node_py.hello_node:main',
            'node_hello_class = learning_node_py.hello_class:main',
            'face_detect_node = learning_node_py.face_detect:main'
        ],
    },
)
