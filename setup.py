#!/usr/bin/env python

# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

import setuptools
from Cython.Build import cythonize


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
