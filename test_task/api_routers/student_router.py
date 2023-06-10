from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from models import Group, Student
from schemas import DeleteStudentSchema, StudentAddSchema, StudentGetSchema

student_router = APIRouter()


@student_router.post(
    '/students',
    response_model=StudentGetSchema
    )
async def add_student(
    student_data: StudentAddSchema,
    session: AsyncSession = Depends(get_async_session)
):
    stmt = insert(Student).values(**student_data.dict())
    await session.execute(stmt)
    await session.commit()
    query = select(
        Student.id, Student.first_name,
        Student.last_name, Group.group_name
    ).join(Group, Student.group_id == Group.id)
    students = await session.execute(query)
    result = students.all()[-1]
    return result


@student_router.get(
    '/students/{id}',
    response_model=StudentGetSchema,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "content": {
                "application/json": {
                    "examples": {
                        'STUDENT DOES NOT EXIST': {
                            "summary": "Student does not exist",
                            "value": {"detail": 'Student with id={id} does not exist'},
                        },
                    },
                }
            }
        }
    }
)
async def get_student_by_id(
    id: int,
    session: AsyncSession = Depends(get_async_session)
):
    query = select(
        Student.id, Student.first_name,
        Student.last_name, Group.group_name
    ).join(Group, Student.group_id == Group.id).where(Student.id == id)
    students = await session.execute(query)
    try:
        result = students.all()[0]
        return result
    except IndexError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Student with id={id} does not exist'
        )


@student_router.put(
    '/students/{id}',
    response_model=StudentGetSchema,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "content": {
                "application/json": {
                    "examples": {
                        'STUDENT DOES NOT EXIST': {
                            "summary": "Student does not exist",
                            "value": {"detail": 'Student with id={id} does not exist'},
                        },
                    },
                }
            }
        }
    }
)
async def update_student_by_id(
    id: int,
    student_data: StudentAddSchema,
    session: AsyncSession = Depends(get_async_session)
):
    stmt = update(Student).values(
        **student_data.dict(exclude_unset=True)
    ).where(Student.id == id)
    await session.execute(stmt)
    await session.commit()
    query = select(
        Student.id, Student.first_name,
        Student.last_name, Group.group_name
    ).join(Group, Student.group_id == Group.id).where(Student.id == id)
    students = await session.execute(query)
    try:
        result = students.all()[0]
        return result
    except IndexError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Student with id={id} does not exist'
        )


@student_router.delete(
    '/students/{id}',
    response_model=DeleteStudentSchema
)
async def delete_student_by_id(
    id: int,
    session: AsyncSession = Depends(get_async_session)
):
    stmt = delete(Student).where(Student.id == id)
    await session.execute(stmt)
    await session.commit()
    return {'detail': f'Student with id={id} was deleted.'}
