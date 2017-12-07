# Flask Boiler Plate

## Getting started

* Clone repo
* Create and initialize a virtualenv with python3
* Install requirements from requirements.txt
* Initialize a postgres database with setup/init_db.sql
* If you wish to use sentry use os variables: `export SENTRY_DSN=<your_dsn>`
* To start a dev server run `gunicorn -c gunicorn_config.py run:app`