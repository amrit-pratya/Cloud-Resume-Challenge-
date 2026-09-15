output "s3_bucket_name" {
  value = aws_s3_bucket.resume.id
}

output "cloudfront_domain_name" {
  value = aws_cloudfront_distribution.cdn.domain_name
}

output "cloudfront_distribution_id" {
  value = aws_cloudfront_distribution.cdn.id
}

output "api_endpoint" {
  value = "${aws_apigatewayv2_api.http_api.api_endpoint}/visitors"
}

output "github_actions_role_arn" {
  value = aws_iam_role.github_actions.arn
}