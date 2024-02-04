resource "google_bigquery_dataset" "generic_dataset" {
  dataset_id                  = var.dataset_name
  location                    = var.location
  default_table_expiration_ms = "3600000" # Optional: Set the default table expiration time in milliseconds
}
