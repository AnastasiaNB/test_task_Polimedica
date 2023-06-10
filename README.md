# test_task_Polimedica
## API для "Системы управления университетом"
### Запуск:
- git clone git@github.com:AnastasiaNB/test_task_Polimedica.git
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt
- cd src/
- uvicorn main:app --reload
### Документация: http://127.0.0.1:8000/docs#/
### Эндпоинты:
- POST /students - создать нового студента.
- GET /students/{student_id} - получить информацию о студенте по его id.
- PUT /students/{student_id} - обновить информацию о студенте по его id.
- DELETE /students/{student_id} - удалить студента по его id.
- GET /teachers - получить список всех преподавателей.
- POST /courses - создать новый курс.
- GET /courses/{course_id} - получить информацию о курсе по его id.
- GET /courses/{course_id}/students - получить список всех студентов на курсе.
- POST /grades - создать новую оценку для студента по курсу.
- PUT /grades/{grade_id} - обновить оценку студента по курсу.
##### Более подробное описание данных запросов и ответов в документации
##### Задание 1: schema_task1.png - диаграмма БД, revision_sql_task1.txt - SQL-скрипт для создания таблиц БД
##### Задание 2: sql_query_task2.txt