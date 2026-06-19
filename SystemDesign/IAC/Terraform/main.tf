terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

variable "stack_name" {
  type        = string
  default     = "my-stack"
  description = "Equivalent to AWS::StackName in CloudFormation"
}

variable "latest_ami_id_parameter" {
  type        = string
  default     = "/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2"
  description = "Fetches the latest Amazon Linux 2 AMI ID from Systems Manager"
}

data "aws_caller_identity" "current" {}

data "aws_ssm_parameter" "latest_ami_id" {
  name = var.latest_ami_id_parameter
}

resource "aws_s3_bucket" "my_s3_bucket" {
  bucket = "${var.stack_name}-basic-bucket-${data.aws_caller_identity.current.account_id}"
}

resource "aws_security_group" "instance_security_group" {
  name        = "${var.stack_name}-sg"
  description = "Enable HTTP/HTTPS and SSH ingress, allow all egress"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "my_ec2_instance" {
  ami                    = data.aws_ssm_parameter.latest_ami_id.value
  instance_type          = "t2.micro"
  vpc_security_group_ids = [aws_security_group.instance_security_group.id]

  tags = {
    Name = "${var.stack_name}-Instance"
  }
}

output "bucket_name" {
  description = "The name of the created S3 bucket"
  value       = aws_s3_bucket.my_s3_bucket.bucket
}

output "bucket_arn" {
  description = "The ARN of the newly created S3 bucket"
  value       = aws_s3_bucket.my_s3_bucket.arn
}

output "instance_id" {
  description = "The Instance ID of the newly created EC2 instance"
  value       = aws_instance.my_ec2_instance.id
}

output "instance_public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.my_ec2_instance.public_ip
}


# Deploy commands
# terraform init
# terraform plan
# terraform apply
# terraform destroy