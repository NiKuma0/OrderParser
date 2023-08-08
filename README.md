# OrderParser

This app makes your csv file with deals into a database.


# How To Run it:

Clone this repo:
```sh
git clone https://github.com/NiKuma0/OrderParser.git
cd OrderParser
```
## Usual mode:
You can use this command if your **docker is v2** and you have sudo privileges:
```sh
make run-docker-compose
```
else/or you need more control:
```sh
make create-env
sudo docker-compose -f infra/docker-compose up
```

> **Warning**
> The `make run-docker-compose` and `make create-env` commands create an `.env` file.
> Do not use this file in production, modify it first as you need it.


## Editable mode:
1. Install dependencies by [`poetry`](https://python-poetry.org/docs/#installation):
    ```sh
    poetry install
    poetry shell
    ```
2. Run the database container, or use your own database (postgressql):
    ```sh
    make run-db
    ```
    or
    ```sh
    sudo docker-compose -f infra/docker-pg.yml up -d
    ```

3. Create the `.env` and change the `DB_HOST` variable to `localhost`, then run it:
    ```sh
    make create-env
    make run
    ```


# API reference:

## `POST /api/deals/`

### Body:

`deals` - `.csv` file of deals

### Returning:

201: The file has been sampled into the database.

## `GET /api/customer/`

### Returning:

200:
```
[
    {
        "username": "samplename",
        "spent_money": 100,
        "gems": [
            "gem1",
            "gem2"
        ]
    },
    {
        "username": "username",
        "spent_money": 123,
        "gems": [
            "gem1",
            "gem3"
        ]
    },
    ...
]
```
