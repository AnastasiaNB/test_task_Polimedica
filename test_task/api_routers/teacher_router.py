from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import get_async_session
from models import Course, Teacher
from schemas import TeacherGetSchema


teacher_router = APIRouter()


@teacher_router.get(
    '/teachers',
    response_model=List[TeacherGetSchema]
)
async def get_teachers(
    session: AsyncSession = Depends(get_async_session)
):
    query = select(
        Teacher.id, Teacher.first_name,
        Teacher.last_name, Course.course_name
    ).join(Course, Teacher.course_id == Course.id)
    teachers = await session.execute(query)
    result = teachers.all()
    return result
