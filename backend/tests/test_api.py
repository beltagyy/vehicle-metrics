from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["app"] == "VehicleMetrics"
    assert "version" in data


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert "services" in data


def test_create_sensor_reading():
    payload = {
        "vehicle_id": "test-vehicle-001",
        "sensor_type": "lidar",
        "value": 42.5,
        "unit": "meters",
    }
    response = client.post("/sensors/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["vehicle_id"] == "test-vehicle-001"
    assert data["sensor_type"] == "lidar"
    assert data["value"] == 42.5
    assert "id" in data
    assert "timestamp" in data


def test_list_sensor_readings():
    response = client.get("/sensors/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_get_sensor_reading_not_found():
    response = client.get("/sensors/999999")
    assert response.status_code == 404
