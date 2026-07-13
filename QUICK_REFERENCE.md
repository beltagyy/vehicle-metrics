# VehicleMetrics - Quick Reference

## 30-Second Overview

**What:** Cloud analytics platform for autonomous vehicle sensor data
**Why:** Ingest, process, analyze vehicle telemetry in real-time
**How:** Kinesis → Lambda → PostgreSQL → Analytics → Dashboard
**Timeline:** 12 months (1 POC + 11 production)
**Team:** Solo developer
**Cost:** $150-200/month (POC)

## Architecture

```
Vehicle Data → S3 → Lambda → PostgreSQL → Microservices → React Dashboard → CloudFront
```

## Phase 1 (Month 1) - POC
- Week 1: AWS Infrastructure (EKS, RDS, S3, Redis)
- Week 2: Data Pipeline (KITTI → PostgreSQL)
- Week 3: Sensor Analytics API (FastAPI)
- Week 4: React Dashboard + Monitoring

**Effort:** ~137 hours

## Tech Stack
- Frontend: React + TypeScript
- Backend: FastAPI
- Orchestration: AWS EKS
- DB: PostgreSQL + TimescaleDB
- Cache: Redis
- Monitoring: Prometheus + Grafana

## Quick Commands
```bash
docker-compose up -d           # Start local stack
make deploy-infra             # Deploy to AWS
make test                     # Run tests
```

---
**Status:** 🚀 Ready to Launch
