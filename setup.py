#!/usr/bin/env python

# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

import setuptools
import sysconfig
from Cython.Build import cythonize

if sysconfig.get_config_var("abi_thread") == "t":
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
                    # GRAALVM_PYTHON happens to mostly set the defines we need
                    define_macros=[("GRAALVM_PYTHON", "1"), ("Py_GIL_DISABLED", "1")],
                )
            ]
        )
    )
else:
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
                )
            ]
        )
    )
