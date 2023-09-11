import pytest

from hexdump.hexdump import runtest


def test_runtest():
    runtest()

def test_runtest_log(tmp_path):
    d = tmp_path / "log"
    d.mkdir()
    p = d / "log-test.txt"
    logfile = str(p)
    runtest(logfile)
    assert 'check passed' in p.read_text()
