# Student Management System API

A comprehensive Django REST Framework-based API for managing educational institution data including students, teachers, courses, departments, and enrollments.

## Features

- **Department Management**: Create and manage academic departments
- **Student Management**: Complete student information system with filtering and search
- **Teacher Management**: Manage faculty information
- **Course Management**: Handle course catalog and details
- **Enrollment System**: Track student course enrollments
- **REST API**: Full CRUD operations for all resources
- **Pagination**: Built-in pagination support
- **Filtering & Search**: Advanced filtering and search capabilities
- **Admin Interface**: Django admin panel for easy management

## Tech Stack

- **Framework**: Django 5.2.8
- **API**: Django REST Framework
- **Database**: SQLite (default)
- **Python**: 3.x

## Installation

### Prerequisites

- Python 3.x installed
- pip package manager

### Setup Steps

1. **Clone the repository**
```bash
git clone <repository-url>
cd students
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install django djangorestframework django-filter
```

4. **Run migrations**
```bash
python manage.py migrate
```

5. **Create a superuser**
```bash
python manage.py createsuperuser
```

6. **Run the development server**
```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

## API Endpoints

### Base URL: `/api/`

### Departments
- `GET /api/department/` - List all departments
- `POST /api/department/` - Create new department
- `GET /api/department/{id}/` - Retrieve department details
- `PUT /api/department/{id}/` - Update department
- `PATCH /api/department/{id}/` - Partial update department
- `DELETE /api/department/{id}/` - Delete department

### Students
- `GET /api/students/` - List all students
- `POST /api/students/` - Create new student
- `GET /api/students/{id}/` - Retrieve student details
- `PATCH /api/students/{id}/` - Update student
- `DELETE /api/students/{id}/` - Delete student

**Query Parameters:**
- `search` - Search by name, student_id, email, phone, address, gender, dob, admission_date
- `ordering` - Order by name
- `department` - Filter by department ID
- `gender` - Filter by gender (male/female)
- `limit` - Pagination limit
- `offset` - Pagination offset

### Teachers
- `GET /api/teachers/` - List all teachers
- `POST /api/teachers/` - Create new teacher
- `GET /api/teachers/{id}/` - Retrieve teacher details
- `PATCH /api/teachers/{id}/` - Update teacher
- `DELETE /api/teachers/{id}/` - Delete teacher

### Courses
- `GET /api/courses/` - List all courses
- `POST /api/courses/` - Create new course
- `GET /api/courses/{id}/` - Retrieve course details
- `PUT /api/courses/{id}/` - Update course
- `PATCH /api/courses/{id}/` - Update course partially
- `DELETE /api/courses/{id}/` - Delete course

### Enrollments
- `GET /api/enrollments/` - List all enrollments
- `POST /api/enrollments/` - Create new enrollment
- `GET /api/enrollments/{id}/` - Retrieve enrollment details
- `PATCH /api/enrollments/{id}/` - Update enrollment
- `DELETE /api/enrollments/{id}/` - Delete enrollment

**Query Parameters:**
- `search` - Search by student ID, course ID, enrollment_date
- `ordering` - Order by enrollment_date, student__id, course__id
- `student` - Filter by student ID
- `course__title` - Filter by course title
- `limit` - Pagination limit
- `offset` - Pagination offset

## Data Models

### Department
```python
{
    "id": integer,
    "name": string,
    "code": string,
    "description": string (optional)
}
```

### Student
```python
{
    "id": integer,
    "name": string,
    "student_id": string (unique),
    "email": string (unique),
    "phone": string (optional),
    "address": string (optional),
    "gender": "male" | "female",
    "dob": date (optional),
    "admission_date": date (optional),
    "department": integer (foreign key),
    "created_at": datetime,
    "updated_at": datetime
}
```

### Teacher
```python
{
    "id": integer,
    "name": string,
    "teacher_id": string (unique),
    "designation": string,
    "email": string (unique),
    "phone": string (optional),
    "address": string (optional),
    "department": integer (foreign key),
    "created_at": datetime
}
```

### Course
```python
{
    "id": integer,
    "title": string,
    "code": string (unique),
    "credit": decimal,
    "semester": integer,
    "department": integer (foreign key),
    "created_at": datetime,
    "updated_at": datetime
}
```

### Enrollment
```python
{
    "id": integer,
    "student": integer (foreign key),
    "course": integer (foreign key),
    "enrollment_date": date (optional),
    "student_name": string (write-only),
    "course_name": string (write-only),
    "created_at": datetime,
    "updated_at": datetime
}
```

## Usage Examples

### Create a Department
```bash
curl -X POST http://127.0.0.1:8000/api/department/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Computer Science",
    "code": "CSE",
    "description": "Department of Computer Science and Engineering"
  }'
```

### Create a Student
```bash
curl -X POST http://127.0.0.1:8000/api/students/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "student_id": "2024001",
    "email": "john@example.com",
    "gender": "male",
    "department": 1
  }'
```

### Search Students
```bash
curl "http://127.0.0.1:8000/api/students/?search=John&department=1"
```

### Create an Enrollment
```bash
curl -X POST http://127.0.0.1:8000/api/enrollments/ \
  -H "Content-Type: application/json" \
  -d '{
    "student_name": "John Doe",
    "course_name": "Data Structures",
    "enrollment_date": "2024-01-15"
  }'
```

## Admin Panel

Access the Django admin panel at `http://127.0.0.1:8000/admin/` using your superuser credentials.

The admin interface provides:
- Visual management of all models
- Search and filter capabilities
- Bulk operations
- Data validation

## Project Structure

```
students/
├── api/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py          # Admin configurations
│   ├── apps.py
│   ├── models.py         # Database models
│   ├── serializers.py    # DRF serializers
│   ├── views.py          # API viewsets
│   └── urls.py           # API URL routing
├── students/
│   ├── __init__.py
│   ├── settings.py       # Project settings
│   ├── urls.py           # Main URL configuration
│   ├── wsgi.py
│   └── asgi.py
├── manage.py
└── db.sqlite3
```

## Configuration

### Settings (`students/settings.py`)

Key configurations:
- `DEBUG = True` - Development mode (set to False in production)
- `ALLOWED_HOSTS = []` - Add your domain in production
- `DATABASES` - Currently using SQLite, can be changed to PostgreSQL/MySQL

### Installed Apps
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api',
]
```

## Known Issues

- `Teacher` model has a syntax error with a comma after `updated_at` field
- `CoursesViewset.destroy()` has a typo: `course.detele()` should be `course.delete()`
- `TeachersViewset.destroy()` returns status 2024 instead of 204
- Commented out `create` and `update` methods in `EnrollmentsSerializer`

## Future Enhancements

- Add authentication and authorization
- Implement grading system
- Add attendance tracking
- Generate reports and analytics
- Add file upload for student/teacher photos
- Implement email notifications
- Add more advanced filtering options

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is open source and available under the MIT License.

## Support

For issues and questions, please create an issue in the repository or contact the development team.

---

**Note**: This is a development version. Please configure proper security settings, use environment variables for sensitive data, and set up a production-grade database before deploying to production.