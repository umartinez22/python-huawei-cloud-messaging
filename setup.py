from distutils.core import setup

version = '1.0.6.1'

setup(
    name='pyhcm',
    packages=['pyhcm'],
    version=f'{version}', license='MIT',
    description='Wrapper of api push huawei for sending notification push using python.',
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
