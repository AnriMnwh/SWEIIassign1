# by Anari Manwah. student ID = 816024772.

# Software Engineering II Assignment 1
This project is based on the staff allocations assigned to me. Below is a list of commands that can be used to interact with the application. The assignment was done locally on PyCharm and committed to the repo through codespaces. It has three files of importance; **control_model.py**, **models.py**, and **wsgi.py** that were modified and created.
I used the offical docs to help me with the formatting of the readme.


### Create a Course
```sh
flask course create <course_name>
```
Creates a new course with the specified name.
- **course_name**: The name of the course to be created.

### Assign Staff to a Course
```sh
flask course assign <course_id> <staff_id>
```
Assigns a staff member to a course.
- **course_id**: The ID of the course.
- **staff_id**: The ID of the staff member.

### View Staff Assigned to a Course
```sh
flask course view_staff <course_id>
```
Displays the staff members assigned to a course.
- **course_id**: The ID of the course.

### View a Course
```sh
flask course view <course_id>
```
Displays details of a course, including assigned staff.
- **course_id**: The ID of the course.

## Staff Commands

### Create a Lecturer
```sh
flask staff create_lecturer <lecturer_name>
```
Creates a new lecturer with the specified name.
- **lecturer_name**: The name of the lecturer to be created.

### Create a TA
```sh
flask staff create_ta <ta_name>
```
Creates a new teaching assistant (TA) with the specified name.
- **ta_name**: The name of the TA to be created.

### Create a Tutor
```sh
flask staff create_tutor <tutor_name>
```
Creates a new tutor with the specified name.
- **tutor_name**: The name of the tutor to be created.
