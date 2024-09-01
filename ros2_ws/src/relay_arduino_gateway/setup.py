from setuptools import find_packages, setup

package_name = 'relay_arduino_gateway'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Game',
    maintainer_email='76461912+noigamegun@users.noreply.github.com',
    description='Control a relay via an Arduino.',
    license='GPLv3',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'relay_control_sub_node = relay_arduino_gateway.relay_control_sub_node:main',
        ],
    },
)
