# api-task
REST API for querying a database (postgres)

Lunch instructions:

1. Download and extract the project.

2. Open terminal in the project directory ("restApi_pgDB").

3. exec: docker-compose up.

   From the "docker-compose.yml", it builds the images as "amichaitr/restapi-pg-db" and "amichaitr/postgres" then it's running the containers as "api" and "pg_db".
   
   In the "amichaitr/postgres" Dockerfile, i use the environment variables of the official image of postgres, to define the username password and database for the application.
   
   When the application starts, it creates the "persons" table according to the schema.
   
4. To insert a new name to the table, use:
curl -d '{"name":"\<person-name\>", "age":"\<person-age\>"}' -H "Content-Type: application/json" -X POST http://0.0.0.0:5000/api/v1/persons
  
  The respons to that request is a json object contain the new person that added to the table.
  
5. To query the database for all names that are of certain age, use:
curl  http://0.0.0.0:5000/api/v1/persons/age=<x\>
  
6. To shutdown the application use:
curl  http://0.0.0.0:5000/shutdown

7. To close the database use:
docker stop pg_db
  


