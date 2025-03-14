# Config

Config microservice

# 📔 Documentation

Open your browser at http://127.0.0.1:7005/config/docs (or equivalent, using your Docker host), you will see an automatic, interactive, API documentation.

There is an alternative API documentation (using ReDoc), which you can access at http://127.0.0.1:7005/config/redoc (or equivalent, using your Docker host).

# 💻 Running locally

## Installation

To install the project locally, the easiest way is to run the build script located in the project root directory
(Please check the script prerequisites in the next section if this is your first time running the project).

The build script takes care of installing all the project dependencies, running tests, performing code validation,
and running linters. Once the script finishes executing, we can start the server using uvicorn.

```shell
./build.sh
poetry run uvicorn app.main:app --port 7005 --reload
```

_**Note**: Please note that the build script generates a `.env` file in the root folder, which contains the necessary environment
variables for running the project. While these variables have default values set, some of them may need to be updated to
reflect your local environment. Therefore, it is recommended that you check the `.env` file and modify the relevant
variables as needed before running the project._

# ⚙️ Requirements for running locally

## Python

If Python is not installed I recommend installing manually from Python's [website](https://www.python.org/downloads/).
Check `pyproject.toml` for exact Python version.

## Creating a PostgresSQL Container

If you don't have it already, you can create a PostgresSQL database server using the following docker command.
Keep in mind that the password is only for local environment and will be reused in all services.

```shell
docker run --name postgres-sibel --network tucana -e POSTGRES_PASSWORD=cantguessthis -p 5432:5432 -d postgres:latest
```

## Install Poetry

You can follow the steps at Poetry's [doc](https://python-poetry.org/docs/), or install by using:

```shell
curl -sSL https://install.python-poetry.org | python3 -
```

# 🧰 Scripts

The scripts assume the [project requirements](#requirements-for-running-locally) are installed and running.

We have a main build script which will:

- Install dependencies
- Format code
- Run feature tests
- Run unit test

There are also a couple of scripts for formatting the code with black and running feature tests independently.

# 📇 Database Migrations

To use alembic we provide a few helping scripts:

- scripts/alembic/create-migrations.sh - Creates a new migrations script (need to provide a message as arg)
- scripts/alembic/migrate.sh - Applies all migrations up to head
- scripts/alembic/rollback.sh - Downgrades one migration

# 🐳 Docker

While locally you probably don't need to run the service as a container, there are a few scripts to help

- scripts/docker/login.sh - Login into the ECR registry
- scripts/docker/build-image.sh - Builds the docker image
- scripts/docker/exec.sh - Execs into the containers
- scripts/docker/rm.sh - Deletes the container
- scripts/docker/run.sh - Runs the container
- scripts/docker/start.sh - Starts the container
- scripts/docker/stop.sh - Stops the container

# Kafka

In order to run Kafka publisher and its topic locally, these scripts will help

- scripts/kafka/start-broker.sh
- scripts/kafka/create-topic.sh
