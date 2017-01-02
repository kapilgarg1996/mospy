from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='pymos',
      version='1.0.0',
      description='Application to create Mosaic',
      long_description=readme(),
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
      ],
      keywords='mosaic image',
      url='https://github.com/kapilgarg1996/pymos',
      author='Kapil Garg',
      author_email='kapilgarg1996@gmail.com',
      license='MIT',
      packages=['pymos'],
      install_requires=['numpy', 'pillow'],
      entry_points={
          'console_scripts': ['pymos=pymos.command_line:main'],
          'gui_scripts': ['pymos-app=pymos.GUI:main']
      },
      zip_safe=False)