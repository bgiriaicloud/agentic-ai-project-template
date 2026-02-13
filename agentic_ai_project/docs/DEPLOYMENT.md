# Agentic AI Project - Deployment Guide

This document outlines the steps to deploy the **Agentic AI Project** to a production environment using Google Kubernetes Engine (GKE).

## 📋 Prerequisites

*   **Google Cloud Platform (GCP) Account** with billing enabled.
*   **Google Cloud SDK (`gcloud`)** installed and initialized.
*   **Docker Desktop** installed.
*   **Kubernetes CLI (`kubectl`)** installed.
*   **Gemini API Key** from Google AI Studio.

---

## 🏗️ 1. Containerization

The application is containerized using Docker. The `Dockerfile` is located in the project root.

### Build and Test Locally

Before deploying, ensure the container works locally:

1.  **Build the Image:**
    ```bash
    cd agentic_ai_project
    docker build -t agentic-ai-local .
    ```

2.  **Run the Container:**
    ```bash
    docker run -p 8080:8080 -e GOOGLE_API_KEY="your_api_key" agentic-ai-local
    ```

3.  **Test the Endpoint:**
    ```bash
    curl -X POST "http://localhost:8080/agent/run" \
         -H "Content-Type: application/json" \
         -d '{"query": "Explain quantum computing"}'
    ```

---

## ☁️ 2. Google Kubernetes Engine (GKE) Deployment

### Step 1: Push Image to Container Registry

1.  **Set Project Variable:**
    ```bash
    export PROJECT_ID="your-gcp-project-id"
    export IMAGE_NAME="gcr.io/$PROJECT_ID/agentic-ai-app:v1"
    ```

2.  **Build & Push:**
    ```bash
    docker build -t $IMAGE_NAME .
    docker push $IMAGE_NAME
    ```

### Step 2: Configure Secrets

**Security Warning:** Never commit API keys to version control.

1.  **Create `k8s/secret.yaml`:**
    Copy the template and fill in your key.
    ```bash
    cp k8s/secret-template.yaml k8s/secret.yaml
    ```
    *Edit `k8s/secret.yaml` and paste your actual `GOOGLE_API_KEY`.*

### Step 3: Update Manifests

1.  **Edit `k8s/deployment.yaml`:**
    Replace the image configuration with your pushed image URL.
    ```yaml
    containers:
    - name: agentic-ai
      image: gcr.io/your-gcp-project-id/agentic-ai-app:v1 # <--- UPDATE THIS
    ```

### Step 4: Deploy to Cluster

1.  **Connect to Cluster:**
    ```bash
    gcloud container clusters get-credentials your-cluster-name --zone your-zone --project $PROJECT_ID
    ```

2.  **Apply Configuration:**
    ```bash
    kubectl apply -f k8s/secret.yaml
    kubectl apply -f k8s/deployment.yaml
    kubectl apply -f k8s/service.yaml
    ```

### Step 5: Verify Deployment

1.  **Check Status:**
    ```bash
    kubectl get pods
    kubectl get service agentic-ai-service
    ```
    *Wait for `EXTERNAL-IP` to appear.*

2.  **Test Production Endpoint:**
    ```bash
    export SERVICE_IP=$(kubectl get service agentic-ai-service -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
    
    curl -X POST "http://$SERVICE_IP:80/agent/run" \
         -H "Content-Type: application/json" \
         -d '{"query": "Plan a marketing strategy"}'
    ```

---

## 🔍 Observability & Logs

*   **View Logs:**
    ```bash
    kubectl logs -l app=agentic-ai
    ```
*   **Google Cloud Console:**
    Navigate to **Kubernetes Engine > Workloads** to see metrics and logs.

## 🛡️ Production Checklist

- [ ] **Secrets:** API keys are stored in K8s Secrets, not environment variables in `deployment.yaml`.
- [ ] **Resources:** CPU/Memory requests and limits are configured in `deployment.yaml`.
- [ ] **Replicas:** Set `replicas` count > 1 for high availability.
- [ ] **Safety:** Verify `guardrails/safety_checks.py` logic meets your safety standards.
