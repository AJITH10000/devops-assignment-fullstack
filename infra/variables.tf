variable "aws_region" {
  default = "ap-south-1"
}

variable "app_name" {
  default = "devops-app"
}

variable "backend_image" {
  description = "ECR image URI for backend"
}

variable "frontend_image" {
  description = "ECR image URI for frontend"
}
