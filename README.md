# Django Tutorials Starter Repo

## Getting started

### Create a virtual env and install requirements

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run

```
python manage.py runserver 0.0.0.0:8000

or 

make run
```

### Add a new app

```
mkdir apps/app-name
djangoadmin startapp app-name ./apps/app-name
```
