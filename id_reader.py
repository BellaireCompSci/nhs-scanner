'''
    File name: id_reader.py
    Author: Ryan Knightly (reknightly@gmail.com)
    Date created: 8/14/2018
    Date last modified: 8/14/2018
    Python Version: 2.7
'''

import csv
import time


STUDENT_LIST_FILE = 'student_list.csv'
ATTENDANCE_FILE = f'Attendance_{time.strftime("%Y-%m-%d_%I-%M%p")}.csv'


def main():
    student_data = read_students()
    print('\n READY TO SCAN. \n')
    create_attendance_file()

    while True:
        result = scan_student(student_data)
        if result is None:
            continue
        else:
            date, scanned_name, scanned_num = result
            record_student(date, scanned_name, scanned_num)

def read_students():
    student_list = {}

    with open(STUDENT_LIST_FILE, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            # First row is headers (column names)
            if line_count == 0:
                print(f'Column names are {", ".join(row)}') # TODO: remove
                line_count += 1
            # Other rows contain Name, ID of students
            else:
                student_name = row[0]
                student_id = int(row[1])

                student_list[student_id] = student_name

                print(f'Student: {student_name} ID: {student_id}.') # TODO: remove
                line_count += 1

    print(f'Processed data for {line_count} students.') # TODO: remove
    return student_list


def scan_student(student_list):
    scanned_num = input('[Scan/Enter] Student ID: ')

    try:
        scanned_num = int(scanned_num)
    except ValueError:
        print('[WARNING] Invalid ID number!')
        return None

    if scanned_num in student_list:
        scanned_name = student_list[scanned_num]
    else:
        print('[WARNING] Student name not found.')
        scanned_name = "UNKNOWN"

    print(f'Welcome, {scanned_name}!')
    date = time.strftime("%Y-%m-%d_%I-%M%p")

    return date, scanned_name, scanned_num


def create_attendance_file():
    with open(ATTENDANCE_FILE, mode='w') as file:
        student_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        student_writer.writerow(["Date-Time", "Name", "ID Number"])


def record_student(date, name, id_num):
    with open(ATTENDANCE_FILE, mode='a') as file:
        student_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        student_writer.writerow([date, name, id_num])


if __name__ == '__main__':
    main();
