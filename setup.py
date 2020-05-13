from distutils.core import setup
setup(
  name = 'phcm',         # How you named your package folder (MyLib)
  packages = ['phcm'],   # Chose the same as "name"
  version = '1.0.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Wrapper of api push huawei for sending notification push using python.',   # Give a short description about your library
  author = 'Ulises Martinez Adon',                   # Type in your name
  author_email = 'umartinezadon@outlook.com',      # Type in your E-Mail
  url = 'https://github.com/umartinez22',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/umartinez22/archive/v_1.0.0.tar.gz',    # I explain this later on
  keywords = ['Huawei', 'cloud', 'messaging', 'notification'],   # Keywords that define your package best
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.8.2'
  ],
)