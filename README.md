# School Registration API

A small Python API project for managing teacher and course registration records. The project uses **FastAPI** to expose HTTP endpoints and **SQLite** for local data storage.

## Features

- Retrieve teacher records.
- Retrieve course records.
- Create teacher and course records through the API.
- Update teacher and course records by ID.
- Delete teacher and course records by ID.
- Automatically create the SQLite tables when the application starts.

## Tech stack

- Python
- FastAPI
- Pydantic
- SQLite

## Project structure

```text
My_registration_app/
└── app/
    ├── main.py       # FastAPI application and API routes
    └── database.py   # SQLite connection and database operations
```

The SQLite database file (`school.db`) is created locally when the application runs. It is intentionally excluded from version control.

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/Susanwanjiruu/My_registration_app.git
cd My_registration_app
```

### 2. Create and activate a virtual environment

On Linux or macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install fastapi uvicorn
```

### 4. Start the API

The application imports its database module from the app directory, so run the server from that directory:

```bash
cd app
uvicorn main:app --reload
```

The API will be available at:

- API root: http://127.0.0.1:8000/
- Interactive Swagger documentation: http://127.0.0.1:8000/docs
- ReDoc documentation: http://127.0.0.1:8000/redoc

## API endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Display the API welcome message |
| GET | `/teachers` | Retrieve teachers from the SQLite database |
| POST | `/teachers` | Submit a teacher record |
| PUT | `/teachers/{teacher_id}` | Update a teacher record |
| DELETE | `/teachers/{teacher_id}` | Delete a teacher record |
| GET | `/courses` | Retrieve courses from the SQLite database |
| POST | `/courses` | Submit a course record |
| PUT | `/courses/{course_id}` | Update a course record |
| DELETE | `/courses/{course_id}` | Delete a course record |

Use the interactive API documentation at `/docs` to inspect the request schemas and try the endpoints.

## Current implementation notes

This is an early learning project. The current POST endpoints append submitted records to in-memory lists, while the GET, PUT, and DELETE operations use SQLite. As a result, records submitted through POST are not currently persisted to the database. This is a known consistency issue to address in a future improvement.

The database schema includes teacher fields such as name, identification number, department, email, and age. Use fictional test data when experimenting; do not commit real personal information or local database files.

## Future improvements

- Make POST operations save records to SQLite.
- Add validation and consistent responses for missing record IDs.
- Add automated tests.
- Add a dependency file such as `requirements.txt`.
- Improve error handling and API response schemas.

## License

No license has been specified for this project yet.
