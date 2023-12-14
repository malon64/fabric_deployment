output "resource_group_id" {
    value = azurerm_resource_group.qs101.id
    description = "Id of the main resource group"
}

output "capacity_id" {
  value = module.fabric_capacity.id
  description = "Resource identifier of the instance of Fabric Capacity."
}

output "capacity_name" {
  value = module.fabric_capacity.name
  description = "Capacity entire name"
}