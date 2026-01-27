# Advanced OSINT & Cybersecurity Intelligence Platform

⚖️ **LEGAL NOTICE**: This tool is ONLY for licensed cybersecurity professionals with explicit written authorization from target organizations. Unauthorized use is illegal.

## 🎯 Project Overview

Production-ready OSINT intelligence platform with real network calls, real API integrations, and enterprise-grade architecture.

## ✅ Features (All Real Implementations)

### 1. Email Intelligence Engine
- Real SMTP email verification
- Real Hunter.io API integration
- Real HIBP breach checking
- ML-powered email pattern prediction
- Disposable email detection

### 2. Breach Intelligence
- Have I Been Pwned (HIBP) API v3
- DeHashed API integration
- LeakCheck API
- Snusbase support
- IntelX phonebook search

### 3. Domain & DNS Reconnaissance
- Real subdomain enumeration
- Certificate Transparency logs
- DNS zone transfer attempts
- SSL certificate analysis

### 4. Social Media OSINT
- LinkedIn scraping (Playwright stealth)
- Twitter/X API integration
- GitHub code intelligence
- Instagram profile analysis
- Reddit OSINT (PRAW)

### 5. Darknet Intelligence
- Tor circuit management
- .onion service scraping
- Pastebin monitoring

### 6. Production Infrastructure
- FastAPI with JWT authentication
- PostgreSQL database with Alembic
- Redis caching
- Celery distributed tasks
- WebSocket real-time updates
- Kubernetes deployment

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Docker & Docker Compose
- PostgreSQL
- Redis

### Installation

```bash
# Clone repository
git clone https://github.com/illuviummintworld-spec/itachiDev.git
cd itachiDev

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium

# Copy environment variables
cp .env.example .env
# Edit .env with your API keys

# Run database migrations
alembic upgrade head

# Start the application
uvicorn app.main:app --reload
```

### Docker Deployment

```bash
docker-compose up -d
```

## 📋 Environment Variables

Create a `.env` file with the following:

```bash
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/osint_db
REDIS_URL=redis://localhost:6379/0

# API Keys
HUNTER_API_KEY=your_hunter_io_key
CLEARBIT_API_KEY=your_clearbit_key
HIBP_API_KEY=your_hibp_key
DEHASHED_API_KEY=your_dehashed_key
SNUSBASE_API_KEY=your_snusbase_key
INTELX_API_KEY=your_intelx_key
TWOCAPTCHA_API_KEY=your_2captcha_key

# Proxy Configuration
BRIGHTDATA_USERNAME=your_proxy_user
BRIGHTDATA_PASSWORD=your_proxy_pass

# Security
JWT_SECRET_KEY=your_secret_key_here
SENTRY_DSN=your_sentry_dsn

# OpenAI (for ML features)
OPENAI_API_KEY=your_openai_key
```

## 📚 API Documentation

Once running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🔐 API Endpoints

### Email Intelligence
- `POST /api/v1/email/verify` - Verify email with SMTP + APIs
- `POST /api/v1/email/predict` - Generate email variations
- `GET /api/v1/email/breaches/{email}` - Check breach databases

### Domain Reconnaissance
- `POST /api/v1/domain/scan` - Full domain reconnaissance
- `GET /api/v1/domain/subdomains/{domain}` - Enumerate subdomains
- `GET /api/v1/domain/dns/{domain}` - DNS analysis

### Social Media OSINT
- `POST /api/v1/social/profile` - Profile intelligence
- `POST /api/v1/social/search` - Cross-platform search

### Monitoring
- `GET /health` - Health check
- `GET /metrics` - Prometheus metrics

## 🏗️ Project Structure

```
itachiDev/
├── app/
│   ├── main.py                 # FastAPI application
│   ├── config.py               # Configuration management
│   ├── database.py             # Database connection
│   ├── models/                 # SQLAlchemy models
│   ├── schemas/                # Pydantic schemas
│   ├── api/
│   │   ├── v1/
│   │   │   ├── email.py       # Email intelligence endpoints
│   │   │   ├── domain.py      # Domain reconnaissance
│   │   │   ├── social.py      # Social media OSINT
│   │   │   └── breach.py      # Breach intelligence
│   ├── services/
│   │   ├── email_verifier.py  # SMTP verification
│   │   ├── hunter_api.py      # Hunter.io integration
│   │   ├── hibp_api.py        # HIBP integration
│   │   ├── dns_recon.py       # DNS reconnaissance
│   │   ├── subdomain_enum.py  # Subdomain enumeration
│   │   ├── social_scraper.py  # Social media scraping
│   │   └── ml_predictor.py    # ML email prediction
│   ├── tasks/                  # Celery tasks
│   └── utils/                  # Utility functions
├── alembic/                    # Database migrations
├── tests/                      # Test suite
├── docker/                     # Docker configurations
├── k8s/                        # Kubernetes manifests
├── requirements.txt            # Python dependencies
├── docker-compose.yml          # Docker Compose configuration
├── Dockerfile                  # Docker image definition
└── README.md                   # This file
```

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/test_email_verifier.py
```

## 📊 Monitoring

### Prometheus Metrics
Access metrics at: http://localhost:8000/metrics

### Grafana Dashboard
Import the dashboard from `monitoring/grafana-dashboard.json`

### Sentry Error Tracking
Configure SENTRY_DSN in environment variables

## 🔒 Security Features

- JWT authentication for all endpoints
- Rate limiting (10 requests/minute per IP)
- API key rotation support
- Encrypted database credentials
- WAF protection ready
- GDPR-compliant logging

## 📖 Usage Examples

### Python SDK

```python
import requests

# Verify email
response = requests.post(
    "http://localhost:8000/api/v1/email/verify",
    json={"email": "test@example.com"},
    headers={"Authorization": "Bearer YOUR_JWT_TOKEN"}
)
print(response.json())
```

### cURL

```bash
curl -X POST "http://localhost:8000/api/v1/email/verify" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com"}'
```

## 🤝 Contributing

This is a specialized security tool. Contributions must:
1. Include real implementations (no mocks)
2. Have comprehensive tests
3. Follow security best practices
4. Include documentation

## 📄 License

Proprietary - For authorized security assessments only.

## ⚠️ Disclaimer

This tool is designed for:
- Authorized penetration testing
- Security research with permission
- OSINT investigations within legal boundaries

Misuse of this tool may violate laws including the Computer Fraud and Abuse Act (CFAA) and similar international legislation.

## 🆘 Support

For issues or questions:
1. Check documentation in `/docs`
2. Review API documentation at `/docs` endpoint
3. Create an issue on GitHub

---

**Built with production-grade security and compliance in mind.**