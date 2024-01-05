variable "version_number" {
  default = 3.0
}


resource "random_pet" "this" {
  keepers = {
    version = var.version_number
  }
}

resource "random_pet" "that" {
  keepers = {
    version = var.version_number
  }
}

variable "example_variable" {
  default = null
}
