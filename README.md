<<<<<<< HEAD
# QEC Leaderboard

## Introduction

Threshold leaderboard of quantum error-correcting codes!

## Backend development

[![Build Status](https://travis-ci.org/errorcorrectionzoo/eczoo_thresholds.svg?branch=master)](https://travis-ci.org/errorcorrectionzoo/eczoo_thresholds)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

Thresholds Zoo. Check out the project's [documentation](http://errorcorrectionzoo.github.io/eczoo_thresholds/).

### Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  

### Local Development

Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```

## Frontend development

The frontend lives in the `client` folder.
```
cd client
```
Before you start, make sure the requirements have been installed.
```
npm install
```

To start the frontend, run the following
```
npm start
```
