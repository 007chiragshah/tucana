# CMS Installer CLIP App

# Development 

## Installation

Run `poetry install`

## Execution

Run `./run.sh`


## Compilation

Run `./compile.sh`


# How to pull the installer image locally

* [Setup AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html#cli-configure-sso-configure) for prod env, make sure to name the profile `tucana-prod` 

* Enable profile for current shell

```shell
export AWS_PROFILE=tucana-prod
```

* Login using sso

```shell
aws sso login --profile tucana-prod
```

* Login to docker

```shell
aws ecr get-login-password | docker login --username AWS --password-stdin 620908046246.dkr.ecr.us-east-2.amazonaws.com
```

* Pull the installer image

```shell
docker pull 620908046246.dkr.ecr.us-east-2.amazonaws.com/install:{desired_tag}
```

* Convert to tar

```shell
docker save 620908046246.dkr.ecr.us-east-2.amazonaws.com/install > install.tar
```

# How to run infra

## Prerequisites

* Terraform
* AWS CLI
* tucana-dev profile configured using aws configure sso
  * Starting URL: https://d-9a6778a1d9.awsapps.com/start/#
  * Region: us-east-2
  * Format: json
  * SessionName: tucana-dev

## Login to AWS Tucana dev account

```shell
aws sso login --profile tucana-dev
```

## Creating Infra

__Take into account all devs will be using same VMs so potentially you could overlap.__

```shell
export AWS_PROFILE=tucana-dev # won't run against other env, make sure to setup you sso use
cd infra/dev
terraform apply
```

## Deleting infra

```shell
terraform destroy
```

# Shortcut Mode

When developing, it might be useful to run in shortcut mode. Shortcut runs a different CLI which goes directly to the installation with some hardcoded values. Do not use this for testing or approving a final version. It's only for development purposes so we don't have to type all params every time.

## Creating .env file for shortcut script

```shell
./create_env.sh
```

## Running Shortcut

```shell
./run_shortcut.py
```

