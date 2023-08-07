start:
	docker-compose build --no-cache
	docker-compose up -d
stop:
	docker-compose down
	docker rmi you_tube_analysis-front
	docker rmi you_tube_analysis-back
restart:
	docker-compose down
	docker rmi you_tube_analysis-front
	docker rmi you_tube_analysis-back
	docker-compose build --no-cache
	docker-compose up -d