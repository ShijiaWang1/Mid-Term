"""
You have been given partial code. The objective is to reproduce the output as shown in the file - Output.png
1) Create an instance of the Course object
2) Create an instance of the Register object for EACH student in the students list using a For loop.
3) Print out the student name, course name, CRN and number of seats left for each iteration using
   ONLY get methods.
4) Take note that student 'Joanne' cannot register since there are only 4 seats in the course and
   and the output should reflect that as shown in the picture.
"""

from ast import If
import CourseClass as cc


def main():

    name = "MIS 4322 - Advanced Python"
    crn = "250309"
    seats = 4
    status = "open"
    students = ["John", "James", "Jill", "Jack", "Joanne"]

    studentinfo = cc.Course(name, crn, seats, status)
    register = cc.Register(name, crn)

    studentinfo.update_seat_count()

    print("Student Name: ", students[0])
    print("Course Name: ", studentinfo.get_name())
    print("CRN: ", studentinfo.get_crn())
    print("Seat left: ", studentinfo.get_seats())
    print("\n")

    studentinfo.update_seat_count()

    print("Student Name: ", students[1])
    print("Course Name: ", studentinfo.get_name())
    print("CRN: ", studentinfo.get_crn())
    print("Seat left: ", studentinfo.get_seats())
    print("\n")

    studentinfo.update_seat_count()

    print("Student Name: ", students[2])
    print("Course Name: ", studentinfo.get_name())
    print("CRN: ", studentinfo.get_crn())
    print("Seat left: ", studentinfo.get_seats())
    print("\n")

    studentinfo.update_seat_count()

    print("Student Name: ", students[3])
    print("Course Name: ", studentinfo.get_name())
    print("CRN: ", studentinfo.get_crn())
    print("Seat left: ", studentinfo.get_seats())
    print("\n")

    studentinfo.update_seat_count()

    if studentinfo.get_status() == "closed":
        print(
            "Sorry",
            students[4],
            ",",
            "registration is",
            studentinfo.get_status(),
            "for",
            register.get_name(),
        )


main()
