start:
	docker-compose build --no-cache
	docker-compose up -d
stop:
	docker-compose down
	docker rmi sabiafrica-client
	docker rmi sabiafrica-server
restart:
	docker-compose down
	docker rmi sabiafrica-client
	docker rmi sabiafrica-server
	docker-compose build --no-cache
	docker-compose up -d