# VehicleMetrics API Reference

## Base URL
```
http://localhost:8000/api/v1
```

## Authentication
All endpoints require Bearer token:
```
Authorization: Bearer <token>
```

## Sensor Analytics Endpoints

### Get Current Metrics
```
GET /vehicle/{vehicle_id}/current-metrics
```

**Response:**
```json
{
  "vehicle_id": "vehicle_001",
  "timestamp": "2024-07-13T10:30:00Z",
  "metrics": {
    "speed_ms": 25.5,
    "acceleration_ms2": 1.2,
    "brake_pressure_pa": 120000,
    "steering_angle_rad": 0.15
  }
}
```

### Get Trends
```
GET /vehicle/{vehicle_id}/trends?period=24h
```

**Parameters:**
- `period`: 1h, 6h, 24h, 7d, 30d
- `aggregation`: 1m, 5m, 1h (default: 1m)

**Response:**
```json
{
  "vehicle_id": "vehicle_001",
  "period": "2024-07-12T10:30:00Z/2024-07-13T10:30:00Z",
  "trends": [
    {
      "timestamp": "2024-07-13T10:30:00Z",
      "avg_speed_ms": 22.3,
      "max_speed_ms": 45.0,
      "min_speed_ms": 5.2
    }
  ]
}
```

### Get Anomalies
```
GET /vehicle/{vehicle_id}/anomalies?limit=10
```

**Response:**
```json
{
  "vehicle_id": "vehicle_001",
  "anomalies": [
    {
      "type": "speed_spike",
      "timestamp": "2024-07-13T14:30:00Z",
      "severity": "medium",
      "value": 85.5,
      "expected_range": [0, 45],
      "description": "Sudden acceleration detected"
    }
  ]
}
```

## Data Management Endpoints

### Upload Sensor Data
```
POST /data/upload
Content-Type: multipart/form-data
```

**Form Data:**
- `file`: CSV/Parquet sensor data
- `vehicle_id`: Vehicle identifier
- `format`: csv|parquet

### Query Data
```
POST /data/query
```

**Request:**
```json
{
  "vehicle_id": "vehicle_001",
  "start_time": "2024-07-13T00:00:00Z",
  "end_time": "2024-07-13T23:59:59Z",
  "sensors": ["speed", "acceleration"]
}
```

## Error Responses

### 400 Bad Request
```json
{
  "error": "Invalid request",
  "detail": "Missing required field: vehicle_id"
}
```

### 401 Unauthorized
```json
{
  "error": "Unauthorized",
  "detail": "Invalid or missing authentication token"
}
```

### 404 Not Found
```json
{
  "error": "Not found",
  "detail": "Vehicle vehicle_001 not found"
}
```

### 500 Internal Server Error
```json
{
  "error": "Internal server error",
  "detail": "Database connection failed"
}
```

## Rate Limiting

- 1000 requests/minute per API key
- 10GB/day data transfer limit
- Contact support for increased limits

## Webhooks

Subscribe to real-time events:
```
POST /webhooks/subscribe
```

**Events:**
- `anomaly_detected`
- `maintenance_alert`
- `compliance_violation`

---

For more details, see [ARCHITECTURE.md](ARCHITECTURE.md)
