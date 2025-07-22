#!/usr/bin/env python

# <-- removing this magic comment breaks Python 3.4 on Windows
"""
1. Dump binary data to the following text format:

00000000: 00 00 00 5B 68 65 78 64  75 6D 70 5D 00 00 00 00  ...[hexdump]....
00000010: 00 11 22 33 44 55 66 77  88 99 AA BB CC DD EE FF  .."3DUfw........

It is similar to the one used by:
Scapy
00 00 00 5B 68 65 78 64 75 6D 70 5D 00 00 00 00  ...[hexdump]....
00 11 22 33 44 55 66 77 88 99 AA BB CC DD EE FF  .."3DUfw........

Far Manager
000000000: 00 00 00 5B 68 65 78 64 ¦ 75 6D 70 5D 00 00 00 00     [hexdump]
000000010: 00 11 22 33 44 55 66 77 ¦ 88 99 AA BB CC DD EE FF   ?"3DUfwˆ™ª»ÌÝîÿ


2. Restore binary data from the formats above as well
   as from less exotic strings of raw hex

"""
import argparse
import binascii  # binascii is required for Python 3
import os
import pkgutil
import sys
import tempfile

if sys.version_info < (3, 8):
    from importlib_metadata import version
else:
    from importlib.metadata import version

VERSION = version('hexdump')


# --- - chunking helpers
def chunks(seq, size):
    """
    Generator that cuts sequence (bytes, memoryview, etc.)
    into chunks of given size. If `seq` length is not multiply
    of `size`, the lengh of the last chunk returned will be
    less than requested.

    >>> list( chunks([1,2,3,4,5,6,7], 3) )
    [[1, 2, 3], [4, 5, 6], [7]]
    """
    d, m = divmod(len(seq), size)
    for i in range(d):
        yield seq[i * size : (i + 1) * size]
    if m:
        yield seq[d * size :]


def chunkread(f, size):
    """
    Generator that reads from file like object. May return less
    data than requested on the last read.
    """
    c = f.read(size)
    while len(c):
        yield c
        c = f.read(size)


def genchunks(mixed, size):
    """
    Generator to chunk binary sequences or file like objects.
    The size of the last chunk returned may be less than
    requested.
    """
    if hasattr(mixed, 'read'):
        return chunkread(mixed, size)
    return chunks(mixed, size)


# --- - /chunking helpers


def dehex(hextext):
    """
    Convert from hex string to binary data stripping
    whitespaces from `hextext` if necessary.
    """
    return bytes.fromhex(hextext)


def dump(binary, size=2, sep=' '):
    """
    Convert binary data (bytes in Py3) to hex string like '00 DE AD BE EF'.
    `size` argument specifies length of text chunks
    and `sep` sets chunk separator.
    """
    hexbstr = binascii.hexlify(binary)
    hexstr = hexbstr.decode('ascii')
    return sep.join(chunks(hexstr.upper(), size))


def dumpgen(data):
    """
    Generator that produces strings:

    '00000000: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................'
    """
    generator = genchunks(data, 16)
    for addr, d in enumerate(generator):
        # 00000000:
        line = '%08X: ' % (addr * 16)
        # 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00
        dumpstr = dump(d)
        line += dumpstr[: 8 * 3]
        if len(d) > 8:  # insert separator if needed
            line += ' ' + dumpstr[8 * 3 :]
        # ................
        # calculate indentation, which may be different for the last line
        pad = 2
        if len(d) < 16:
            pad += 3 * (16 - len(d))
        if len(d) <= 8:
            pad += 1
        line += ' ' * pad

        for byte in d:
            # printable ASCII range 0x20 to 0x7E
            if 0x20 <= byte <= 0x7E:
                line += chr(byte)
            else:
                line += '.'
        yield line


def hexdump(data, result='print'):
    """
    Transform binary data to the hex dump text format:

    00000000: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................

      [x] data argument as a binary string
      [x] data argument as a file like object

    Returns result depending on the `result` argument:
      'print'     - prints line by line
      'return'    - returns single string
      'generator' - returns generator that produces lines
    """
    if isinstance(data, str):
        raise TypeError('Abstract unicode data (expected bytes sequence)')

    gen = dumpgen(data)
    if result == 'generator':
        return gen
    if result == 'return':
        return '\n'.join(gen)
    if result == 'print':
        for line in gen:
            print(line)
        return
    raise ValueError('Unknown value of `result` argument')


def restore(dump):
    """
    Restore binary data from a hex dump.
      [x] dump argument as a string
      [ ] dump argument as a line iterator

    Supported formats:
      [x] hexdump.hexdump
      [x] Scapy
      [x] Far Manager
    """
    minhexwidth = 2 * 16  # minimal width of the hex part - 00000... style
    bytehexwidth = 3 * 16 - 1  # min width for a bytewise dump - 00 00 ... style

    result = bytes()
    if not isinstance(dump, str):
        raise TypeError('Invalid data for restore')

    text = dump.strip()  # ignore surrounding empty lines
    for line in text.split('\n'):
        # strip address part
        addrend = line.find(':')
        if 0 < addrend < minhexwidth:  # : is not in ascii part
            line = line[addrend + 1 :]
        line = line.lstrip()
        # check dump type
        if line[2] == ' ':  # 00 00 00 ...  type of dump
            # check separator
            sepstart = (2 + 1) * 7 + 2  # ('00'+' ')*7+'00'
            sep = line[sepstart : sepstart + 3]
            if sep[:2] == '  ' and sep[2:] != ' ':  # ...00 00  00 00...
                hexdata = line[: bytehexwidth + 1]
            elif sep[2:] == ' ':  # ...00 00 | 00 00...  - Far Manager
                hexdata = line[:sepstart] + line[sepstart + 3 : bytehexwidth + 2]
            else:  # ...00 00 00 00... - Scapy, no separator
                hexdata = line[:bytehexwidth]
            line = hexdata
        result += dehex(line)
    return result


def runtest(logfile=None):
    """
    Run hexdump tests. Requires hexfile.bin to be in the same
    directory as hexdump.py itself.
    """

    class TeeOutput:
        def __init__(self, stream1, stream2):
            self.outputs = [stream1, stream2]

        # -- methods from sys.stdout / sys.stderr
        def write(self, data):
            for stream in self.outputs:
                if 'b' in stream.mode:
                    data = data.encode('utf-8')
                stream.write(data)
                stream.flush()

        def tell(self):
            raise IOError

        def flush(self):
            for stream in self.outputs:
                stream.flush()

        # --/ sys.stdout

    if logfile:
        openlog = open(logfile, 'wb')
        # copy stdout and stderr streams to log file
        savedstd = sys.stderr, sys.stdout
        sys.stderr = TeeOutput(sys.stderr, openlog)
        sys.stdout = TeeOutput(sys.stdout, openlog)

    def echo(msg, linefeed=True):
        sys.stdout.write(msg)
        if linefeed:
            sys.stdout.write('\n')

    expected = '''\
00000000: 00 00 00 5B 68 65 78 64  75 6D 70 5D 00 00 00 00  ...[hexdump]....
00000010: 00 11 22 33 44 55 66 77  88 99 0A BB CC DD EE FF  .."3DUfw........\
'''

    # get path to hexfile.bin
    # this doesn't work from .zip
    #   import os.path as osp
    #   hexfile = osp.dirname(osp.abspath(__file__)) + '/hexfile.bin'
    # this doesn't work either
    #   hexfile = osp.dirname(sys.modules[__name__].__file__) + '/hexfile.bin'
    # this works
    binfile = pkgutil.get_data('hexdump', 'data/hexfile.bin')

    # various length of input data
    hexdump(b'zzzz' * 12)
    hexdump(b'o' * 17)
    hexdump(b'p' * 24)
    hexdump(b'q' * 26)
    # allowable character set filter
    hexdump(b'line\nfeed\r\ntest')
    # fmt: off
    hexdump(
        b'\x00\x00\x00\x5B\x68\x65\x78\x64\x75\x6D\x70\x5D\x00\x00\x00\x00'
        b'\x00\x11\x22\x33\x44\x55\x66\x77\x88\x99\x0A\xBB\xCC\xDD\xEE\xFF'
    )
    # fmt: on
    print('---')
    # dumping file-like binary object to screen (default behavior)
    hexdump(binfile)
    print('return output')
    hexout = hexdump(binfile, result='return')
    assert hexout == expected, 'returned hex didn\'t match'
    print('return generator')
    hexgen = hexdump(binfile, result='generator')
    assert (
        next(hexgen) == expected.split('\n', maxsplit=1)[0]
    ), 'hex generator 1 didn\'t match'
    assert next(hexgen) == expected.split('\n')[1], 'hex generator 2 didn\'t match'

    # binary restore test
    bindata = restore(
        '''
00000000: 00 00 00 5B 68 65 78 64  75 6D 70 5D 00 00 00 00  ...[hexdump]....
00000010: 00 11 22 33 44 55 66 77  88 99 0A BB CC DD EE FF  .."3DUfw........
'''
    )
    echo('restore check ', linefeed=False)
    assert binfile == bindata, 'restore check failed'
    echo('passed')

    far = '''\
000000000: 00 00 00 5B 68 65 78 64 ¦ 75 6D 70 5D 00 00 00 00     [hexdump]
000000010: 00 11 22 33 44 55 66 77 ¦ 88 99 0A BB CC DD EE FF   ?"3DUfwˆ™ª»ÌÝîÿ
'''
    echo('restore far format ', linefeed=False)
    assert binfile == restore(far), 'far format check failed'
    echo('passed')

    scapy = '''\
00 00 00 5B 68 65 78 64 75 6D 70 5D 00 00 00 00  ...[hexdump]....
00 11 22 33 44 55 66 77 88 99 0A BB CC DD EE FF  .."3DUfw........
'''
    echo('restore scapy format ', linefeed=False)
    assert binfile == restore(scapy), 'scapy format check failed'
    echo('passed')

    assert restore('5B68657864756D705D') == b'[hexdump]', 'no space check failed'
    assert dump(b'\\\xa1\xab\x1e', sep='').lower() == '5ca1ab1e'

    print('---[test file hexdumping]---')

    hexfile = tempfile.NamedTemporaryFile(delete=False)
    try:
        hexfile.write(binfile)
        hexfile.close()
        hexdump(open(hexfile.name, 'rb'))
    finally:
        os.remove(hexfile.name)
    if logfile:
        sys.stderr, sys.stdout = savedstd
        openlog.close()


def main(argv=None):  # pragma: no cover
    if argv is None:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser(
        usage='''
        %(prog)s [binfile|-]
        %(prog)s -r hexfile
        %(prog)s --test [logfile]''',
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    parser.add_argument(
        '-r',
        '--restore',
        nargs='?',
        help='restore binary from hex dump',
    )
    parser.add_argument(
        'binfile',
        nargs='?',
        type=argparse.FileType('rb'),
        help='binary input file or stdin',
    )
    parser.add_argument(
        '--test',
        nargs='?',
        type=str,
        const=True,
        default=None,
        metavar="LOGFILE",
        help='run %(prog)s sanity checks with optional logfile',
    )

    args = parser.parse_args()

    if args.test:
        if args.test is True:
            runtest()
        else:
            runtest(logfile=args.test)
    elif not len(argv) > 0:
        parser.print_help()
        sys.exit(0)
    else:
        # dump file
        if not args.restore:
            # [x] memory effective dump
            hexdump(args.binfile)
        # restore file
        else:
            # prepare input stream
            instream = args.restore
            # output stream
            # [ ] memory efficient restore
            sys.stdout.buffer.write(restore(instream.read()))


if __name__ == '__main__':
    main()  # pragma: no cover

# [x] file restore from command line utility
# [ ] write dump with LF on Windows for consistency
# [ ] encoding param for hexdump()ing Python 3 str if anybody requests that

# [ ] document chunking API
# [ ] document hexdump API
# [ ] blog about sys.stdout text mode problem on Windows
