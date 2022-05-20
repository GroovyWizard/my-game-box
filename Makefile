migrate:
	docker exec my-game-box-web-1 bash -c "python manage.py makemigrations && python manage.py migrate" 
