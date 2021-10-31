run-test:
	locust --users 5 --spawn-rate 1 -H "http://localhost:8000" -f locust.py
