import csv
import time


STUDENT_LIST_FILE = 'data/student_list.csv'
ATTENDANCE_FILE = f'Attendance_{time.strftime("%Y-%m-%d_%I-%M%p")}.csv'


def main():
    '''
    Runs an infinite loop of scanning students and recording them.

    :returns: None
    '''
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
    '''
    Reads the student data from the STUDENT_LIST_FILE
    Data should be in a csv file with the columns (name, id)

    :returns: A dictionary of all the students in the form {name: id}
    '''
    all_students = {}

    with open(STUDENT_LIST_FILE, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0: # First row is headers (column names)
                print(f'Column names are {", ".join(row)}') # TODO: remove
                line_count += 1
            else:   # Other rows contain Name, ID of students
                student_name = row[0]
                student_id = int(row[1])

                all_students[student_id] = student_name

                print(f'Student: {student_name} ID: {student_id}.') # TODO: remove
                line_count += 1

    print(f'Found data for {line_count} students.') # TODO: remove
    return all_students


def scan_student(all_students):
    '''
    Asks for the input from a single student and looks up the associated name.
    The input can be typed in manually or scanned with a USB scanner

    :param all_students: a dictionary of form {name: id} for all the students 
    :returns: date-time of scan, name of student scanned, student ID number scanned
    '''
    scanned_num = input('[Scan/Enter] Student ID: ')

    try:
        scanned_num = int(scanned_num)
    except ValueError:
        print('[WARNING] Invalid ID number!')
        return None

    if scanned_num in all_students:
        scanned_name = all_students[scanned_num]
    else:
        print('[WARNING] Student name not found.')
        scanned_name = "UNKNOWN"

    print(f'Welcome, {scanned_name}!')
    date = time.strftime("%Y-%m-%d_%I-%M%p")

    return date, scanned_name, scanned_num


def create_attendance_file():
    '''
    Creates the file to store the attendance and writes in the column names

    :returns: None
    '''
    with open(ATTENDANCE_FILE, mode='w') as file:
        student_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        student_writer.writerow(["Date-Time", "Name", "ID Number"])


def record_student(date, name, id_num):
    '''
    Records the attendance of one student in the attendance file

    :param date: a string of the date of the scan
    :param name: a string of the name of the student
    :param id_num: an int of the scanned ID number
    :returns: None
    '''
    with open(ATTENDANCE_FILE, mode='a') as file:
        student_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        student_writer.writerow([date, name, id_num])
