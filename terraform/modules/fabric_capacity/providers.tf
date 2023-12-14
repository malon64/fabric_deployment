terraform {
  required_providers {
    azapi = {
      source  = "azure/azapi"
      version = "=0.1.0"
    }
  }
}

provider "azapi" {
  default_location = "francecentral"
  default_tags = {
    team = "Azure deployments"
  }
}