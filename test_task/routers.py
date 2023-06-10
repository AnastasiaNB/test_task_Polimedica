from fastapi import APIRouter

from api_routers.course_router import course_router
from api_routers.grade_router import grade_router
from api_routers.student_router import student_router
from api_routers.teacher_router import teacher_router

router = APIRouter()

router.include_router(student_router, tags=['Students'])
router.include_router(teacher_router, tags=['Teachers'])
router.include_router(course_router, tags=['Courses'])
router.include_router(grade_router, tags=['Grades'])
