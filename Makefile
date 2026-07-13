.PHONY: help setup dev test deploy-infra

help:
	@echo "VehicleMetrics - Available Commands"
	@echo "setup                - Setup development environment"
	@echo "dev                  - Start local stack"
	@echo "test                 - Run tests"
	@echo "deploy-infra         - Deploy to AWS"

setup:
	@echo "Setting up environment..."
	docker-compose up -d

dev:
	@echo "Starting services..."
	docker-compose up -d
	@echo "Services running on:"
	@echo "  PostgreSQL: localhost:5432"
	@echo "  Grafana: http://localhost:3001"

test:
	@echo "Running tests..."

deploy-infra:
	@echo "Deploying to AWS..."
