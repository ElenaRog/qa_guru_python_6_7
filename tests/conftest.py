import glob
import os

import pytest

tmp_dir = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'tmp'
)

res_dir = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'resources'
)


def path_to_file_tmp(filename):
    return (os.path.join(
        tmp_dir, filename
    ))


def path_to_file_res(filename):
    return (os.path.join(
        res_dir, filename
    ))


@pytest.fixture(scope='function')
def tmp_dir_manager():
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)

    yield

    files = glob.glob(os.path.join(tmp_dir, '*'))
    for file in files:
        os.remove(file)
