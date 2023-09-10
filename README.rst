=========
 hexdump
=========

|ci| |wheels| |conda| |coverage| |release|

|pre| |cov| |pylint|

|tag| |license| |python|


.. note:: This package disappeared from BitBucket and was resurrected from
          Pypi and given a new home and package layout, with an actual license
          and PEP 517 packaging.

What is it about?
=================

* *dump* binary to hex and *restore* it back
* Linux / Windows / OS X
* Python 3
* library and command line tool

.. note:: Python 2 is no longer officially supported as of version 3.5.0.

command line
============

There are several ways to execute hexdump from the command line. If you
are inside the source repository, you can use the convenience symlink::

    $ ./hexdump --test

    $ python src/hexdump/hexdump.py

    # after installing with `pip install hexdump`
    $ hexdump

Dump binary data in hex form::

    $ hexdump binary.dat
    0000000000: 00 00 00 5B 68 65 78 64  75 6D 70 5D 00 00 00 00  ...[hexdump]....
    0000000010: 00 11 22 33 44 55 66 77  88 99 AA BB CC DD EE FF  .."3DUfw........

Restore binary from a saved hex dump::

    $ hexdump --restore hexdump.txt > binary.dat


basic API
=========

dump(binary, size=2, sep=' ')

    Convert binary data (bytes in Python 3 and
    str in Python 2) to string like '00 DE AD BE EF'.
    `size` argument specifies length of text chunks
    and `sep` sets chunk separator.

dehex(hextext)

    Helper to convert from hex string to binary data
    stripping whitespace from `hextext` if necessary.


advanced API: write full dumps
==============================

Python 3::

    >>> from hexdump import hexdump
    >>> hexdump.hexdump('\x00'*16)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    TypeError: Abstract unicode data (expected bytes sequence)
    >>> hexdump.hexdump(b'\x00'*16)
    00000000: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................

Python 3 string is a sequence of indices in abstract unicode
table. Each index points to a symbol, which doesn't specify
its binary value. To convert symbol to binary data, you need
to lookup a value for it in the encoding.

Here is how the same Russian text looks when transformed from
abstract unicode integers of Python 3 to bytes in Windows-1251
encoding and to bytes in UTF-8::

    >>> message = 'интерференция'
    >>> hexdump.hexdump(message.encode('windows-1251'))
    00000000: E8 ED F2 E5 F0 F4 E5 F0  E5 ED F6 E8 FF           .............
    >>> hexdump.hexdump(message.encode('utf-8'))
    00000000: D0 B8 D0 BD D1 82 D0 B5  D1 80 D1 84 D0 B5 D1 80  ................
    00000010: D0 B5 D0 BD D1 86 D0 B8  D1 8F                    ..........


advanced API: restore binary data from different hexdump formats
================================================================

Python 3::

    >>> res = hexdump.restore(
    ... '0010: 00 11 22 33 44 55 66 77  88 99 AA BB CC DD EE FF  .."3DUfw........')
    >>> res
    b'\x00\x11"3DUfw\x88\x99\xaa\xbb\xcc\xdd\xee\xff'
    >>> type(res)
    <class 'bytes'>


run self-tests
==============

Manually, after installing::

    $ hexdump --test

Or from inside the source repository with ``tox``::

    $ tox -e pyNN-platform

where ``NN`` is your default python version and ``platform`` is one of
``linux``, ``macos``, or ``windows``, for example::

    $ tox -e py38-linux


.. note:: When using an OS package, for example a Gentoo ebuild, the
          console script should be installed with a different name, such as
          ``hexdumper`` so as not to conflict with the util-linux command
          ``hexdump`` or the actual module filename ``hexdump.py``
          (the symlink in the top-level source directory is provided
          as a convenience).


questions
=========

| Q: Why create another module when there is binascii already?
| A: ``binascii.unhexlify()`` chokes on whitespace and linefeeds.
| ``hexdump.dehex()`` doesn't have this problem.

If you have other questions, feel free to open an issue
at https://github.com/sarnold/hexdump/issues


ChangeLog
=========

See the `HISTORY.rst`_ file for the full change history.

.. _HISTORY.rst: HISTORY.rst

Release checklist
=================

| [ ] run tests
| [ ] update version in hexdump.py
| [ ] update ChangeLog in README.txt from hexdump.py
| [ ] python setup.py register sdist upload


License
=======
GNU AGPL-3-or-newer  (see the LICENSE file for details)


Credits
=======
| anatoly techtonik <techtonik@gmail.com>
| George Schizas
| Ian Land
| Steve Arnold


.. |ci| image:: https://github.com/sarnold/hexdump/workflows/CI/badge.svg
    :target: https://github.com/sarnold/hexdump/actions?query=workflow:CI
    :alt: CI Status

.. |wheels| image:: https://github.com/sarnold/hexdump/workflows/Wheels/badge.svg
    :target: https://github.com/sarnold/hexdump/actions?query=workflow:Wheels
    :alt: Wheel Status

.. |conda| image:: https://github.com/sarnold/hexdump/workflows/Conda/badge.svg
    :target: https://github.com/sarnold/hexdump/actions?query=workflow:Conda
    :alt: Conda Status

.. |coverage| image:: https://github.com/sarnold/hexdump/actions/workflows/coverage.yml/badge.svg
    :target: https://github.com/sarnold/hexdump/actions/workflows/coverage.yml
    :alt: Coverage Status

.. |release| image:: https://github.com/sarnold/hexdump/workflows/Release/badge.svg
    :target: https://github.com/sarnold/hexdump/actions?query=workflow:Release
    :alt: Release Status

.. |cov| image:: https://raw.githubusercontent.com/sarnold/hexdump/badges/main/test-coverage.svg
    :target: https://github.com/sarnold/hexdump/
    :alt: Test coverage

.. |pylint| image:: https://raw.githubusercontent.com/sarnold/hexdump/badges/main/pylint-score.svg
    :target: https://github.com/sarnold/hexdump/actions/workflows/pylint.yml
    :alt: Pylint Score

.. |license| image:: https://img.shields.io/github/license/sarnold/hexdump
    :target: https://github.com/sarnold/hexdump/blob/master/LICENSE
    :alt: License

.. |tag| image:: https://img.shields.io/github/v/tag/sarnold/hexdump?color=green&include_prereleases&label=latest%20release
    :target: https://github.com/sarnold/hexdump/releases
    :alt: GitHub tag

.. |python| image:: https://img.shields.io/badge/python-3.6+-blue.svg
    :target: https://www.python.org/downloads/
    :alt: Python

.. |pre| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&amp;logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit
