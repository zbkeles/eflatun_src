from setuptools import setup

package_name = 'eflatun'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/software_in_the_loop.launch.py', 'launch/pixhawk_test.launch.py']),
        ('share/' + package_name + '/config', ['config/object_tracker.yaml', 'config/object_detector.yaml', 'config/best_object_selector.yaml']), 
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sezer',
    maintainer_email='muhammedsezer12@gmail.com',
    description='TODO: Package description',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'object_tracker = eflatun.Object_Tracker:main',
            'object_detector = eflatun.Object_Detector:main',
            'object = eflatun.Object:main',
            'best_object_selector = eflatun.Best_Object_Selector:main',
            'vehicle_status_gui = eflatun.Vehicle_Status_Gui:main',
        ],
    },
)
