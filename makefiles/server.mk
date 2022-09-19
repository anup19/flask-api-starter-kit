### SERVER
# ¯¯¯¯¯¯¯¯¯¯¯

server.install: ## Install server with its dependencies
	docker build -t postgres_db -f Dockerfile_db . && docker-compose run --rm server pip install -r requirements-dev.txt --user --upgrade --no-warn-script-location

server.start: ## Start server in its docker container
	docker-compose up server

server.bash: ## Connect to server to lauch commands
	docker-compose exec server bash

server.daemon: ## Start daemon server in its docker container
	docker-compose up -d server

server.stop: ## Start server in its docker container
	docker-compose stop

server.clean:
	docker stop flask-api-starter-kit_server_1 flask-api-starter-kit_db_1 flask-api-starter-kit_dbdata_1 && \
	docker rm flask-api-starter-kit_server_1 flask-api-starter-kit_db_1 flask-api-starter-kit_dbdata_1 && \
	docker volume prune -f

server.logs: ## Display server logs
	tail -f server.log

server.upgrade: ## Upgrade pip dependencies
	docker-compose run --rm server bash -c "python vendor/bin/pip-upgrade requirements.txt requirements-dev.txt --skip-virtualenv-check"
