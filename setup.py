from setuptools import setup
from os import path

version = '1.0.6.3'
long_description = ''

current_directory = path.abspath(path.dirname(__file__))

with open(path.join(current_directory, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='pyhcm',
    packages=['pyhcm'],
    version=f'{version}', license='MIT',
    description='Wrapper of huawei cloud messaging (Push Kit) for sending push notification using python.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Ulises Martinez Adon',
    author_email='umartinezadon@outlook.com',
    url='https://github.com/umartinez22',
    download_url=f'https://github.com/umartinez22/python-huawei-cloud-messaging/archive/v_{version}.tar.gz',
    keywords=['Huawei', 'cloud', 'messaging', 'notification'],
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python'
    ],
)
