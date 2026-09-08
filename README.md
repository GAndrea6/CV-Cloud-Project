# ☁️ Azure Cloud Resume Challenge

[![Deploy Frontend](https://github.com/GAndrea6/CV-Cloud-Project/actions/workflows/frontend.yml/badge.svg)](https://github.com/GAndrea6/CV-Cloud-Project/actions/workflows/frontend.yml)
[![Deploy Backend](https://github.com/GAndrea6/CV-Cloud-Project/actions/workflows/backend.yml/badge.svg)](https://github.com/GAndrea6/CV-Cloud-Project/actions/workflows/backend.yml)

A fully serverless, highly available online resume application deployed on Microsoft Azure using Infrastructure as Code (Terraform) and Automated CI/CD Pipelines (GitHub Actions).

---



## 🏛️ Architecture Overview

```text
 [ Client Browser ]
        |
        v  (HTTPS)
 [ Azure Static Web App ] ---> Serves HTML / CSS / JS Frontend
        |
        v  (Fetch API / CORS)
 [ Azure Function App ]   ---> Python Serverless Backend (HTTP Trigger)
        |
        v  (Cosmos SDK)
 [ Azure Cosmos DB ]      ---> NoSQL Database (Visitor Counter Storage)


 
 
 ✨ Features & Technical Stack
Frontend: HTML5, CSS3, and JavaScript hosted on Azure Static Web Apps.

Backend: Azure Functions (Python 3.10) with HTTP Trigger providing a serverless API endpoint.

Database: Azure Cosmos DB (Serverless / NoSQL API) tracking total visitor count.

Infrastructure as Code (IaC): Complete Azure environment provisioned via Terraform.

CI/CD Workflows:

Automated Static Web App deployment via Azure/static-web-apps-deploy.

Automated Python Function deployment via Azure/functions-action with automated pytest execution.

Observability: Real-time performance and error telemetry tracked via Azure Application Insights (KQL Queries).



📂 Project Structure
.
├── .github/
│   └── workflows/
│       ├── frontend.yml    # CI/CD pipeline for Frontend
│       └── backend.yml     # CI/CD pipeline & tests for Backend
├── backend/
│   ├── function_app.py     # Azure Function Python logic
│   ├── requirements.txt    # Python dependencies
│   └── test_function.py    # Pytest unit testing suite
├── frontend/
│   ├── index.html          # Resume Layout
│   ├── style.css           # Styling
│   └── main.js             # API Integration script
├── main.tf                 # Terraform infrastructure definition
└── README.md



🛠️ Local Development & Testing
Running Backend Locally

cd backend
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
func start



Running Pytest Unit Tests

cd backend
pytest test_function.py