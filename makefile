make: up

install:
	pip3 install \
		--upgrade \
		-r requirements.txt

rebuild:
	docker-compose \
		--project-name ff-cluster \
		--file ./shared.docker-compose.yml \
		build \
			--force-rm \
			--no-cache

up:
	docker-compose \
		--project-name ff-cluster \
		--file ./shared.docker-compose.yml \
		--log-level ERROR \
		up -d \
		&& make logs

down:
	docker-compose \
		--project-name ff-cluster \
		--file ./shared.docker-compose.yml \
		--log-level ERROR \
		down

logs:
	docker-compose \
		--project-name ff-cluster \
		--file ./shared.docker-compose.yml \
		--log-level ERROR \
		logs --tail 100 -f app-fastapi

restart:
	docker-compose \
		--project-name ff-cluster \
		--file ./shared.docker-compose.yml \
		--log-level ERROR \
		restart app-fastapi \
	&& make logs

ps:
	docker-compose \
		--project-name ff-cluster \
		--file ./shared.docker-compose.yml \
		ps
