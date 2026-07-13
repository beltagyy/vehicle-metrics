# VehicleMetrics - Architecture

## 3-Tier Cloud-Native Design

### Tier 1: Presentation
- React SPA (TypeScript)
- CloudFront CDN
- S3 hosting

### Tier 2: Application (AWS EKS)
- Sensor Analytics Service
- Brake Monitoring (Phase 2)
- Safety Compliance (Phase 2)
- Data Explorer (Phase 2)
- AI/ML Gateway (Phase 3)
- Lambda Processing
- Monitoring Stack

### Tier 3: Data
- S3 (raw + processed)
- PostgreSQL + TimescaleDB (time-series)
- Redis (cache)

## Data Flow

```
Vehicle → Kinesis → Lambda (ETL) → Storage
                                      ↓
                                   Analytics
                                      ↓
                                   Dashboard
```

## Key Technologies

| Component | Technology | Rationale |
|-----------|-----------|-----------|
| Orchestration | AWS EKS | Managed Kubernetes |
| Streaming | Kinesis | AWS-native, managed |
| Processing | Lambda | Serverless, scales to zero |
| DB | PostgreSQL + TimescaleDB | Time-series optimized |
| Cache | Redis | Fast, TTL support |
| API | FastAPI | Python, async, fast |
| Frontend | React | Modern, interactive |
| Monitoring | Prometheus + Grafana | Industry standard |

---
See README.md for full overview
