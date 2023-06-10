from pydantic import BaseModel


class StudentAddSchema(BaseModel):
    first_name: str
    last_name: str
    group_id: int

    class Config:
        orm_mode = True


class StudentGetSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    group_name: str

    class Config:
        orm_mode = True


class DeleteStudentSchema(BaseModel):
    detail: str = 'Student wuth id = {id} deleted.'


class TeacherGetSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    course_name: str

    class Config:
        orm_mode = True


class CourseAddSchema(BaseModel):
    course_name: str

    class Config:
        orm_mode = True


class CourseGetSchema(BaseModel):
    id: int
    course_name: str

    class Config:
        orm_mode = True


class ExamGradeAddSchema(BaseModel):
    course_id: int
    student_id: int
    grade_id: int
    semester_id: int

    class Config:
        orm_mode = True


class ExamGradeGetSchema(BaseModel):
    id: int
    course_name: str
    first_name: str
    last_name: str
    grade_name: str
    semester_name: str

    class Config:
        orm_mode = True


class ExamGradePutSchema(BaseModel):
    grade_id: int

    class Config:
        orm_mode = True
