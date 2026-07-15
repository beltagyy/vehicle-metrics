# 🚗 VehicleMetrics - Autonomous Vehicle Analytics Platform

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: POC](https://img.shields.io/badge/Status-POC%20%28Month%201%29-blue.svg)]()

A cloud-native, real-time analytics platform for autonomous vehicle sensor data processing, anomaly detection, and predictive intelligence.

## 🏗️ System Architecture:

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃        PRESENTATION TIER               ┃
┃  React Dashboard + CloudFront CDN      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                      │
┏━━━━━━━━━━━━━━━━━━━━▼━━━━━━━━━━━━━━━━━━┓
┃    APPLICATION TIER (AWS EKS)         ┃
┃  • Sensor Analytics                   ┃
┃  • Brake Monitoring (Phase 2)         ┃
┃  • Safety Compliance (Phase 2)        ┃
┃  • Data Explorer (Phase 2)            ┃
┃  • AI/ML Gateway (Phase 3)            ┃
┃  • Lambda Processing                  ┃
┗━━━━━━━━━━━━━━━━━━━━▲━━━━━━━━━━━━━━━━━━┛
                      │
┏━━━━━━━━━━━━━━━━━━━━┴━━━━━━━━━━━━━━━━━━┓
┃       DATA TIER                       ┃
┃  • S3 (raw + processed)               ┃
┃  • PostgreSQL + TimescaleDB           ┃
┃  • Redis Cache                        ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

## 📊 Quick Stats

- **Timeline:** 12 months (1 POC + 11 production)
- **Phase 1:** 4 weeks, ~137 hours
- **Cost (POC):** $150-200/month ✅ Free tier eligible
- **Tech Stack:** AWS EKS, FastAPI, React, PostgreSQL, TimescaleDB, Redis
- **Documentation:** 2700+ lines with gorgeous ASCII diagrams

## 🚀 Quick Start

```bash
# Local development
docker-compose up -d

# Access services
# API:        http://localhost:8000/docs
# PostgreSQL: localhost:5432
# Redis:      localhost:6379
# Grafana:    http://localhost:3001
# Prometheus: http://localhost:9090
```

## 🔧 Backend API

FastAPI-based REST API for sensor data ingestion and retrieval.

### Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | App info |
| GET | `/health` | Health check (PostgreSQL + Redis) |
| POST | `/sensors/` | Create sensor reading |
| GET | `/sensors/` | List readings (filter by `vehicle_id`) |
| GET | `/sensors/{id}` | Get single reading |

### Run Locally (without Docker)

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 📈 Project Phases

### Phase 1: POC (Month 1)
- Data pipeline: KITTI → Lambda → PostgreSQL
- Sensor Analytics microservice
- React dashboard with live metrics
- Prometheus + Grafana monitoring

### Phase 2: Core Platform (Months 2-6)
- 4 analytics applications
- Multi-vehicle support (5-10 vehicles)
- Advanced monitoring & alerting

### Phase 3: Production (Months 7-12)
- AI/ML Gateway (GPT-4, Claude, Llama)
- Predictive maintenance models
- ISO 21434 compliance
- Scale to 50+ vehicles

## 🛠️ Tech Stack

- **Frontend:** React 18 + TypeScript
- **Backend API:** FastAPI (Python)
- **Orchestration:** AWS EKS (Kubernetes)
- **Streaming:** AWS Kinesis (+ Kafka option)
- **Time-Series DB:** PostgreSQL + TimescaleDB + pgvector
- **Cache:** Redis ElastiCache
- **Storage:** AWS S3 (multi-tier)
- **Monitoring:** Prometheus + Grafana
- **IaC:** Terraform
- **CI/CD:** GitHub Actions

## 📚 Documentation

- **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** - 30-second overview
- **[ARCHITECTURE.md](ARCHITECTURE.md)** - Technical details with diagrams
- **[TIMELINE.md](TIMELINE.md)** - 12-month roadmap
- **[PROJECT.md](PROJECT.md)** - GitHub project setup

## 🎯 Success Criteria

### Phase 1
- ✅ Data flows end-to-end
- ✅ API P99 < 200ms
- ✅ Dashboard < 2s load
- ✅ Cost < $200/month

## 📄 License

MIT License - See [LICENSE](LICENSE)

---

**Status:** 🚀 Ready to Launch | **Next:** Create GitHub Project & Issues

## 🔒 Security Vision

We treat security as a first-class product requirement. Goals:

- Never commit secrets: use environment files (.env), Docker secrets, or a secrets manager; exclude secrets from version control.
- Secure defaults: enable TLS, minimize exposed ports, and apply least-privilege service accounts and RBAC.
- Continuous hygiene: run automated dependency and image scanning, and CI checks for leaked credentials.
- Incident readiness: rotate any exposed credentials immediately and follow documented response steps.

### Known Issues

| # | Issue | Status |
|---|-------|--------|
| [#8](https://github.com/beltagyy/vehicle-metrics/issues/8) | Hardcoded credentials in `docker-compose.yml` (`POSTGRES_PASSWORD`, `GF_SECURITY_ADMIN_PASSWORD`) | Fixed in #11 |

