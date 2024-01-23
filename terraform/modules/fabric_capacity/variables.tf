
variable "basename" {
  type        = string
  description = "Basename of the module."
  validation {
    condition     = can(regex("^[-0-9a-zA-Z]{1,21}$", var.basename)) && can(regex("[0-9a-zA-Z]+$", var.basename))
    error_message = "The name must be between 1 and 21 characters, can contain only letters, numbers, and hyphens. Must end with a letter or number. Cannot contain consecutive hyphens."
  }
}

variable "resource_group_id" {
  type        = string
  description = "Resource group id."
}

variable "location" {
  type        = string
  description = "Location of the resource group."
}

variable "tags" {
  type        = map(string)
  default     = {}
  description = "A mapping of tags which should be assigned to the deployed resource."
}

variable "module_enabled" {
  type        = bool
  description = "Variable to enable or disable the module."
  default     = true
}

/*
SKU   Capacity Units    COST (ESTIMATED/MONTH)
F2          2               $292.00
F4          4               $584.00
F8          8               $1,168.00
F16         16              $2,336.00
F32         32              $4,672.00
F64         64              $9,344.00
F128        128             $18,688.00
F256        256             $37,376.00
F512        512             $74,752.00
F1024       1024            $149,504.00
F2048       2048            $299,008.00
*/
variable "sku" {
  type        = string
  default     = "F2"
  description = "Capacity type of pricing exists between F2 and F2048"
  validation {
    condition = can(regex("F+[0-9]{1,4}$", var.sku))
    error_message = "Capacity SKU must be one of these : F2 F4 F8 F16 F32 F64 F128 F256 F512 F1024 F2048"
  }
}


variable "admin_email" {
    type = string
    description = "Email of the capacity administrator "
    validation {
      condition = can(regex("^[\\w-\\.]+@([\\w-]+\\.)+[\\w-]{2,4}$", var.admin_email))
      error_message = "Value must be a well formated email : test@domain.com"
    }
  
}