from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from models import Course, Exam, Grade, Semester, Student
from schemas import ExamGradeAddSchema, ExamGradeGetSchema, ExamGradePutSchema

grade_router = APIRouter()


@grade_router.post(
    '/grades',
    response_model=ExamGradeGetSchema
)
async def add_exam_grade(
    grade_data: ExamGradeAddSchema,
    session: AsyncSession = Depends(get_async_session)
):
    stmt = insert(Exam).values(**grade_data.dict())
    await session.execute(stmt)
    await session.commit()
    query = select(
        Exam.id,
        Course.course_name,
        Grade.grade_name,
        Student.first_name,
        Student.last_name,
        Semester.semester_name).join(
            Course, Exam.course_id == Course.id
        ).join(
            Grade, Exam.grade_id == Grade.id
        ).join(
            Student, Exam.student_id == Student.id
        ).join(
            Semester, Exam.semester_id == Semester.id
        )
    result = await session.execute(query)
    return result.all()[-1]


@grade_router.put(
    '/grades/{id}',
    response_model=ExamGradeGetSchema,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "content": {
                "application/json": {
                    "examples": {
                        'GRADE DOES NOT EXIST': {
                            "summary": "Grade does not exist",
                            "value": {"detail": 'Grade with id={id} does not exist'},
                        },
                    },
                }
            }
        }
    }
)
async def update_exam_grade_by_id(
    id: int,
    grade_data: ExamGradePutSchema,
    session: AsyncSession = Depends(get_async_session)
):
    stmt = update(Exam).values(
            **grade_data.dict()
        ).where(
            Exam.id == id
        )
    await session.execute(stmt)
    await session.commit()
    query = select(
        Exam.id,
        Course.course_name,
        Grade.grade_name,
        Student.first_name,
        Student.last_name,
        Semester.semester_name).join(
            Course, Exam.course_id == Course.id
        ).join(
            Grade, Exam.grade_id == Grade.id
        ).join(
            Student, Exam.student_id == Student.id
        ).join(
            Semester, Exam.semester_id == Semester.id
        ).where(Exam.id == id)
    result = await session.execute(query)
    try:
        return result.all()[0]
    except IndexError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Grade with id={id} does not exist'
        )
