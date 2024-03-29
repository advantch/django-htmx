## --------------------------------------------------------------------------------------------------
## Welcome to the Makefile docs
##
## Please see below for a list of commands available
## If you face any issues you can run the commands manually.
## --------------------------------------------------------------------------------------------------

help:  ## makefile documentation.
	@sed -ne '/@sed/!s/## //p' $(MAKEFILE_LIST)

run: ## run project
	python3 manage.py runserver 0.0.0.0:8000

lint: ## lint & format
	pre-commit run --all-files

app: ## make a new app
	mkdir ./apps/$(a)
	django-admin startapp $(a) ./apps/$(a)

migrate: ## migrate
	python3 manage.py makemigrations
	python3 manage.py migrate

seed_db: ## seed db
	python3 manage.py seed_db
