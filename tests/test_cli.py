import os
import shutil

import pytest

from mbdl.const import magic


@pytest.mark.parametrize('directories, out',
                         [
                             ("./tests/files/dA ./tests/files/B.txt", "./tests/out/1.mbdl"),
                             ("./tests/files", "./tests/out/1.mbdl"),
                         ])
def test_cli_bundle(directories, out):
    cmd = os.system("python ./mbdl/main.py bundle " + directories + " -o " + out)
    assert cmd == 0
    assert os.path.exists(out)
    assert os.path.getsize(out) > len(magic)


@pytest.mark.parametrize('file, out',
                         [
                             ("./tests/out/1.mbdl", "./tests/out/1"),
                             ("./tests/out/1.mbdl", "./tests/out/1"),
                         ])
def test_cli_unbundle(file, out):
    if os.path.exists(out):
        cmd = os.system("python ./mbdl/main.py unbundle " + file + " " + out)
        assert cmd != 0
        shutil.rmtree(out)

    cmd = os.system("python ./mbdl/main.py unbundle " + file + " " + out)
    assert cmd == 0

    assert os.path.exists(out)
    assert os.path.isdir(out)
    assert os.path.exists(os.path.join(out, "dA"))