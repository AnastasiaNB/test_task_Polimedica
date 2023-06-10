from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from models import Course, Group, Student, StudyPlan
from schemas import CourseAddSchema, CourseGetSchema, StudentGetSchema

course_router = APIRouter()


@course_router.post(
    '/course',
    response_model=CourseGetSchema
)
async def add_course(
    course_data: CourseAddSchema,
    session: AsyncSession = Depends(get_async_session)
):
    stmt = insert(Course).values(**course_data.dict())
    await session.execute(stmt)
    await session.commit()
    query = select(Course.id, Course.course_name)
    result = await session.execute(query)
    return result.all()[-1]


@course_router.get(
    '/course/{id}',
    response_model=CourseGetSchema,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "content": {
                "application/json": {
                    "examples": {
                        'COURSE DOES NOT EXIST': {
                            "summary": "Course does not exist",
                            "value": {"detail": 'Course with id={id} does not exist'},
                        },
                    },
                }
            }
        }
    }
)
async def get_course_by_id(
    id: int,
    session: AsyncSession = Depends(get_async_session)
):
    query = select(
        Course.id, Course.course_name
    ).where(Course.id == id)
    result = await session.execute(query)
    try:
        return result.all()[0]
    except IndexError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Course with id={id} does not exist'
        )


@course_router.get(
    '/course/{id}/students',
    response_model=List[StudentGetSchema]
)
async def get_students_by_course_id(
    id: int,
    session: AsyncSession = Depends(get_async_session)
):
    query_1 = select(StudyPlan.group_id).where(StudyPlan.course_id == id)
    groups = await session.execute(query_1)
    students = []
    for group_id in groups.all():
        query = select(
            Student.id,
            Student.first_name,
            Student.last_name,
            Group.group_name
        ).join(
            Group, Student.group_id == Group.id
        ).where(
            Student.group_id == group_id[0]
        )
        result = await session.execute(query)
        students.extend(result.all())
    return students
