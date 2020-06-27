# options-and-pushes

## Start
* Just pull and run `docker-compose up --build`

## Endpoints
* http://18.157.253.138/ - the home page of the app (only for logged in users)
* http://18.157.253.138/admin - usual django admin to rule users

![login view](https://github.com/algol2302/options_and_pushes/blob/master/image0.png)
![pushes view](https://github.com/algol2302/options_and_pushes/blob/master/image1.png)
![options view](https://github.com/algol2302/options_and_pushes/blob/master/image2.png)


## Design

* The app based on usual old school django forms and views. 
* There aren't any DRF endpoints. I guess it wasn't required.
* It's used https://django-adminlte2.readthedocs.io/en/latest/.
* For a preview is used `jquery`.
* Prod envs is here for example (and of course, it's not safe for the real prod app).
* The app runs just on `docker-compose -f docker-compose.yml up -d`.
* `docker-compose.override.yml` - for local development, in this case should to install poetry.
* `nginx` is used for to proxy gunicorn and to provide static files.
* `poetry` is used for a control of dependencies.
* The vps on aws lightsail.

## TODO
* [ ]  fit with the design (a lot of details)
* [ ]  add supervisor (I've never used it)
* [ ]  add tests
* [ ]  fit templates with DRY 
* [X]  deploy to an public server (add to ALLOWED_HOSTS ip or an subdomain)
* [X]  test on the public server 
 
