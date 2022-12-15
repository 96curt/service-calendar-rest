# Service Calendar REST API
Capstone Project at California State University, Chico sponsored by Sierra Pacific Windows

This is the backend section of my project. The frontend is located at https://github.com/96curt/service-calendar-web

Live API is at https://api.curtishohman.info

## Technologies
- Django Web Framework - A effortless development platform.
- Django Rest Framework - toolkit to develop a REST API with Django.
- drf-spectacular - OpenAPI 3.0 schema Documentation with Swagger UI.
- Docker - Development and Deployment application containers. 
- Gunicorn - Python WSGI application server.
- Nginx - HTTP and reverse proxy server, used to host static files.


## Development Setup with Docker
1. $ docker-compose up
3. $ docker-compose exec web python manage.py migrate
4. $ docker-compose exec web python manage.py createsuperuser
5. Open browser to localhost:8888

## Production Setup with Docker *not working
1. modify envroment varibles in prod/.env
2. $ docker-compose up -d db     (wait for db to start)
3. $ docker-compose up -d gunicorn
4. $ docker-compose up -d nginx
5. $ docker-compose exec web python manage.py createsuperuser
6. Open browser to localhost:8082
