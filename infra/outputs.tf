output "vpc_id" {
  value = aws_vpc.main.id
}

output "public_subnet_ids" {
  value = aws_subnet.public[*].id
}

output "alb_dns_name" {
  value = aws_lb.app_lb.dns_name
}
