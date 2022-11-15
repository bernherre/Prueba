from setuptools import setup, find_packages
import os
# read the contents of your README file
from pathlib import Path
__location__ = os.path.dirname(__file__)
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSION = '0.1.0' 
DESCRIPTION = 'Python ST'
LONG_DESCRIPTION = 'This package contains nothing.'

# Setting up
# Be careful and avoid adding core libraries as requierements
setup(
       # the name must match the folder name 'skynet_tools'
        name="Prueba",
        version=VERSION,
        author="BHO",
        author_email="<bernherre@gmail.com>",
        description=DESCRIPTION,
        long_description=long_description,
        long_description_content_type='text/markdown',
        packages=find_packages(),
        license='MIT',
        install_requires=[
        "numpy>=1.16"
        ],
        keywords=['python', 'Skynet package'],
        classifiers= [
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering',
        'Framework :: IPython',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"]
)