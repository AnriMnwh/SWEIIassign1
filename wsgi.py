import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize )


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)

from App.controllers import model_control #my code starts here as I tried to figure out how to write it properly and didnt want to break it

course_cli = AppGroup('course', help='Course object commands')

@course_cli.command("create", help="Creates a course")
@click.argument("course_name")
def createcourse(course_name):
    model_control.createcourse(course_name)
    print(f'Course {course_name} created!')

@course_cli.command("assign", help="Assigns staff to a course")
@click.argument("course_id")
@click.argument("staff_id")
def assignstaff(course_id, staff_id):
    model_control.assignstaff(course_id, staff_id)
    print(f'Staff with ID {staff_id} assigned to course with ID {course_id}!')

@course_cli.command("view_staff", help="View staff assigned to a course")
@click.argument("course_id")
def viewstaff(course_id):
    staff = model_control.getstaff(course_id)
    print(f'Staff for course with ID {course_id}: {staff}')

@course_cli.command("view", help="View a course")
@click.argument("course_id")
def viewcourse(course_id):
    course = model_control.viewcourse(course_id)
    if course:
        print(f'Course ID: {course["id"]}, Course Name: {course["name"]}')
        for staff in course['staff']:
            print(f'Staff Name: {staff[0]}, Role: {staff[1]}')
    else:
        print(f'Course with ID {course_id} not found.')

app.cli.add_command(course_cli)

staff_cli = AppGroup('staff', help='Staff object commands')

@staff_cli.command("create_lecturer", help="Creates a lecturer")
@click.argument("lecturer_name")
def createlecturer(lecturer_name):
    model_control.createlecturer(lecturer_name)
    print(f'Lecturer {lecturer_name} created!')

@staff_cli.command("create_ta", help="Creates a TA")
@click.argument("ta_name")
def createta(ta_name):
    model_control.createta(ta_name)
    print(f'TA {ta_name} created!')

@staff_cli.command("create_tutor", help="Creates a tutor")
@click.argument("tutor_name")
def createtutor(tutor_name):
    model_control.createtutor(tutor_name)
    print(f'Tutor {tutor_name} created!')

app.cli.add_command(staff_cli)

