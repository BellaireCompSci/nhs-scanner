import csv
import time


STUDENT_LIST_FILE = 'data/NHSMasterJrsSrs.csv'
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
            date, last_name, first_name, grade, scanned_num = result
            record_student(date, last_name, first_name, grade, scanned_num)


def read_students():
    '''
    Reads the student data from the STUDENT_LIST_FILE
    Data should be in a csv file with the columns (name, id)

    :returns: A dictionary of all the students in the form 
    {
    id: {
        'last-name': '',
        'first-name': '',
        'grade': 0,
        }
    }
    '''
    all_students = {}

    with open(STUDENT_LIST_FILE, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            line_count += 1
            if line_count == 1: # First row is headers (column names)
                # print(f'Column names are {", ".join(row)}') # TODO: remove
                continue
            elif len(row[0]) == 0: # Blank rows (at end of file)
                line_count -= 1
                break
            else:   # Other rows contain Name, ID of students
                student_lastname = row[0]
                student_firstname = row[1]
                student_grade = int(row[2])
                student_id = int(row[3])

                student_data = {'last-name': student_lastname, 
                                'first-name': student_firstname,
                                'grade': student_grade}

                all_students[student_id] = student_data

                # print(f'last-name: {student_lastname}, first-name: {student_firstname}, grade: {student_grade}, ID: {student_id}.') # TODO: remove

    print(f'Using data for {line_count-1} students.') 
    return all_students


def scan_student(all_students):
    '''
    Asks for the input from a single student and looks up the associated name.
    The input can be typed in manually or scanned with a USB scanner

    :param all_students: a dictionary of form {name: id} for all the students 
    :returns: date-time of scan, last name, first name, grede, and ID number of student scanned
    '''
    scanned_num = input('[Scan/Enter] Student ID: ')

    try:
        scanned_num = int(scanned_num)
    except ValueError:
        print('[WARNING] Invalid ID number!')
        return None

    if scanned_num in all_students:
        student_data = all_students[scanned_num]

        last_name = student_data['last-name']
        first_name = student_data['first-name']
        grade = student_data['grade']
    else:
        print('[WARNING] Student name not found.')
        last_name = "UNKNOWN"
        first_name = "UNKNOWN"
        grade = -1

    print(f'Welcome, {first_name} {last_name}!\n')
    date = time.strftime("%Y-%m-%d_%I-%M%p")

    return date, last_name, first_name, grade, scanned_num


def create_attendance_file():
    '''
    Creates the file to store the attendance and writes in the column names

    :returns: None
    '''
    with open(ATTENDANCE_FILE, mode='w') as file:
        student_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        student_writer.writerow(["Date-Time", "Last Name", "First Name", "Grade", "ID Number"])


def record_student(date, last_name, first_name, grade, id_num):
    '''
    Records the attendance of one student in the attendance file

    :param date: a string of the date of the scan
    :param last_name: a string of the last name of the student
    :param first_name: a string of the first name of the student
    :param id_num: an int of the scanned ID number
    :returns: None
    '''
    with open(ATTENDANCE_FILE, mode='a') as file:
        student_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        student_writer.writerow([date, last_name, first_name, grade, id_num])
