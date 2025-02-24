# EC2 Instances
resource "aws_instance" "ingress_node" {
  ami                         = "ami-0b61425d47a44fc5f" # Ubuntu Server 22.04 LTS (64b x86)
  instance_type               = "t2.xlarge"
  subnet_id                   = aws_subnet.public_subnet.id
  security_groups             = [aws_security_group.ssh_access.id]
  associate_public_ip_address = true

  root_block_device {
    volume_size = 200
    volume_type = "gp3"
  }

  key_name = "ci-cd-test-cli-installer"
  tags = {
    Name = "${var.usage_identifier}_cli_e2e_ingress_node"
  }
}

resource "aws_instance" "control_plane_node" {
  ami                         = "ami-0b61425d47a44fc5f" # Ubuntu Server 22.04 LTS (64b x86)
  instance_type               = "t2.xlarge"
  subnet_id                   = aws_subnet.public_subnet.id
  vpc_security_group_ids      = [aws_security_group.ssh_access.id]
  associate_public_ip_address = true
  key_name                    = "ci-cd-test-cli-installer"

  root_block_device {
    volume_size = 200
    volume_type = "gp3"
  }

  tags = {
    Name = "${var.usage_identifier}_cli_e2e_control_plane_node"
  }
}

resource "aws_instance" "worker_node_1" {
  ami                         = "ami-0b61425d47a44fc5f" # Ubuntu Server 22.04 LTS (64b x86)
  instance_type               = "t2.xlarge"
  subnet_id                   = aws_subnet.public_subnet.id
  vpc_security_group_ids      = [aws_security_group.ssh_access.id]
  associate_public_ip_address = true
  key_name                    = "ci-cd-test-cli-installer"


  root_block_device {
    volume_size = 200
    volume_type = "gp3"
  }

  tags = {
    Name = "${var.usage_identifier}_cli_e2e_worker_node_1"
  }
}

resource "aws_instance" "worker_node_2" {
  ami                         = "ami-0b61425d47a44fc5f" # Ubuntu Server 22.04 LTS (64b x86)
  instance_type               = "t2.xlarge"
  subnet_id                   = aws_subnet.public_subnet.id
  vpc_security_group_ids      = [aws_security_group.ssh_access.id]
  associate_public_ip_address = true
  key_name                    = "ci-cd-test-cli-installer"

  root_block_device {
    volume_size = 200
    volume_type = "gp3"
  }

  tags = {
    Name = "${var.usage_identifier}_cli_e2e_worker_node_2"
  }
}

resource "aws_instance" "worker_node_3" {
  ami                         = "ami-0b61425d47a44fc5f" # Ubuntu Server 22.04 LTS (64b x86)
  instance_type               = "t2.xlarge"
  subnet_id                   = aws_subnet.public_subnet.id
  vpc_security_group_ids      = [aws_security_group.ssh_access.id]
  associate_public_ip_address = true
  key_name                    = "ci-cd-test-cli-installer"

  root_block_device {
    volume_size = 200
    volume_type = "gp3"
  }

  tags = {
    Name = "${var.usage_identifier}_cli_e2e_worker_node_3"
  }
}

