import os
import re
from src.consts import *


def is_null_or_empty(s):
    return s is None or s == ''


def write_to_file(file_path, string):
    if os.path.exists(file_path):
        mode = 'a'  # Открываем файл в режиме добавления
    else:
        mode = 'w'  # Открываем файл в режиме записи
    with open(file_path, mode, encoding=ENCODING) as file:
        file.write(string)


def write_headers(file_path):
    first_line = read_first_line(file_path)
    if not first_line or not first_line.startswith(HEADERS[0]):
        line = ";".join(HEADERS) + "\n"
        write_to_file(file_path, line)


def read_first_line(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding=ENCODING) as file:
            return file.readline()
    else:
        with open(file_path, 'w'):
            pass
   
   
# def write_headers(file_path):
    # clean_result_file(file_path)
    # line = ";".join(HEADERS) + "\n"
    # write_to_file(file_path, line)
 
 
# def clean_result_file(file_path):
    # with open(file_path, 'w'):
        # pass


def read_stat_id(file_path):
    pattern = re.compile(r'^\d{10}$')
    valid_lines = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                cleaned_line = line.strip()
                if pattern.match(cleaned_line):
                    valid_lines.append(cleaned_line)
    else:
        with open(file_path, 'w'):
            raise f'Добавьте в файл {file_path} номера заявлений в столбик'
    return valid_lines


class Statement:
    def __init__(self, stat_id, target, status, date_in, date_out_max, fullname, birth_date, pay_id, pay_sum, reason):
        self.stat_id = stat_id
        self.target = target
        self.status = status
        self.date_in = date_in
        self.date_out_max = date_out_max
        self.fullname = fullname
        self.birth_date = birth_date
        self.pay_id = '\'' + pay_id
        self.pay_sum = pay_sum
        self.reason = reason.replace('\n', ' ')

    def __str__(self):
        return f"{self.stat_id}"

    def write_body(self, file_path):
        fields = vars(self).values()
        line = ";".join(map(str, fields)) + "\n"
        write_to_file(file_path, line)
