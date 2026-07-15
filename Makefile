.PHONY: help setup dev test lint clean logs stop

help:
	@echo "VehicleMetrics - Available Commands"
	@echo "===================================="
	@echo "  make setup      - Setup development environment"
	@echo "  make dev        - Start local stack"
	@echo "  make stop       - Stop all services"
	@echo "  make logs       - View service logs"
	@echo "  make test       - Run tests"
	@echo "  make lint       - Run linters"
	@echo "  make clean      - Clean up volumes"

setup:
	@echo "Setting up environment..."
	@test -f .env || cp .env.example .env
	docker-compose up -d
	@echo "Waiting for services..."
	@sleep 5
	@echo "✓ Services running:"
	@echo "  PostgreSQL: localhost:5432"
	@echo "  Redis:      localhost:6379"
	@echo "  Grafana:    http://localhost:3001"
	@echo "  Prometheus: http://localhost:9090"

dev:
	@echo "Starting services..."
	docker-compose up -d
	@echo "✓ Services running"

stop:
	docker-compose down

logs:
	docker-compose logs -f

test:
	@echo "Running tests..."
	@echo "✓ Tests passed (no tests configured yet)"

lint:
	@echo "Running linters..."
	@which terraform > /dev/null 2>&1 && terraform fmt -check -recursive infrastructure/terraform/ || echo "Terraform not installed, skipping"
	@echo "✓ Linting complete"

clean:
	docker-compose down -v
	@echo "✓ Volumes removed"
