twisted-iocpsupport
===================

.. image:: https://img.shields.io/github/actions/workflow/status/twisted/twisted-iocpsupport/github-deploy.yml?branch=default
    :alt: GitHub Actions
    :target: https://github.com/twisted/twisted-iocpsupport/
.. image:: https://img.shields.io/pypi/v/twisted-iocpsupport?logo=pypi
    :alt: PyPI
    :target: https://pypi.org/project/twisted-iocpsupport/


An extension for use in the L{twisted.internet.iocpreactor} I/O Completion
Ports reactor.

This code was initially part of the core Twisted project. It was moved into a
separate repo in order to simplify the Twisted production deployment. As such,
issues are handled via the `twisted/twisted GitHub Issues system <https://github.com/twisted/twisted/issues?q=is%3Aopen+is%3Aissue+label%3Aiocpreactor>`_

Additionally, this package provides no compatability gurantees:
All use must be via the ``Twisted`` PyPI distribution and ``twisted`` Python package.
Applications must not depend on the ``twisted-iocpsupport`` PyPI distribution directly.
Applications must not import names from the ``twisted_iocpsupport``
package directly.
See the `Twisted Compatability Policy <https://docs.twisted.org/en/stable/development/compatibility-policy.html`_ for more info.
