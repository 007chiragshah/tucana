variable "aws_vpc_cidr_block" {
  description = "CIDR Blocks for AWS VPC"
}

variable "aws_cluster_name" {
  description = "Name of Cluster"
}

variable "aws_avail_zones" {
  description = "AWS Availability Zones Used"
  type        = list(string)
}

variable "aws_cidr_subnets_private" {
  description = "CIDR Blocks for private subnets in Availability zones"
  type        = list(string)
}

variable "aws_cidr_subnets_public" {
  description = "CIDR Blocks for public subnets in Availability zones"
  type        = list(string)
}

variable "allow_ssh_connections_cidr" {
  description = "CIDR Blocks for public subnets in Availability zones"
  type        = list(string)
  default     = ["0.0.0.0/0"]
}

variable "encryption_key_arn" {
  description = "AWS encryption key arn"
}