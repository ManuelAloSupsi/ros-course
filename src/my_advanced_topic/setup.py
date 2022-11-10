from setuptools import setup

package_name = 'my_advanced_topic'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='labosmt',
    maintainer_email='labosmt@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
	    'talker=my_advanced_topic.publisher:main',
            'listener=my_advanced_topic.subscriber:main',
	],
    },
)
