## DevOps Fullstack App

This project demonstrates a two-tier fullstack application deployed on AWS using Docker, GitHub Actions (CI/CD), and Terraform. It includes a Flask backend and a Next.js frontend, both containerized and orchestrated using AWS ECS with an Application Load Balancer.

---

##  Project Structure 
devops-fullstack-app/
│
├── backend/                  # Python Flask/FastAPI backend
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── tests/
│       └── test_app.py
│
├── frontend/                 # Next.js frontend
│   ├── pages/
│   │   └── index.js
│   ├── package.json
│   ├── Dockerfile
│   └── tests/
│       └── e2e.test.js
│
├── infra/                    # Terraform infrastructure
│   ├── main.tf
│   ├── variables.tf
│   ├── vpc.tf
│   ├── ecs.tf
│   ├── alb.tf
│   ├── iam.tf
│   └── outputs.tf
│
├── .github/
│   └── workflows/
│       └── dev.yml          # GitHub Actions CI/CD workflow
│
├── README.md                 # Overview and instructions
└── .gitignore

---
###  1. Clone the Repository

git https://github.com/AJITH10000/devops-assignment-fullstack.git

cd devops-assignment-fullstack

---
### 2. Configure GitHub Secrets
Set the following secrets in your GitHub repository:

AWS_ACCESS_KEY_ID

AWS_SECRET_ACCESS_KEY

AWS_REGION

AWS_ACCOUNT_ID

BACKEND_IMAGE – ECR URI for backend (e.g., 123456789.dkr.ecr.region.amazonaws.com/backend)

FRONTEND_IMAGE – ECR URI for frontend

### 3. Run Terraform to Provision Infrastructure
cd infra
terraform init
terraform plan
terraform apply

### CI/CD Workflow

The GitHub Actions pipeline (.github/workflows/ci-cd.yml) performs the following:

On push to develop:

Run backend tests using Pytest

Run frontend tests using npm

Build Docker images and push to AWS ECR

On merge to main:

Deploy updated services on ECS using pushed images

### API & UI Endpoints

Once deployed, use the Load Balancer DNS name (output from Terraform):

alb_dns = "http://<alb-dns-name>"


### Monitoring & Alerting
AWS CloudWatch Dashboards for:

CPU Utilization

Memory Usage

Request Count

Alarm:

Email notification if CPU > 70% for 5 minutes (via SNS)

### IAM & Secrets

ECS Task Role: Only required permissions for ECR, SecretsManager, CloudWatch

Secrets (e.g., database credentials or API keys) stored in AWS Secrets Manager

Fetched securely at runtime by ECS task definitions

Network security configured using Security Groups and private/public subnets

### Dockerization

Multi-stage Dockerfiles used for both services to keep images small and secure.

Sample build (automated in CI):
# Backend
cd backend
docker build -t backend .
# Frontend
cd frontend
docker build -t frontend .

### Testing
Backend: pytest unit tests under backend/tests/

Frontend: Jest or Cypress end-to-end tests under frontend/tests/

### Submission Checklist 

- README.md with setup & architecture overview

- Backend and frontend pass all tests locally and in CI

- Docker images pushed to AWS ECR with Git SHA tags

- Terraform infrastructure deployed successfully on AWS

- CI/CD pipeline deploys on main merges

- CloudWatch dashboards and alarms configured

- IAM roles are least-privileged and secrets are securely managed



###  Author
 Koppala Ajith Kumar Reddy
🔗 GitHub: https://github.com/AJITH10000

