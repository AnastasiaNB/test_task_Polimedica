from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from database import Base


class Faculty(Base):
    __tablename__ = 'faculty'

    id: int = Column('id', Integer, primary_key=True)
    faculty_name: str = Column('faculty_name', String)


class Department(Base):
    __tablename__ = 'department'

    id: int = Column('id', Integer, primary_key=True)
    department_name: str = Column('department_name', String)
    faculty_id: int = Column('faculty_id', Integer, ForeignKey('faculty.id'))


class Group(Base):
    __tablename__ = 'groups'

    id: int = Column('id', Integer, primary_key=True)
    group_name: str = Column('group_name', String)
    department_id: int = Column(
        'department_id',
        Integer,
        ForeignKey('department.id')
    )


class Teacher(Base):
    __tablename__ = 'teacher'

    id: int = Column('id', Integer, primary_key=True)
    first_name: str = Column('first_name', String)
    last_name: str = Column('last_name', String)
    course_id: int = Column('course_id', Integer, ForeignKey('course.id'))


class Student(Base):
    __tablename__ = 'student'

    id: int = Column('id', Integer, primary_key=True)
    first_name: str = Column('first_name', String)
    last_name: str = Column('last_name', String)
    group_id: int = Column('group_id', Integer, ForeignKey('groups.id'))


class Building(Base):
    __tablename__ = 'building'

    id: int = Column('id', Integer, primary_key=True)
    building_name: str = Column('building_name', String)


class Room(Base):
    __tablename__ = 'room'

    id: int = Column('id', Integer, primary_key=True)
    room_name: str = Column('room_name', String)
    building_id: int = Column(
        'building_id',
        Integer,
        ForeignKey('building.id')
    )


class Course(Base):
    __tablename__ = 'course'

    id: int = Column('id', Integer, primary_key=True)
    course_name: str = Column('course_name', String)


class Grade(Base):
    __tablename__ = 'grade'

    id: int = Column('id', Integer, primary_key=True)
    grade_name: str = Column('grade_name', String)


class Semester(Base):
    __tablename__ = 'semester'

    id: int = Column('id', Integer, primary_key=True)
    semester_name: str = Column('semester_name', String)


class Timetable(Base):
    __tablename__ = 'timetable'

    id: int = Column('id', Integer, primary_key=True)
    teacher_id: int = Column('teacher_id', Integer, ForeignKey('teacher.id'))
    group_id: int = Column('group_id', Integer, ForeignKey('groups.id'))
    room_id: int = Column('room_id', Integer, ForeignKey('room.id'))
    date_time: datetime = Column('datetime', DateTime)


class Exam(Base):
    __tablename__ = 'exam'

    id: int = Column('id', Integer, primary_key=True)
    course_id: int = Column('course_id', Integer, ForeignKey('course.id'))
    student_id: int = Column('student_id', Integer, ForeignKey('student.id'))
    grade_id: int = Column('grade_id', Integer, ForeignKey('grade.id'))
    semester_id: int = Column(
        'semester_id',
        Integer,
        ForeignKey('semester.id')
    )


class Task(Base):
    __tablename__ = 'task'

    id: int = Column('id', Integer, primary_key=True)
    course_id: int = Column('course_id', Integer, ForeignKey('course.id'))
    student_id: int = Column('student_id', Integer, ForeignKey('student.id'))
    grade_id: int = Column('grade_id', Integer, ForeignKey('grade.id'))
    program_id: int = Column(
        'program_id',
        Integer,
        ForeignKey('course_program.id')
    )
    created_on: datetime = Column('created_on', DateTime)
    text: str = Column('task', String)


class CourseProgram(Base):
    __tablename__ = 'course_program'

    id: int = Column('id', Integer, primary_key=True)
    course_id: int = Column('course_id', Integer, ForeignKey('course.id'))
    topic: str = Column('topic', String)
    hours: int = Column('hours', Integer)
    semester_id: int = Column(
        'semester_id',
        Integer,
        ForeignKey('semester.id')
    )


class StudyPlan(Base):
    __tablename__ = 'study_plan'

    id: int = Column('id', Integer, primary_key=True)
    semester_id: int = Column(
        'semester_id',
        Integer,
        ForeignKey('semester.id')
    )
    course_id: int = Column('course_id', Integer, ForeignKey('course.id'))
    group_id: int = Column('group_id', Integer, ForeignKey('groups.id'))
