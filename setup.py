from setuptools import setup

setup(
  name='general_backend',
  packages=['backend'],
  include_package_data=True,
  install_requires=[
    'flask', 'pymysql'
  ],
)
