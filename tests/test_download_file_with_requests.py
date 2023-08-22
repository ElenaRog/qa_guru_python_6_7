import os.path
import requests
from tests.conftest import path_to_file_tmp

url = 'https://selenium.dev/images/selenium_logo_square_green.png'

tmp_logo = path_to_file_tmp('selenium_logo.png')
# TODO оформить в тест, добавить ассерты, сохранять и читать из tmp, использовать универсальный путь


def test_download_png_with_request(tmp_dir_manager):
    response = requests.get(url)
    assert response.status_code == 200

    with open(tmp_logo, 'wb') as file:
        file.write(response.content)
    assert os.path.exists(tmp_logo)

    size = os.path.getsize(tmp_logo)
    assert size == 30803
