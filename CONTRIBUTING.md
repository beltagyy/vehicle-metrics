# Contributing to VehicleMetrics

## Getting Started

### Prerequisites
- Python 3.11+
- Node.js 18+
- Docker & Docker Compose
- AWS CLI (configured)
- Terraform 1.5+

### Local Development Setup

```bash
# Clone repository
git clone https://github.com/beltagyy/vehicle-metrics.git
cd vehicle-metrics

# Start local environment
docker-compose up -d

# Verify services
docker-compose ps
```

### Development Workflow

1. **Create Feature Branch**
```bash
git checkout -b feature/issue-#XXX-description
```

2. **Make Changes**
```bash
# Code, test, commit
git add .
git commit -m "feat: Description of change (fixes #XXX)"
```

3. **Push & Create PR**
```bash
git push origin feature/issue-#XXX-description
# Create pull request on GitHub
```

## Code Standards

### Python
- Black for formatting
- Pylint for linting
- 80% test coverage minimum
- Type hints required

### JavaScript/React
- ESLint configuration included
- Prettier for formatting
- 80% test coverage
- TypeScript for all new code

### Git Commits
- Use conventional commits: `feat:`, `fix:`, `docs:`, `test:`, `chore:`
- Reference issue numbers: `(fixes #123)`
- Keep commits atomic and logical
- Write descriptive commit messages

## Testing

```bash
# Run all tests
make test

# Run specific test
pytest tests/test_etl.py -v

# Check coverage
pytest --cov=applications --cov=processing
```

## Deployment

### Staging
```bash
git push origin feature/branch
# GitHub Actions runs tests automatically
# Manual deploy to staging environment
```

### Production
```bash
# Create release tag
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0

# Production deployment via GitHub Actions
```

## Documentation

- Update README.md for user-facing changes
- Update ARCHITECTURE.md for structural changes
- Add docstrings to all new functions
- Update API docs in docs/ folder

## Reporting Issues

Use GitHub Issues with appropriate template:
- Bug reports
- Feature requests
- Documentation improvements

## Code Review

All PRs require:
- Tests passing
- Code review approval
- Documentation updated
- No merge conflicts

---

Thanks for contributing to VehicleMetrics!
