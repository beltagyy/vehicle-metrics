#!/bin/bash

echo "🏥 Health Check for VehicleMetrics"
echo "===================================="
echo ""

# Check EKS cluster
echo "📊 EKS Cluster Status:"
kubectl cluster-info
echo ""

# Check nodes
echo "🖥️  Node Status:"
kubectl get nodes
echo ""

# Check pods
echo "🐳 Pod Status:"
kubectl get pods --all-namespaces
echo ""

# Check services
echo "🌐 Services:"
kubectl get svc --all-namespaces
echo ""

# Check PVCs
echo "💾 Persistent Volumes:"
kubectl get pvc --all-namespaces
echo ""

echo "✅ Health check complete!"
