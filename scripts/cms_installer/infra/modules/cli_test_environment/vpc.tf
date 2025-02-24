# Create a VPC
resource "aws_vpc" "cli_e2e_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags = {
    Name = "${var.usage_identifier}_cli_e2e_vpc"
  }
}

# Create a public subnet
resource "aws_subnet" "public_subnet" {
  vpc_id                  = aws_vpc.cli_e2e_vpc.id
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = true
  availability_zone       = "us-east-2a"
  tags = {
    Name = "${var.usage_identifier}_cli_e2e_subnet_public"
  }
}

# Internet Gateway for the VPC
resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.cli_e2e_vpc.id

  tags = {
    Name = "${var.usage_identifier}_cli_e2e_ig"
  }
}

# Route Table for the public subnet
resource "aws_route_table" "public_rt" {
  vpc_id = aws_vpc.cli_e2e_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }

  tags = {
    Name = "${var.usage_identifier}_cli_e2e_public_rt"
  }
}

# Associate Route Table with Subnet
resource "aws_route_table_association" "public_rt_assoc" {
  subnet_id      = aws_subnet.public_subnet.id
  route_table_id = aws_route_table.public_rt.id
}



# Security Group for SSH access
resource "aws_security_group" "ssh_access" {
  vpc_id = aws_vpc.cli_e2e_vpc.id

# Ingress rules (Allow incoming traffic)
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "Allow SSH"
  }

  ingress {
    from_port   = 6443
    to_port     = 6443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "Allow API Server"
  }

  ingress {
    from_port   = 2379
    to_port     = 2379
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "Allow ETCD"
  }

  ingress {
    from_port   = 9345
    to_port     = 9345
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "Allow rke2"
  }

  ingress {
    from_port   = 6444
    to_port     = 6444
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "Allow rke2 connection"
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "Allow HTTP"
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "Allow HTTPS"
  }

  ingress {
    from_port = 0
    to_port = 0
    protocol = "icmp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "Allow ICMP"
  }
  # Egress rules (Allow all outgoing traffic)
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1" # All protocols
    cidr_blocks = ["0.0.0.0/0"]
    description = "Allow all outbound traffic"
  }

  tags = {
    Name = "${var.usage_identifier}_cli_e2e_ssh_http_https_access_rule"
  }
}