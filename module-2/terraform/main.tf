terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.6.0"
    }
  }
}

provider "google" {
  credentials = file(var.credentials)
  project     = var.project
  region      = var.region
}

module "gcs_bucket" {
  source      = "./modules/gcs_bucket"
  bucket_name = "green_taxi_ny"
  location    = var.location
}

module "bg_dataset" {
  source       = "./modules/bigquery_dataset"
  dataset_name = "green_taxi_ny"
  location    = var.location
}
