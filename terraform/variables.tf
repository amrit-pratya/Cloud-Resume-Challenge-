variable "aws_region" {
  default = "us-east-1"
}

variable "project_name" {
  default = "cloud-resume"
}

variable "github_repo" {
  description = "Format: github_username/repo_name"
  type        = string
}