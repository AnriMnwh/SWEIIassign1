from App.database import db

class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)
    staff = db.relationship('CourseStaff', back_populates='course')

    def __init__(self, name):
        self.name = name

class Staff(db.Model):
    __tablename__ = 'staff'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    courses = db.relationship('CourseStaff', back_populates='staff')

    def __init__(self, name, role):
        self.name = name
        self.role = role

