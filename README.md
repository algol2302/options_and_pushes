# options-and-pushes

## Start
* Just pull and run `docker-compose up --build`

## Endpoints
* http://localhost:8000/ - the home page of the app
* http://localhost:8000/admin - usual django admin to rule users

## Design

* The app based on usual django forms and views. 
* There aren't any DRF endpoints.
* It's used https://django-adminlte2.readthedocs.io/en/latest/
* For preview is's used jquery
* prod envs is here for example (and of course, it's not safe for the real prod app)
* docker-compose.override.yml - for local development, but in this case should to install poetry
* nginx is used for to proxy gunicorn and to provide static files

## TODO
* [ ]  fit with the design (a lot of details)
* [ ]  add supervisor (I've never used it)
* [ ]  add tests
* [ ]  deploy to an public server (add to ALLOWED_HOSTS ip or an subdomain)
* [ ]  test on the public server 
 