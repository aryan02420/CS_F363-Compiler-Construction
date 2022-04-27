from setuptools import setup

setup(name='tetrislang',
      version='0.1',
      description='CS F363',
      long_description='Compiler Construction',
      keywords='funniest joke comedy flying circus',
      url='https://github.com/aryan02420/CS_F363-Compiler-Construction',
      author='BlockBusters',
      author_email='',
      license='gpl-3.0',
      packages=['tetrislang'],
      scripts=['tetrislang/bin/tetris-lang'],
      install_requires=[
          'sly',
          'pygame'
      ],
      include_package_data=True,
      zip_safe=False)