output "dataset_id" {
  description = "ID of the created BigQuery dataset"
  value       = google_bigquery_dataset.generic_dataset.dataset_id
}

output "dataset_name" {
  description = "Name of the created BigQuery dataset"
  value       = var.dataset_name
}