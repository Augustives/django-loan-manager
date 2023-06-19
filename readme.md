# Django Loan Manager

## How to run:
    - Make sure you have docker installed and running.
    - Run `make up` or `make recreate` in the root folder of the project.

## Urls and User:
    - Django will be available on `localhost:8000`
    - Django admin user and password are "admin"
    - Front-end is available at `localhost:3000`
    - RabbitMq interface is available at `localhost:15672`
    - RabbitMq user and password are "guest"

## Creating a loan proposal:
To create a loan proposal you can either use the front-end or make a post request to `localhost:8000/loan-proposals/` with the following data schema:

```
{
    "value": <int>,
    "customer": {
        "name": <str>,
        "cpf": <str>,
        "address": {
            "country": <str>,
            "state": <str>,
            "city": <str>,
            "street": <str>,
            "postal_code": <str>,
            "additional_info": <optional> <str>
        }   
    }
}
```

*Country currently accepts only one option `BR`*