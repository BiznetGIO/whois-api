# Whois API

[![Build Status](https://travis-ci.org/BiznetGIO/whois-api.svg?branch=master)](https://travis-ci.org/BiznetGIO/whois-api)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

whois-api is an API service for whois lookup.

## Quickstart

Build the docker image:

``` bash
$ docker build -t whois-api:0.0.1 .
```

Run the image using `docker-compose`:

``` bash
$ docker-compose up
```

Now you can use the api:

```bash
$ curl -X POST http://localhost:5000/api/whois/ \
    -H "Content-Type: text/plain" \
    -H 'X-Whois-key: fakekey123' \
    -d "google.com"
```
