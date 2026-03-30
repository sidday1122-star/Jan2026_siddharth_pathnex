provider "aws" {
  region = "ap-south-1"
}

resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0" # example AMI
  instance_type = "t2.micro"

  tags = {
    Name = "Day3-Terraform-Instance"
  }
}
