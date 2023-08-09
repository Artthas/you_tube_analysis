start:
	docker-compose build --no-cache
	docker-compose up -d
stop:
	docker-compose down
	docker rmi you_tube_analysis_front
	docker rmi you_tube_analysis_back
restart:
	docker-compose down
	docker rmi you_tube_analysis_front
	docker rmi you_tube_analysis_back
	docker-compose build --no-cache
	docker-compose up -d