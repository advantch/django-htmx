# Django HTMX MeiliSearch

## Getting started

This project uses docker and docker-compose


```bash

docker-compose build
make migrate_d

# seed db with dummy data
make seed_db


# finally add the docs to the search engine
make update_index

# run the app
make run_d
```

### Database
The project is set up to use postgres.

To use sqlite replace the default database with the following:

```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

### Add a new app

```
mkdir apps/app-name
djangoadmin startapp app-name ./apps/app-name
```

### Utilities

The project includes some utilities to help you get up and running.

```
# add sample data to the database
make seed_db

# setup and index your instance
make update_index

# clear index
make clear_index
```
