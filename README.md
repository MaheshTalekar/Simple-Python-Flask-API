# Simple-Python-Flask-API
Implementation of Python flask API using sqlite database to perform GET and POST operations.

First go through Database.txt and Requirement.txt files to create Database, Virtual environment and install Libraries required to execute .py file.

Run the python file using the command: python Task.py

Following are the curl requests to perform GET and POST operations:

GET request to fetch data of all cars: curl http://localhost:5000/car

GET request to fetch data for particular car id: curl http://localhost:5000/car/3

POST request to add new entry to the database: curl -d '{"make":"Audi", "model":"Q7", "year":"2006", "chassis_id":"12345Q", "car_id":"7", "last_updated":"", "price":"800"}' -H "Content-Type: application/json" -X POST http://localhost:5000/car
