variable "location" {
  type        = string
  description = "Location of the resource group. Lower case of the the Azure location"
  validation {
    condition = can(regex("[a-z]$", var.location))
    error_message = "Location must be in lower case and named after a real Azure Location, ex: francecentral"
  }
}