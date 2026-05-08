# Cloud-Native Trading Application Deployment using Kubernetes & DevOps

## Project Overview

This project demonstrates the end-to-end deployment of a cloud-native trading application using modern DevOps and Kubernetes practices. The application was containerized using Docker and deployed on Kubernetes with automated CI/CD pipelines using GitHub Actions.

The primary objective of this project was to build a scalable, production-style infrastructure setup that reflects real-world DevOps workflows including container orchestration, ingress management, service discovery, deployment automation, and troubleshooting.

---

## Key Features

* Containerized frontend and backend applications using Docker
* Kubernetes-based deployment architecture
* Automated CI/CD pipeline using GitHub Actions
* Kubernetes Deployments, Services, and Ingress configuration
* NGINX Ingress Controller setup for external traffic routing
* Service discovery and internal communication handling
* Secure and scalable application deployment practices
* Infrastructure troubleshooting and operational monitoring

---

## Technologies Used

* Kubernetes
* Docker
* GitHub Actions
* NGINX Ingress Controller
* YAML
* Linux
* Git & GitHub
* Cloud Shell

---

## Project Architecture

The application consists of:

* Frontend Application
* Backend Application
* Kubernetes Deployments
* ClusterIP Services
* NGINX Ingress Controller
* CI/CD Workflow Pipeline

Traffic flows through the Ingress Controller, which routes requests securely to the frontend and backend services running inside the Kubernetes cluster.

---

## CI/CD Workflow

1. Developer pushes code to GitHub
2. GitHub Actions pipeline gets triggered
3. Docker images are built automatically
4. Kubernetes manifests are deployed
5. Application updates are rolled out inside the cluster

---

## Challenges Faced

During the project implementation, several real-world troubleshooting scenarios were handled, including:

* Kubernetes service discovery issues
* Ingress routing problems
* HTTPS and external exposure configuration
* Debugging pod communication
* Endpoint and networking validation
* YAML configuration troubleshooting

These challenges helped strengthen practical understanding of Kubernetes networking and production deployment workflows.

---

## Learning Outcomes

Through this project, I gained hands-on experience in:

* Kubernetes architecture and deployment strategies
* Docker containerization
* CI/CD automation
* Kubernetes networking and ingress management
* Troubleshooting production-style infrastructure issues
* DevOps best practices and automation workflows

---

## Future Enhancements

* Helm chart implementation
* Monitoring using Prometheus & Grafana
* Terraform-based infrastructure provisioning
* AKS deployment
* Secret management integration
* Autoscaling and production hardening
