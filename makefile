install:
	pip install \
		--upgrade \
		-r requirements.txt

rebuild:
	docker-compose build \
		--force-rm \
		--no-cache

restart:
	docker-compose restart app && make logs

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs --tail 100 -f app
