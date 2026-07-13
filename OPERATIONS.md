# Operations Guide

## Daily Operations

### Morning Checks (9 AM)
```bash
# Run health check
./infrastructure/scripts/health-check.sh

# Check alerts
# (Go to Grafana dashboard)

# Verify backups completed
aws rds describe-db-snapshots \
  --query "DBSnapshots[?Status=='available']" \
  --output table
```

### Evening Checks (5 PM)
```bash
# Check logs for errors
kubectl logs -n vehicle-metrics --all-containers=true

# Monitor resource usage
kubectl top nodes
kubectl top pods -n vehicle-metrics
```

## Monitoring

### Key Metrics to Monitor
- API response time (target: <200ms P99)
- Error rate (target: <0.1%)
- Data ingestion rate
- Storage usage
- Database connections
- Cache hit rate

### Alert Thresholds
- CPU > 80% for 5 minutes
- Memory > 85% for 5 minutes
- Disk > 90%
- Error rate > 1%
- Response time P99 > 500ms

## Backup & Recovery

### Automated Backups
```bash
# RDS backups: Daily at 3 AM UTC
# Retention: 30 days
# Location: AWS backup vault

# S3 backups: Continuous (versioning enabled)
# Retention: 90 days
```

### Manual Backup
```bash
# Create RDS snapshot
aws rds create-db-snapshot \
  --db-instance-identifier vehicle-metrics-db \
  --db-snapshot-identifier vehicle-metrics-manual-$(date +%Y%m%d)

# Verify
aws rds describe-db-snapshots \
  --db-snapshot-identifier vehicle-metrics-manual-20240713
```

### Recovery Procedure
```bash
# 1. Identify recovery point
aws rds describe-db-snapshots --query "DBSnapshots[].[DBSnapshotIdentifier,SnapshotCreateTime]"

# 2. Restore from snapshot
aws rds restore-db-instance-from-db-snapshot \
  --db-instance-identifier vehicle-metrics-db-recovered \
  --db-snapshot-identifier <snapshot-id>

# 3. Update endpoints in EKS
kubectl set env deployment/sensor-analytics \
  RDS_ENDPOINT=<new-endpoint> \
  -n vehicle-metrics

# 4. Verify connectivity
kubectl exec -it <pod> -n vehicle-metrics -- \
  psql -h $RDS_ENDPOINT -U admin -c "SELECT 1"
```

## Scaling

### Horizontal Pod Autoscaling
```bash
# Auto-scale based on CPU
kubectl autoscale deployment sensor-analytics \
  --min=2 --max=10 \
  --cpu-percent=80 \
  -n vehicle-metrics
```

### Database Scaling
```bash
# Add read replica
aws rds create-db-instance-read-replica \
  --db-instance-identifier vehicle-metrics-db-read-1 \
  --source-db-instance-identifier vehicle-metrics-db \
  --db-instance-class db.t3.small
```

## Updates & Patching

### Kubernetes Updates
```bash
# Check current version
kubectl version --short

# Update EKS cluster
aws eks update-cluster-version \
  --name vehicle-metrics-cluster \
  --kubernetes-version 1.29

# Update node group
aws eks update-nodegroup-version \
  --cluster-name vehicle-metrics-cluster \
  --nodegroup-name vehicle-metrics-node-group \
  --kubernetes-version 1.29
```

### Application Updates
```bash
# Build new image
docker build -t vehicle-metrics:v1.2.0 .

# Push to ECR
aws ecr get-login-password | docker login --username AWS --password-stdin $ECR_REGISTRY
docker push $ECR_REGISTRY/vehicle-metrics:v1.2.0

# Update deployment
kubectl set image deployment/sensor-analytics \
  sensor-analytics=$ECR_REGISTRY/vehicle-metrics:v1.2.0 \
  -n vehicle-metrics

# Verify rollout
kubectl rollout status deployment/sensor-analytics -n vehicle-metrics
```

## Troubleshooting

### Pod Not Starting
```bash
# Check pod status
kubectl describe pod <pod-name> -n vehicle-metrics

# Check logs
kubectl logs <pod-name> -n vehicle-metrics --previous

# Check events
kubectl get events -n vehicle-metrics --sort-by='.lastTimestamp'
```

### Database Connection Issues
```bash
# Test RDS connectivity
psql -h $RDS_ENDPOINT -U admin -d vehiclemetrics -c "SELECT 1"

# Check security group
aws ec2 describe-security-groups \
  --group-ids <db-sg-id> \
  --query "SecurityGroups[].IpPermissions"
```

### High Latency
```bash
# Check pod resource usage
kubectl top pod <pod-name> -n vehicle-metrics

# Check node capacity
kubectl top node

# Check network policies
kubectl get networkpolicies -n vehicle-metrics
```

## Runbooks

### Emergency - Database Down
1. Check AWS RDS console for status
2. Initiate failover if Multi-AZ
3. Restore from latest snapshot if needed
4. Update connection strings
5. Verify application connectivity
6. Run health check

### Emergency - API Pod Crashes
1. Check logs: `kubectl logs <pod> -n vehicle-metrics`
2. Check resources: `kubectl top pod <pod>`
3. Scale replicas: `kubectl scale deployment sensor-analytics --replicas=3`
4. Check dependencies (database, cache)
5. Restart pod if necessary

### Emergency - Storage Full
1. Identify large tables: Check CloudWatch metrics
2. Archive old data to S3
3. Delete old data if not needed
4. Increase storage if necessary
5. Monitor for recurrence

---

See [DEPLOYMENT.md](DEPLOYMENT.md) for deployment procedures
