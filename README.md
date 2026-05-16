# Student Management System API

A production-ready Django REST Framework API for managing educational institution data — students, teachers, courses, departments, and enrollments — with JWT authentication, Redis caching, Celery background tasks, and PostgreSQL database support.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | Django 5.2.8 + Django REST Framework |
| Auth | JWT via `djangorestframework-simplejwt` |
| Database | PostgreSQL (via psycopg2) |
| Cache | Redis (`django-redis`) |
| Task Queue | Celery + Redis broker |
| API Docs | drf-spectacular (Swagger & ReDoc) |
| Filtering | `django-filter` |
| Container | Docker + Docker Compose |

---

## Project Structure

```
students/                        ← Django project root (settings, urls, wsgi, celery)
├── api/                         ← Student model, serializer, viewset
├── users/                       ← Custom user model + auth endpoints
├── departments/                 ← Department CRUD
├── courses/                     ← Course CRUD
├── teachers/                    ← Teacher CRUD
├── enrollments/                 ← Enrollment CRUD
├── attendance/                  ← (placeholder)
├── results/                     ← (placeholder)
├── docker-compose.yml
├── Dockerfile
├── manage.py
└── requirements.txt
```

---

## Quick Start (Docker — Recommended)

### 1. Clone & configure environment

```bash
git clone <repository-url>
cd students
cp .env.example .env   # then edit .env with your values
```

Minimum `.env` contents:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_ENGINE=django.db.backends.postgresql
DB_NAME=student_db
DB_USER=student_user
DB_PASSWORD=student123
DB_HOST=db
DB_PORT=5432

CACHE_LOCATION=redis://redis:6379/0
REDIS_URL=redis://redis:6379/1
```

### 2. Start all services

```bash
docker compose up --build
```

This starts: **PostgreSQL**, **Redis**, **Django (Gunicorn)**, **Celery worker**, and **Celery Beat**.

The API will be available at `http://localhost:8000`.

---

## Quick Start (Local / Without Docker)

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

> Make sure a PostgreSQL and Redis instance are running and your `.env` is configured to point to them.

---

## Authentication

The API uses **JWT Bearer tokens**. All endpoints (except register and login) require an `Authorization: Bearer <access_token>` header.

| Endpoint | Method | Description |
|---|---|---|
| `/users/register/` | POST | Create a new user account |
| `/users/login/` | POST | Login with email + password, returns tokens |
| `/users/logout/` | POST | Blacklist the refresh token |
| `/users/token/refresh/` | POST | Obtain a new access token |

### Register

```bash
curl -X POST http://localhost:8000/users/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "naimur", "email": "naimur@diu.edu.bd", "password": "pass1234"}'
```

### Login

```bash
curl -X POST http://localhost:8000/users/login/ \
  -H "Content-Type: application/json" \
  -d '{"email": "naimur@diu.edu.bd", "password": "pass1234"}'
```

Response includes `tokens.access` and `tokens.refresh`. Use the access token in subsequent requests:

```bash
-H "Authorization: Bearer <access_token>"
```

---

## API Endpoints

### Departments — `/departments/`

| Method | URL | Action |
|---|---|---|
| GET | `/departments/` | List all departments |
| POST | `/departments/` | Create department |
| GET | `/departments/{id}/` | Get department |
| PUT | `/departments/{id}/` | Full update |
| PATCH | `/departments/{id}/` | Partial update |
| DELETE | `/departments/{id}/` | Delete |

**Filters:** `name`, `code`  
**Search:** `name`, `code`  
**Ordering:** `name`, `code`

---

### Students — `/api/students/`

| Method | URL | Action |
|---|---|---|
| GET | `/api/students/` | List all students |
| POST | `/api/students/` | Create student |
| GET | `/api/students/{id}/` | Get student |
| PATCH | `/api/students/{id}/` | Partial update |
| DELETE | `/api/students/{id}/` | Delete |

**Filters:** `department`, `department__name`, `gender`  
**Search:** `name`, `student_id`, `email`, `phone`, `address`, `gender`, `department__name`  
**Ordering:** `name`

---

### Teachers — `/teachers/`

| Method | URL | Action |
|---|---|---|
| GET | `/teachers/teachers/` | List all teachers |
| POST | `/teachers/teachers/` | Create teacher |
| GET | `/teachers/teachers/{id}/` | Get teacher |
| PATCH | `/teachers/teachers/{id}/` | Partial update |
| DELETE | `/teachers/teachers/{id}/` | Delete |

**Filters:** `department`, `department__name`, `designation`  
**Search:** `name`, `teacher_id`, `designation`, `email`, `department__name`  
**Ordering:** `name`, `department__name`

---

### Courses — `/courses/`

| Method | URL | Action |
|---|---|---|
| GET | `/courses/courses/` | List all courses |
| POST | `/courses/courses/` | Create course |
| GET | `/courses/courses/{id}/` | Get course |
| PUT | `/courses/courses/{id}/` | Full update |
| PATCH | `/courses/courses/{id}/` | Partial update |
| DELETE | `/courses/courses/{id}/` | Delete |

**Filters:** `department__name`, `semester`  
**Search:** `title`, `code`, `semester`, `department__name`  
**Ordering:** `title`, `code`

---

### Enrollments — `/enrollments/`

| Method | URL | Action |
|---|---|---|
| GET | `/enrollments/enrollments/` | List all enrollments |
| POST | `/enrollments/enrollments/` | Create enrollment |
| GET | `/enrollments/enrollments/{id}/` | Get enrollment |
| PATCH | `/enrollments/enrollments/{id}/` | Partial update |
| DELETE | `/enrollments/enrollments/{id}/` | Delete |

**Filters:** `student`, `course`, `course__title`  
**Search:** `student__name`, `course__title`, `enrollment_date`  
**Ordering:** `enrollment_date`, `student__name`, `course__title`

---

### Users — `/users/`

| Method | URL | Action |
|---|---|---|
| GET | `/users/allusers/` | List all users (admin) |
| GET | `/users/allusers/{id}/` | Get user |
| PATCH | `/users/allusers/{id}/` | Update user |
| DELETE | `/users/allusers/{id}/` | Delete user |

---

## Pagination

All list endpoints support `LimitOffsetPagination`:

```
GET /api/students/?limit=10&offset=0
```

---

## Data Models

### Student
```json
{
  "id": 1,
  "name": "Md Rahim",
  "student_id": "STD2025001",
  "email": "rahim@example.com",
  "phone": "01710000001",
  "address": "Dhaka",
  "gender": "male",
  "dob": "2003-05-11",
  "admission_date": "2021-01-10",
  "department": 1,
  "department_name": "Computer Science & Engineering"
}
```

### Teacher
```json
{
  "id": 1,
  "name": "Dr. Ahsan Habib",
  "teacher_id": "TCH1001",
  "designation": "Professor",
  "email": "ahsan@example.com",
  "phone": "01820000001",
  "address": "Dhaka",
  "department": 1,
  "department_name": "Computer Science & Engineering"
}
```

### Course
```json
{
  "id": 1,
  "title": "Introduction to Programming",
  "code": "CSE101",
  "credit": "3.00",
  "semester": 1,
  "department": 1,
  "department_name": "Computer Science & Engineering"
}
```

### Enrollment
```json
{
  "id": 1,
  "student": 1,
  "course": 1,
  "enrollment_date": "2024-11-05",
  "student_detail": { "...": "full student object" },
  "course_detail": { "...": "full course object" },
  "created_at": "2024-11-05T10:00:00Z"
}
```

---

## Caching

Redis-backed caching is applied to all list and detail endpoints with a **15-minute TTL** (10 minutes for enrollments). Cache is automatically invalidated on any write operation (create / update / delete).

Cache key pattern:
- List: `sms:student_list_<query_params>`
- Detail: `sms:student_detail_<pk>`

---

## API Documentation

Interactive API docs are auto-generated via `drf-spectacular`:

| UI | URL |
|---|---|
| Swagger | `http://localhost:8000/api/docs/` |
| ReDoc | `http://localhost:8000/api/redoc/` |
| Raw Schema | `http://localhost:8000/api/schema/` |

---

## Admin Panel

Access at `http://localhost:8000/admin/` using superuser credentials.

Registered models: `CustomUser`, `Student`, `Teacher`, `Course`, `Department`, `Enrollment`

---

## Load Demo Data

```bash
python manage.py loaddata students_demo.json
```

Loads 3 departments, 5 students, 4 teachers, 5 courses, and 50 enrollments.

---

## Docker Services

| Service | Container | Port |
|---|---|---|
| Django (Gunicorn) | `sms_django` | 8000 |
| PostgreSQL | `sms_postgres` | 5432 |
| Redis | `sms_redis` | 6379 |
| Celery Worker | `sms_celery` | — |
| Celery Beat | `sms_celery_beat` | — |

---

## CI/CD Pipeline

This project uses **GitHub Actions** for automated testing and deployment.

### Pipeline Overview

| Job | Trigger | Description |
|---|---|---|
| `test` | Every push to `main` | Lint, migrate, and run tests |
| `docker` | Push to `main` (after test passes) | Build and push Docker image to Docker Hub |

### What Happens on `git push origin main`

1. **Lint** — Checks for syntax errors using flake8
2. **Migrate** — Runs migrations against a temporary test database
3. **Test** — Runs `python manage.py test`
4. **Migration check** — Ensures no migrations are missing
5. **Docker build & push** — Builds and pushes the image to Docker Hub if all steps pass

### Required GitHub Secrets

Go to **Repository → Settings → Secrets and variables → Actions** and add the following:

| Secret | Description |
|---|---|
| `SECRET_KEY` | Django secret key |
| `DB_NAME` | PostgreSQL database name |
| `DB_USER` | PostgreSQL username |
| `DB_PASSWORD` | PostgreSQL password |
| `DOCKERHUB_USERNAME` | Docker Hub username |
| `DOCKERHUB_TOKEN` | Docker Hub access token |

### Docker Image Tags

Each successful push to `main` produces three tags:

| Tag | Description |
|---|---|
| `latest` | Most recent build from `main` |
| `main` | Branch name tag |
| `sha-xxxxxxx` | Short commit SHA — useful for rollbacks |


---

## JWT Token Lifetime

| Token | Lifetime |
|---|---|
| Access | 60 days |
| Refresh | 10 days |

Refresh token rotation and blacklisting are enabled.

---

## Future Enhancements

- Results / grading module (model scaffolded)
- Attendance tracking module (model scaffolded)
- Role-based permissions (admin / teacher / student)
- File upload for profile photos
- Email notifications via Celery tasks
- Analytics and reporting endpoints

---

## License

MIT License — open source and free to use.