# Django HTMX MeiliSearch

## Getting started

This project uses docker and docker-compose


```bash
docker-compose build
make migrate_d
make run_d
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
