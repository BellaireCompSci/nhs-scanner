'''
    File name: id_reader.py
    Author: Ryan Knightly (reknightly@gmail.com)
    Date created: 8/14/2018
    Date last modified: 8/14/2018
    Python Version: 2.7
'''

import csv
import datetime

STUDENT_LIST_FILE_NAME = 'student_list.csv'
RECORD_FILE = 'attendance-{date}.csv'.format(date=datetime.datetime.today().strftime('%Y-%m-%d'))

def main():
    student_data = read_students()
    while True:
        scan_student(student_data)
        record_student(date, scanned_name, scanned_num)


def read_students():
    student_list = {}

    with open(STUDENT_LIST_FILE_NAME, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            # First row is headers (column names)
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            # Other rows contain Name, ID of students
            else:
                student_name = row[0]
                student_id = row[1]

                student_list[student_id] = student_name

                print(f'Student: {student_name} ID: {student_id}.')
                line_count += 1

    print(f'Processed data for {line_count} students.')
    return student_list


def scan_student(student_list):
    scanned_num = int(input('Scan student ID: '))
    scanned_name = student_list[scanned_num]
    date = datetime.datetime.today().strftime('%Y-%m-%d')

    return date, scanned_name, scanned_num


def record_student(date, name, id_num):
    with open(RECORD_FILE, mode='w') as employee_file:
        student_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        student_writer.writerow([date, name, id_num])


if __name__ == '__main__':
    main();
