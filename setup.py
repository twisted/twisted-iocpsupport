#!/usr/bin/env python

# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

import setuptools
import sysconfig
from Cython.Build import cythonize

macros = None
# we need these defines to build free-threaded on Windows:
# Py_GIL_DISABLED needs to be 1
# CYTHON_USE_TYPE_SPECS needs to be 0, otherwise the module won't compile
# CYTHON_METH_FASTCALL needs to be 0, but Py_GIL_DISABLED sets it to 1
# CYTHON_ASSUME_SAFE_MACROS needs to be 0, but Py_GIL_DISABLED sets it to 1
# we define GRAALVM_PYTHON because it sets CYTHON_METH_FASTCALL to 0 and
# CYTHON_ASSUME_SAFE_MACROS to 0
# this should probably be re-checked every major Python version
if sysconfig.get_config_var("Py_GIL_DISABLED") == 1:
    macros = [("GRAALVM_PYTHON", "1"), ("Py_GIL_DISABLED", "1")]
setuptools.setup(
    ext_modules=cythonize(
        [
            setuptools.Extension(
                "twisted_iocpsupport.iocpsupport",
                sources=[
                    "twisted_iocpsupport/iocpsupport.pyx",
                    "twisted_iocpsupport/winsock_pointers.c",
                ],
                libraries=["ws2_32"],
                define_macros=macros,
            )
        ]
    )
)
