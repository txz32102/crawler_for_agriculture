.PHONY: run kill

run:
	nohup sh -c 'cd backend && python3 manage.py runserver' > log1.txt 2>&1 &
	cd frontend && npm start

kill:
	-pkill -f 'python3 manage.py runserver'
	-pgrep -f 'npm start' | xargs kill -9
	python3 backend/crawler/delete.py