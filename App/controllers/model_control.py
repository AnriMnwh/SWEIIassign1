from App.database import db
from App.models import models
def createcourse(name):
    new_course = models.Course(name=name)
    db.session.add(new_course)
    db.session.commit()

def createlecturer(name):
    new_lecturer = models.Staff(name=name, role='Lecturer')
    db.session.add(new_lecturer)
    db.session.commit()

def createta(name):
    new_ta = models.Staff(name=name, role='TA')
    db.session.add(new_ta)
    db.session.commit()

def createtutor(name):
    new_tutor = models.Staff(name=name, role='Tutor')
    db.session.add(new_tutor)
    db.session.commit()

def assignstaff(course_id, staff_id):
    course = models.Course.query.get(course_id)
    staff = models.Staff.query.get(staff_id)
    if course and staff:
        course.staff.append(staff)
        db.session.commit()

def getstaff(course_id):
    course = models.Course.query.get(course_id)
    if course:
        return [(staff.name, staff.role) for staff in course.staff]
    return []

def viewcourse(course_id):
    course = models.Course.query.get(course_id)
    if course:
        return {
            'id': course.id,
            'name': course.name,
            'staff': [(staff.name, staff.role) for staff in course.staff]
        }
    return None

