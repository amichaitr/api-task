# api-task
Home assignment, REST API for querying a database (postgres)

Lunch instructions:

1. download and extract the project.

2. open terminal in the project directory ("restApi_pgDB").

3. exec: docker-compose up
   # from the "docker-compose.yml", build the images as "amichaitr/restapi-pg-db" and "amichaitr/postgres" then "run the containers as "api" and "pg_db"
   
   # in the "amichaitr/postgres" Dockerfile, i use the environment variables of the official image of postgres, to define the username password and database for the application.
   # When the application starts, it creates the "persons" table according to the schema.
   
4. to insert a new name to the table, use:
curl -d '{"name":"<person-name>", "age":"<person-age>"}' -H "Content-Type: application/json" -X POST http://0.0.0.0:5000/api/v1/persons
  
5. to query the database for all names that are of certain age, use:
curl  http://0.0.0.0:5000/api/v1/persons/age=<x>
  
6. to shutdown the application use:
curl  http://0.0.0.0:5000/shutdown

7. to close the database use:
docker stop pg_db
  


