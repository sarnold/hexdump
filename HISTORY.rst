3.4.0 (2021-03-07)
------------------

* Add conda recipe and workflow.
* Add pylint/custom badge workflow.
* Cleanup doctests so they run with py3.
* Update tox env/cfg, cleanup some lint, and reformat source
* Update ci workflows (add release and wheel artifact check)
* Remove py2 from package, tox, and ci envs.

3.3 (2015-01-22)
----------------

* accept input from sys.stdin if "-" is specified
  for both dump and restore (issue #1)
* new normalize_py() helper to set sys.stdout to
  binary mode on Windows

3.2 (2015-07-02)
----------------

* hexdump is now packaged as .zip on all platforms
  (on Linux created archive was tar.gz)
* .zip is executable! try `python hexdump-3.2.zip`
* dump() now accepts configurable separator, patch
  by Ian Land (PR #3)

3.1 (2014-10-20)
----------------

* implemented workaround against mysterious coding
  issue with Python 3 (see revision 51302cf)
* fix Python 3 installs for systems where UTF-8 is
  not default (Windows), thanks to George Schizas
  (the problem was caused by reading of README.txt)

3.0 (2014-09-07)
----------------

* remove unused int2byte() helper
* add dehex(text) helper to convert hex string
  to binary data
* add 'size' argument to dump() helper to specify
  length of chunks

2.0 (2014-02-02)
----------------

* add --restore option to command line mode to get
  binary data back from hex dump
* support saving test output with `--test logfile`
* restore() from hex strings without spaces
* restore() now raises TypeError if input data is
  not string
* hexdump() and dumpgen() now don't return unicode
  strings in Python 2.x when generator is requested

1.0 (2013-12-30)
----------------

* length of address is reduced from 10 to 8
* hexdump() got new 'result' keyword argument, it
  can be either 'print', 'generator' or 'return'
* actual dumping logic is now in new dumpgen()
  generator function
* new dump(binary) function that takes binary data
  and returns string like "66 6F 72 6D 61 74"
* new genchunks(mixed, size) function that chunks
  both sequences and file like objects

0.5 (2013-06-10)
----------------

* hexdump is now also a command line utility (no
  restore yet)

0.4 (2013-06-09)
----------------

* fix installation with Python 3 for non English
  versions of Windows, thanks to George Schizas

0.3 (2013-04-29)
----------------

* fully Python 3 compatible

0.2 (2013-04-28)
----------------

* restore() to recover binary data from a hex dump in
  native, Far Manager and Scapy text formats (others
  might work as well)
* restore() is Python 3 compatible

0.1 (2013-04-28)
----------------

* working hexdump() function for Python 2
