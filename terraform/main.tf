locals {
  resource_group = {
    name = "rg-fabric101"
  }
  yaml_capacity= yamldecode(file("${path.root}/../capacity_config.yml")).capacity
}

data "local_file" "yaml_capacity" {
  filename = "${path.root}/../capacity_config.yml"
}

resource "azurerm_resource_group" "qs101" {
  name     = local.resource_group.name
  location = var.location
}

module "fabric_capacity" {
  source = "./modules/fabric_capacity"
  basename = local.yaml_capacity.basename
  resource_group_id = azurerm_resource_group.qs101.id
  location = var.location
  sku = local.yaml_capacity.sku
  admin_email = local.yaml_capacity.admin_email
  module_enabled = true
  tags = local.yaml_capacity.tags

}