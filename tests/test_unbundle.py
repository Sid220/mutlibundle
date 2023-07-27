import argparse
import os
import shutil

import pytest
from mbdl import libmbdl


@pytest.mark.parametrize('file, out',
                         [
                             ("./tests/out/1.mbdl", "./tests/out/1"),
                             ("./tests/out/1.mbdl", "./tests/out/1"),
                         ])
def test_unbundle(file, out):
    if os.path.exists(out):
        shutil.rmtree(out)
    libmbdl.unbundle(file, argparse.Namespace(output=out, keep_full_path=False, verbose=True))
    assert os.path.exists(out)
    assert os.path.isdir(out)
    assert os.path.exists(os.path.join(out, "dA"))
