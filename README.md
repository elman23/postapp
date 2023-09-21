# Post App

A FastAPI project.

## Virtual environments

Create a virtual environment and activate it:
- Windows:
```cmd
py -3 -m venv venv
.\venv\Scripts\activate.bat
```
- Unix:
```bash
python3 -m venv venv
source ./venv/bin/activate
```

## Dependencies

```bash
pip install "fastapi[all]" 
pip freeze > requirements.txt
```

## Run

```bash
uvicorn app.main:app --reload
```

## Documentation

Swagger built-in at: http://localhost:8000/docs.

ReDoc built-in at: http://localhost:8000/redoc.

## Alembic

```bash
alembic init alembic
```

Configure `alembic/env.py`.

```bash
alembic revision -m "create post table"
```

Fill in the `upgrade()` and `downgrade()` functions.

Apply the revision:
```bash
alembic current
alembic upgrade [REVISION_NUMBER]
```

Other commands:
```bash
alembic heads
alembic upgrade head 
```

Downgrade:
```bash
alembic downgrade [REVISION_NUMBER]
alembic downgrade -1
```

Automatically generate features:
```bash
alembic revision --autogenerate -m "[MESSAGE HERE]"
```

## Tests

Run tests with:
```bash
pytest
```

## Links

Tutorial: from [freeCodeCamp](https://www.youtube.com/watch?v=0sOvCWFmrtA).