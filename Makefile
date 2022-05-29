## --------------------------------------------------------------------------------------------------
## Welcome to the Makefile docs
##
## Please see below for a list of commands available
## If you face any issues you can run the commands manually.
## --------------------------------------------------------------------------------------------------
EXEC_DOCKER=docker-compose run --rm django

help:  ## makefile documentation.
	@sed -ne '/@sed/!s/## //p' $(MAKEFILE_LIST)

run: ## run project
	python3 manage.py runserver 0.0.0.0:8000

run_d: ## run project
	docker-compose up

lint: ## lint & format
	pre-commit run --all-files

app: ## make a new app
	mkdir ./apps/$(a)
	django-admin startapp $(a) ./apps/$(a)

migrate: ## migrate
	python3 manage.py makemigrations
	python3 manage.py migrate

migrate_d: ## migrate
	$(EXEC_DOCKER) python3 manage.py makemigrations
	$(EXEC_DOCKER) python3 manage.py migrate

seed_db: ## seed db
	$(EXEC_DOCKER) python3 manage.py seed_db --verbosity=2

update_index: ## update_index
	$(EXEC_DOCKER) python3 manage.py update_index

clear_index: ## clear_index
	$(EXEC_DOCKER) python3 manage.py clear_index
