from setuptools import setup
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[0] < 3:
    with open(os.path.join(_here, 'README.adoc')) as f:
        long_description = f.read()
else:
    with open(os.path.join(_here, 'README.adoc'), encoding='utf-8') as f:
        long_description = f.read()

version = {}
with open(os.path.join(_here, 'pi_sample_duration', 'version.py')) as f:
    exec(f.read(), version)

setup(
    name='pi_sample_duration',
    version=version['__version__'],
    description=('Example of a python Performance Indicator.'),
    long_description=long_description,
    author='Anthony Remazeilles',
    author_email='anthony.remazeilles@tecnalia.com',
    url='https://github.com/tobedefined',
    license='Beerware',
    packages=['pi_sample_duration'],
#   no dependencies in this example
#   install_requires=[
#       'dependency==1.2.3',
#   ],

    scripts=['script/run_pi'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.6'],
    )
