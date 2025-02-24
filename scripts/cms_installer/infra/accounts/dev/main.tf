terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"

  backend "s3" {
    bucket         = "sibel-tucana-e2e-cli-installer-dev"
    key            = "terraform/dev/e2e/cli/terraform.tfstate"
    region         = "us-east-2"
    dynamodb_table = "dev-cli-installer-e2e-lock"
  }
}

provider "aws" {
  region = "us-east-2"
  allowed_account_ids = [
    "104472814609"
  ]
  default_tags {
    tags = {
      env        = "dev"
      project    = "tucana"
      compliance = "hipaa"
      managed_by = "terraform"
    }
  }
}

module "cli_test_environment" {
  source = "../../modules/cli_test_environment"
  usage_identifier = "dev"
}