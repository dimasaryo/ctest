from setuptools import setup

setup(name='ctest',
      version='0.1',
      description='Functional Test Library',
      url='http://github.com/dimasaryo/ctest',
      author='Dimas Aryo Prakoso',
      author_email='dimasaryoprakoso@gmail.com',
      license='MIT',
      packages=['ctest'],
      install_requires=[
            'selenium'
      ],
      zip_safe=False)
