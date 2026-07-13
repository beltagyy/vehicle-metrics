#!/bin/bash

set -e

PROJECT_NAME="vehicle-metrics"
AWS_REGION="us-east-1"

echo "🚀 Deploying VehicleMetrics to EKS..."

# Get cluster info
echo "📊 Fetching cluster info..."
CLUSTER_NAME=$(terraform output -raw eks_cluster_name)
RDS_ENDPOINT=$(terraform output -raw rds_endpoint)
REDIS_ENDPOINT=$(terraform output -raw redis_endpoint)

# Configure kubectl
echo "🔧 Configuring kubectl..."
aws eks update-kubeconfig \
  --name $CLUSTER_NAME \
  --region $AWS_REGION

# Create namespaces
echo "📁 Creating namespaces..."
kubectl apply -f infrastructure/kubernetes/namespaces.yaml

# Create ConfigMaps
echo "⚙️  Creating ConfigMaps..."
kubectl create configmap vehicle-metrics-config \
  --from-literal=RDS_ENDPOINT=$RDS_ENDPOINT \
  --from-literal=REDIS_ENDPOINT=$REDIS_ENDPOINT \
  -n vehicle-metrics \
  --dry-run=client -o yaml | kubectl apply -f -

# Create secrets
echo "🔐 Creating secrets..."
RDS_PASSWORD=$(terraform output -raw rds_password)
kubectl create secret generic vehicle-metrics-secrets \
  --from-literal=RDS_PASSWORD=$RDS_PASSWORD \
  -n vehicle-metrics \
  --dry-run=client -o yaml | kubectl apply -f -

echo "✅ Deployment complete!"
echo ""
echo "📊 Cluster Info:"
echo "  Cluster: $CLUSTER_NAME"
echo "  Region: $AWS_REGION"
echo "  Namespace: vehicle-metrics"
echo ""
echo "🎯 Next steps:"
echo "  1. kubectl get pods -n vehicle-metrics"
echo "  2. Deploy applications"
echo "  3. Configure monitoring"
