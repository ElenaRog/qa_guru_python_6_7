import os
from zipfile import ZipFile
from tests.conftest import res_dir, path_to_file_tmp, path_to_file_res

zip_test = path_to_file_tmp('resdir.zip')
res_files = os.listdir(res_dir)


def test_compare_folder_with_archive(tmp_dir_manager):
    with ZipFile(zip_test, 'w') as zip_file:
        for file in res_files:
            zip_file.write(path_to_file_res(file), file)

    with ZipFile(zip_test, 'r') as zip_file:
        for file in res_files:
            assert file in zip_file.namelist()
            assert os.stat(path_to_file_res(file)).st_size == zip_file.getinfo(file).file_size
