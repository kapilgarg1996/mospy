from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='mospy',
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
      url='https://github.com/kapilgarg1996/mospy',
      author='Kapil Garg',
      author_email='kapilgarg1996@gmail.com',
      license='MIT',
      packages=['mospy'],
      install_requires=['numpy', 'pillow'],
      entry_points={
          'console_scripts': ['mospy=mospy.command_line:main'],
          'gui_scripts': ['mospy-app=mospy.GUI:main']
      },
      zip_safe=False)