#!/usr/bin/env python

# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

import setuptools
import sysconfig
from Cython.Build import cythonize

macros = None
if sysconfig.get_config_var("Py_GIL_DISABLED") == 1:
    macros = [("Py_GIL_DISABLED", "1")]
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
