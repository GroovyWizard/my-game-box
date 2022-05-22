migrate:
	docker exec my-game-box-web-1 bash -c "python manage.py makemigrations && python manage.py migrate" 


pip:
	docker exec my-game-box-web-1 bash -c "pip install -r requirements.txt" 
