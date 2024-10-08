from setuptools import find_packages, setup

package_name = 'printtestpak'

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
    maintainer_email='game@thapat.me',
    description='Prints "Hello World"',
    license='GPLv3',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'printhello = printtestpak.printhello:main',
        ],
    },
)
