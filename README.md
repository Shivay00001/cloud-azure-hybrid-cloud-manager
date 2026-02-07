# Cloud Azure Hybrid Cloud Manager

[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB.svg)](https://www.python.org/)
[![Azure SDK](https://img.shields.io/badge/Azure_SDK-1.28-0078D4.svg)](https://azure.microsoft.com/en-us/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A **production-grade hybrid cloud management tool** for Microsoft Azure. This repository provides a Python-based interface for managing Azure Virtual Machines and simulating hybrid connectivity scenarios, using the official Azure SDK for Python.

## 🚀 Features

- **VM Management**: Programmatic control over Azure VMs (Start, Stop, Restart, List).
- **Hybrid Connection Simulation**: Mock implementation of Azure Relay/Hybrid Connections logic.
- **Secure Authentication**: Uses `DefaultAzureCredential` for seamless local and cloud authentication.
- **Resource Group Auditing**: Automated listing and status checks of resources within groups.
- **Type Safety**: Fully typed Python codebase with Pydantic models.

## 📁 Project Structure

```
cloud-azure-hybrid-cloud-manager/
├── src/
│   ├── azure_ops/        # Azure management logic
│   │   ├── vm_manager.py
│   │   └── hybrid_connect.py
│   └── main.py           # CLI Entrypoint
├── tests/                # Unit tests
├── requirements.txt
└── Dockerfile
```

## 🛠️ Quick Start

```bash
# Clone
git clone https://github.com/Shivay00001/cloud-azure-hybrid-cloud-manager.git

# Install
pip install -r requirements.txt

# Run CLI (Requires Azure Login)
az login
python src/main.py list-vms --resource-group my-rg
```

## 📄 License

MIT License
