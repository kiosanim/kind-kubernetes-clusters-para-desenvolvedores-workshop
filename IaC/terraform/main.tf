# Autor: Fábio Sartori
# Copyright: 20220524

terraform {
  required_providers {
    linode = {
      source = "linode/linode"
      version = "1.26.1"
    }
  }
}

provider "linode" {
    token = var.shared_token
}

resource "linode_instance" "ubuntukind" {
    label = var.ubuntu_label
    image = var.ubuntu_image
    type = var.ubuntu_type
    region = var.shared_region
    root_pass = var.shared_root_pass
    authorized_keys = var.authorized_keys
    private_ip = var.shared_private_ip
    tags = var.ubuntu_tags
}

variable "shared_token" {}
    variable "region" {
    default = "us-central"
}
variable "shared_root_pass" {}
variable "shared_private_ip" {}
variable "shared_region" {}
variable "authorized_keys" {}
variable "ubuntu_tags" {}
variable "ubuntu_label" {}
variable "ubuntu_image" {}
variable "ubuntu_type" {}
