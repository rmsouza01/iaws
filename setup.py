#! /usr/bin/env python

# System imports
from distutils.core import *
from distutils      import sysconfig

import os

(opt,) = sysconfig.get_config_vars('OPT')
os.environ['OPT'] = " ".join(flag for flag in opt.split() if flag != '-Wstrict-prototypes')




# Third-party modules - we depend on numpy for everything
import numpy


# Obtain the numpy include directory.  This logic works across numpy versions.
try:
    numpy_include = numpy.get_include()
except AttributeError:
    numpy_include = numpy.get_numpy_include() # get_numpy_include()

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

# extension modules
_watershed_c =  Extension(
            '_watershed_c',
            ['iaws/watershed_c.cpp', 'iaws/watershed_c.i'], 
            include_dirs=[numpy_include], 
            extra_compile_args=["-fopenmp"],
            extra_link_args=["-fopenmp"],
            define_macros=[('NDEBUG', None),('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')],    
            library_dirs=[],
            libraries=[],
            swig_opts=['-c++', '-includeall', '-threads', '-keyword'],)

       

setup(  name        = "iaws",
        version     = "0.1",
	ext_modules = [_watershed_c],
	packages=['iaws'],
	author="Roberto M Souza and collaborators",
        author_email="roberto.medeiros.souza@gmail.com",
        description="Watershed implementations",
        license="BSD 2-clause License",
        keywords=["image processing", "mathematical morphology","max-tree"],
        url="...",
        long_description=read('README.txt'),
        classifiers=[
        "Development Status :: 1 - Alpha",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python and C++ glued with SWIG",
        "Topic :: Scientific/Engineering :: Mathematical Morphology",
        "License :: BSD 2-clause",
        ],
        )


