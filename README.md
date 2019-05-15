# real-world-drf

[![Build Status](https://travis-ci.org/cavadev/real-world-drf.svg?branch=master)](https://travis-ci.org/cavadev/real-world-drf)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

Example of real world project that use django rest framework.

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  
- [Travis CLI](http://blog.travis-ci.com/2013-01-14-new-client/)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

# Local Development

Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```

# Continuous Deployment

Deployment is automated via Travis. When builds pass on the master or qa branch, Travis will deploy that branch to Heroku. Follow these steps to enable this feature.

Initialize the production server:

```
heroku create real-world-drf-prod --remote prod && \
    heroku addons:create newrelic:wayne --app real-world-drf-prod && \
    heroku addons:create heroku-postgresql:hobby-dev --app real-world-drf-prod && \
    heroku config:set DJANGO_SECRET_KEY=`openssl rand -base64 32` \
        DJANGO_AWS_ACCESS_KEY_ID="Add your id" \
        DJANGO_AWS_SECRET_ACCESS_KEY="Add your key" \
        DJANGO_AWS_STORAGE_BUCKET_NAME="real-world-drf-prod" \
        DJANGO_CONFIGURATION="Production" \
        DJANGO_SETTINGS_MODULE="backend.config" \
        --app real-world-drf-prod
```

You can see the result in [https://real-world-drf-prod.herokuapp.com](https://real-world-drf-prod.herokuapp.com)

Initialize the qa server:

```
heroku create real-world-drf-qa --remote qa && \
    heroku addons:create newrelic:wayne --app real-world-drf-qa && \
    heroku addons:create heroku-postgresql:hobby-dev --app real-world-drf-qa && \
    heroku config:set DJANGO_SECRET_KEY=`openssl rand -base64 32` \
        DJANGO_AWS_ACCESS_KEY_ID="Add your id" \
        DJANGO_AWS_SECRET_ACCESS_KEY="Add your key" \
        DJANGO_AWS_STORAGE_BUCKET_NAME="real-world-drf-qa" \
        DJANGO_CONFIGURATION="Production" \
        DJANGO_SETTINGS_MODULE="backend.config" \
        --app real-world-drf-qa
```

You can see the result in [https://real-world-drf-qa.herokuapp.com](https://real-world-drf-qa.herokuapp.com)

Securely add your Heroku credentials to Travis so that it can automatically deploy your changes (You can also edit project settings in the travis website for add a new environment variable):

```bash
travis encrypt HEROKU_API_KEY="add you heroku api key here" --add
```

Commit your changes and push to master and qa to trigger your first deploys:

```bash
git commit -a -m "ci(travis): first deploy" && \
git push origin master:qa && \
git push origin master
```

You're now ready to continuously ship! ✨ 🛳
