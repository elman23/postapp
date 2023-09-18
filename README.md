# Python FastAPI

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
uvicorn main:app
```

## Links

Tutorial: from [freeCodeCamp](https://www.youtube.com/watch?v=0sOvCWFmrtA).