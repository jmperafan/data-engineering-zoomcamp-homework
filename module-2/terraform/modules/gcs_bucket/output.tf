output "bucket_url" {
  description = "URL of the created GCS bucket"
  value       = google_storage_bucket.generic_bucket.url
}

output "bucket_name" {
  description = "Name of the created GCS bucket"
  value       = var.bucket_name
}