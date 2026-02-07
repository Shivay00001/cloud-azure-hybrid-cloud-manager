from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
import os

class AzureVMManager:
    def __init__(self, subscription_id: str):
        self.credential = DefaultAzureCredential()
        self.compute_client = ComputeManagementClient(self.credential, subscription_id)

    def list_vms(self, resource_group: str):
        """Lists all VMs in a resource group."""
        vms = self.compute_client.virtual_machines.list(resource_group)
        return [
            {
                "name": vm.name,
                "location": vm.location,
                "size": vm.hardware_profile.vm_size if vm.hardware_profile else "Unknown",
                "provisioning_state": vm.provisioning_state
            }
            for vm in vms
        ]

    def start_vm(self, resource_group: str, vm_name: str):
        """Starts a specific VM."""
        async_action = self.compute_client.virtual_machines.begin_start(resource_group, vm_name)
        return async_action.result()

    def stop_vm(self, resource_group: str, vm_name: str):
        """Stops (deallocates) a specific VM."""
        async_action = self.compute_client.virtual_machines.begin_deallocate(resource_group, vm_name)
        return async_action.result()
