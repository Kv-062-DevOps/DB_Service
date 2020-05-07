variable "region" {}
provider "aws" {
  region = var.region
}
resource "aws_dynamodb_table" "employee" {
  name           = "Employees"
  billing_mode   = "PROVISIONED"
  read_capacity  = 10
  write_capacity = 10
  hash_key       = "types"
  range_key      = "emp_id"

  attribute {
    name = "types"
    type = "S"
  }

  attribute {
    name = "emp_id"
    type = "S"
  }
  tags = {
    Name        = "dynamodb-table-1"
    Environment = "production"
  }
}
resource "aws_dynamodb_table_item" "employee" {
  table_name = "aws_dynamodb_table.employee.name"
  hash_key   = "aws_dynamodb_table.employee.hash_key"
  range_key  = "aws_dynamodb_table.employee.range_key"
  item       = <<ITEMS
{
  "types": {"S": "manager"},
  "emp_id": {"S": "1"},
  "first_name": {"S": "Yurii"},
  "second_name": {"S": "Liaskovets"},
  "default_salary": {"S": "2000"},
  "experience": {"S": "1"}
}
ITEMS
}
