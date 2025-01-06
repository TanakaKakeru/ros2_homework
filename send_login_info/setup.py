from setuptools import setup

package_name = 'send_login_info'

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
    maintainer='tanaka',
    maintainer_email='s23c1085lw@s.chibakoudai.jp',
    description='package for sending login information',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'send_login_info = send_login_info.send_login_info:main'
        ],
    },
)
