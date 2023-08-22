import os.path
import time
from selenium import webdriver
from selene import browser

from tests.conftest import tmp_dir, path_to_file_tmp

# TODO оформить в тест, добавить ассерты и использовать универсальный путь к tmp
options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": tmp_dir,
    "download.prompt_for_download": False
}
options.add_experimental_option("prefs", prefs)
browser.config.driver_options = options

tmp_zip = path_to_file_tmp('pytest-main.zip')


def test_download_with_ui():
    browser.open("https://github.com/pytest-dev/pytest")
    browser.element(".d-none .Button-label").click()
    browser.element('[data-open-app="link"]').click()

    for i in range(5):
        if not os.path.exists(tmp_zip):
            time.sleep(1)
    assert os.path.exists(tmp_zip)
