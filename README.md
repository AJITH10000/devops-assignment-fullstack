# DevOps Fullstack App

This project demonstrates a two-tier fullstack app deployed on AWS using DevOps tools.

## 📁 Project Structure

- `backend/`: Flask REST API
- `frontend/`: Next.js UI
- `infra/`: Terraform scripts for AWS ECS + ALB
- `.github/workflows/`: CI/CD pipeline using GitHub Actions

## 🔧 Setup

1. Clone the repo
2. Configure secrets in GitHub
3. Run `terraform apply` in `infra/`
4. Push to `develop` → triggers build/test
5. Merge to `main` → deploys to AWS

## ✅ Endpoints

- Backend: `/health`, `/api/message`
- Frontend: `/` with a button to call backend

---
