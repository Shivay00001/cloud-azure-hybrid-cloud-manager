import argparse
import os
from dotenv import load_dotenv
from src.azure_ops.vm_manager import AzureVMManager

load_dotenv()

def main():
    parser = argparse.ArgumentParser(description="Azure Hybrid Cloud Manager")
    parser.add_argument("action", choices=["list-vms", "start-vm", "stop-vm"], help="Action to perform")
    parser.add_argument("--resource-group", required=True, help="Azure Resource Group")
    parser.add_argument("--vm-name", help="VM Name (required for start/stop)")
    parser.add_argument("--subscription-id", default=os.getenv("AZURE_SUBSCRIPTION_ID"), help="Azure Subscription ID")

    args = parser.parse_args()

    if not args.subscription_id:
        print("Error: Subscription ID must be provided via argument or AZURE_SUBSCRIPTION_ID env var.")
        return

    manager = AzureVMManager(args.subscription_id)

    try:
        if args.action == "list-vms":
            vms = manager.list_vms(args.resource_group)
            print(f"Found {len(vms)} VMs in {args.resource_group}:")
            for vm in vms:
                print(f" - {vm['name']} ({vm['size']}): {vm['provisioning_state']}")

        elif args.action == "start-vm":
            if not args.vm_name:
                print("Error: --vm-name is required for start-vm.")
                return
            print(f"Starting VM {args.vm_name}...")
            manager.start_vm(args.resource_group, args.vm_name)
            print("VM started successfully.")

        elif args.action == "stop-vm":
            if not args.vm_name:
                print("Error: --vm-name is required for stop-vm.")
                return
            print(f"Stopping VM {args.vm_name}...")
            manager.stop_vm(args.resource_group, args.vm_name)
            print("VM stopped successfully.")

    except Exception as e:
        print(f"Operation failed: {e}")

if __name__ == "__main__":
    main()
