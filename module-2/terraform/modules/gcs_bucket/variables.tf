variable "bucket_name" {
  description = "Name of the GCS bucket"
}

variable "location" {
  description = "Location of the bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}