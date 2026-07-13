# Deployment Guide

## Prerequisites

### AWS Setup
```bash
# Configure AWS CLI
aws configure

# Create S3 bucket for Terraform state
aws s3 mb s3://vehicle-metrics-terraform-state-prod
```

### Terraform Variables
```bash
# Copy template
cp infrastructure/terraform/dev.tfvars infrastructure/terraform/prod.tfvars

# Edit with production values
vim infrastructure/terraform/prod.tfvars
```

## Phase 1 Deployment (POC)

### Step 1: EKS Cluster
```bash
cd infrastructure/terraform

# Initialize Terraform
terraform init -backend-config="bucket=vehicle-metrics-terraform-state-prod"

# Plan deployment
terraform plan -var-file=prod.tfvars -out=tfplan

# Apply
terraform apply tfplan
```

### Step 2: Configure kubectl
```bash
# Get cluster credentials
aws eks update-kubeconfig --name vehicle-metrics-prod --region us-east-1

# Verify
kubectl get nodes
```

### Step 3: Deploy Applications
```bash
# Deploy to EKS
kubectl apply -f infrastructure/kubernetes/namespaces.yaml
kubectl apply -f infrastructure/kubernetes/deployments/

# Verify
kubectl get pods -n vehicle-metrics
```

### Step 4: Database Setup
```bash
# Get RDS endpoint
RDS_ENDPOINT=$(aws rds describe-db-instances \
  --db-instance-identifier vehicle-metrics-db \
  --query 'DBInstances[0].Endpoint.Address' \
  --output text)

# Connect and initialize
psql -h $RDS_ENDPOINT -U admin -d vehiclemetrics < \
  infrastructure/database/schema.sql
```

## Monitoring

### Prometheus
```bash
# Access Prometheus
kubectl port-forward -n vehicle-metrics svc/prometheus 9090:9090
# Visit: http://localhost:9090
```

### Grafana
```bash
# Access Grafana
kubectl port-forward -n vehicle-metrics svc/grafana 3000:3000
# Visit: http://localhost:3000
# Default: admin/admin
```

## Scaling

### Auto-Scaling
```bash
# Update HPA
kubectl autoscale deployment sensor-analytics \
  --min=2 --max=10 \
  -n vehicle-metrics
```

### Database Scaling
```bash
# Add read replica
aws rds create-db-instance-read-replica \
  --db-instance-identifier vehicle-metrics-db-read \
  --source-db-instance-identifier vehicle-metrics-db
```

## Backup & Recovery

### Automated Backups
```bash
# Enable backups (30-day retention)
aws rds modify-db-instance \
  --db-instance-identifier vehicle-metrics-db \
  --backup-retention-period 30
```

### Manual Backup
```bash
# Create snapshot
aws rds create-db-snapshot \
  --db-instance-identifier vehicle-metrics-db \
  --db-snapshot-identifier vehicle-metrics-backup-$(date +%Y%m%d)
```

## Troubleshooting

### Pod Won't Start
```bash
kubectl describe pod <pod-name> -n vehicle-metrics
kubectl logs <pod-name> -n vehicle-metrics
```

### Database Connection Issues
```bash
# Test connectivity
psql -h $RDS_ENDPOINT -U admin -d vehiclemetrics -c "SELECT 1"
```

### High Latency
```bash
# Check metrics
kubectl top pods -n vehicle-metrics
kubectl top nodes
```

## Production Checklist

- [ ] SSL certificates configured
- [ ] Backups running automatically
- [ ] Monitoring alerts configured
- [ ] Auto-scaling enabled
- [ ] VPC security groups locked down
- [ ] Read replicas configured
- [ ] CloudFront cache policies set
- [ ] Rate limiting enabled
- [ ] DDoS protection (AWS Shield)
- [ ] Audit logging enabled

---

See [ARCHITECTURE.md](ARCHITECTURE.md) for infrastructure details
