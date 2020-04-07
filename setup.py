import os
import sys
from setuptools import setup, Command


_python = 'python%d' % sys.version_info.major


setup(
    name='deucalion',
    version='0.0.1',
    author='Shahar Azulay',
    author_email='shahar4@gmail.com',
    url='https://github.com/shaharazulay/deucalion',
    packages=[
        'deucalion',
        'examples',
        'examples.3_sum_algorithm'
    ],
    license='bsd',
    description='',
    long_description=open('README.rst').read(),
    install_requires=[],
    zip_safe=False,
    package_data={},
    include_package_data=True,
    cmdclass={
        'test': '',
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Information Analysis',
    ],
)
