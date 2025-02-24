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

# Create the S3 bucket for Terraform state
resource "aws_s3_bucket" "tf_state_bucket" {
  bucket = "sibel-tucana-e2e-cli-installer-dev"

  tags = {
    Name        = "sibel-tucana-e2e-cli-installer-dev"
    Environment = "dev"
  }
}

resource "aws_s3_bucket_ownership_controls" "tf_state_bucket_oc" {
  bucket = aws_s3_bucket.tf_state_bucket.id
  rule {
    object_ownership = "BucketOwnerPreferred"
  }
}

resource "aws_s3_bucket_acl" "tf_state_bucket_acl" {
  depends_on = [aws_s3_bucket_ownership_controls.tf_state_bucket_oc]

  bucket = aws_s3_bucket.tf_state_bucket.id
  acl    = "private"
}

resource "aws_s3_bucket_versioning" "tf_state_bucket_versioning" {
  bucket = aws_s3_bucket.tf_state_bucket.id
  versioning_configuration {
    status = "Enabled"
  }
}

# Create DynamoDB table for state locking
resource "aws_dynamodb_table" "tf_state_lock" {
  name         = "dev-cli-installer-e2e-lock"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"

  attribute {
    name = "LockID"
    type = "S" # String
  }

  tags = {
    Name        = "dev-cli-installer-e2e-lock"
    Environment = "dev"
  }
}

output "s3_bucket_name" {
  value = aws_s3_bucket.tf_state_bucket.id
}

output "dynamodb_table_name" {
  value = aws_dynamodb_table.tf_state_lock.name
}