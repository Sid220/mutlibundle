import os.path
import argparse
import pytest
from mbdl import libmbdl
from mbdl.const import magic


@pytest.mark.parametrize('directories, out',
                         [
                             ("./tests/files/dA ./tests/files/B.txt", "./tests/out/1.mbdl"),
                             ("./tests/files", "./tests/out/1.mbdl"),
                         ])
def test_bundle(directories, out):
    libmbdl.bundle(directories.split(" "), argparse.Namespace(output=out, keep_full_path=False, verbose=True))
    assert os.path.exists(out)
    assert os.path.getsize(out) > len(magic)
