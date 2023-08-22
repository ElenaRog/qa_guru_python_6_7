import csv
import os.path

from tests.conftest import path_to_file_res

eggs = path_to_file_res('eggs.csv')
# TODO оформить в тест, добавить ассерты и использовать универсальный путь


def test_csv_writenread():
    with open(eggs, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

        assert os.path.exists(eggs)

    with open(eggs) as csvfile:
        csvreader = csv.reader(csvfile)
        for i, row in enumerate(csvreader):
            if i == 0:
                assert row == ['Anna', 'Pavel', 'Peter']
            elif i == 1:
                assert row == ['Alex', 'Serj', 'Yana']
            else:
                assert i < 3, 'Wrong number of rows'
