# 🚀 FastAPI ELK Stack Monitoring System

A production-ready FastAPI application with complete ELK (Elasticsearch, Logstash, Kibana) stack integration for real-time logging, monitoring, and analytics.

![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-009688?style=flat&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=flat&logo=docker)
![Elasticsearch](https://img.shields.io/badge/Elasticsearch-8.11.3-005571?style=flat&logo=elasticsearch)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat&logo=python)

## 📑 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [API Documentation](#api-documentation)
- [Monitoring & Logs](#monitoring--logs)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Deployment](#deployment)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This project demonstrates a complete microservices logging and monitoring solution using:
- **FastAPI** for building high-performance REST APIs
- **Uvicorn** as the ASGI server
- **Docker** for containerization
- **Elasticsearch** for log storage and search
- **Logstash** for log processing and enrichment
- **Kibana** for visualization and analytics

Perfect for learning DevOps practices, microservices architecture, and observability patterns.

## ✨ Features

### API Features
- ✅ RESTful CRUD operations
- ✅ Data validation with Pydantic
- ✅ Interactive API documentation (Swagger UI)
- ✅ Comprehensive error handling
- ✅ Structured logging

### Infrastructure Features
- ✅ Fully containerized with Docker Compose
- ✅ Centralized logging with ELK stack
- ✅ Real-time log monitoring
- ✅ Log aggregation and parsing
- ✅ Custom log visualization dashboards
- ✅ Health check endpoints
- ✅ Production-ready configuration

### Monitoring Features
- ✅ Multi-level logging (DEBUG, INFO, WARNING, ERROR)
- ✅ Request/response logging
- ✅ Performance metrics
- ✅ Error tracking and alerting
- ✅ Historical log analysis

## 🏗️ Architecture
```
┌─────────────────────────────────────────────────────────────┐
│                     Client/Browser                          │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ↓
         ┌───────────────────────┐
         │   FastAPI Application │
         │    (Port 8000)        │
         │   - REST API          │
         │   - Business Logic    │
         │   - Data Validation   │
         └───────────┬───────────┘
                     │
                     ├──→ Local File Logging (/app/logs/app.log)
                     │
                     ↓
         ┌───────────────────────┐
         │      Logstash         │
         │    (Port 5000)        │
         │   - Log Collection    │
         │   - Parsing           │
         │   - Enrichment        │
         └───────────┬───────────┘
                     │
                     ↓
┌────────────────────────────────────┐
│         Elasticsearch              │
│         (Port 9200)                │
│   - Document Storage               │
│   - Full-text Search               │
│   - Aggregations                   │
└────────────┬───────────────────────┘
             │
             ↓
┌────────────────────────────────────┐
│           Kibana                   │
│         (Port 5601)                │
│   - Data Visualization             │
│   - Dashboards                     │
│   - Alerts & Monitoring            │
└────────────────────────────────────┘
```

## 📋 Prerequisites

- **Docker** 20.10+ and **Docker Compose** 2.0+
- **Python** 3.11+ (for local development)
- **Git** 2.30+
- Minimum **4GB RAM** and **20GB disk space**
- Linux/Unix environment (Ubuntu 22.04 recommended)

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/fastapi-elk-project.git
cd fastapi-elk-project
```

### 2. Start All Services
```bash
# Build and start all containers
docker-compose -f docker-compose-elk.yml up -d

# Wait for services to initialize (2-3 minutes)
# Check status
docker-compose -f docker-compose-elk.yml ps
```

### 3. Verify Services
```bash
# Check FastAPI
curl http://localhost:8000/health

# Check Elasticsearch
curl http://localhost:9200/

# Check Kibana (open in browser)
# http://localhost:5601
```

### 4. Access the Application

- **FastAPI Swagger Docs**: http://localhost:8000/docs
- **FastAPI ReDoc**: http://localhost:8000/redoc
- **Kibana Dashboard**: http://localhost:5601
- **Elasticsearch API**: http://localhost:9200

## 📚 API Documentation

### Endpoints

#### Health Check
```bash
GET /health
```

#### Items Management

**Create Item**
```bash
POST /items/
Content-Type: application/json

{
  "name": "Laptop",
  "description": "Gaming laptop",
  "price": 1299.99,
  "quantity": 10
}
```

**List All Items**
```bash
GET /items/
```

**Get Specific Item**
```bash
GET /items/{item_id}
```

**Delete Item**
```bash
DELETE /items/{item_id}
```

**Generate Test Logs**
```bash
GET /logs/test
```

### Example Usage
```bash
# Create multiple items
curl -X POST http://localhost:8000/items/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Mouse","description":"Wireless","price":29.99,"quantity":50}'

# List all items
curl http://localhost:8000/items/ | jq

# Get specific item
curl http://localhost:8000/items/1 | jq

# Delete item
curl -X DELETE http://localhost:8000/items/1
```

## 📊 Monitoring & Logs

### View Docker Logs
```bash
# FastAPI logs
docker logs -f fastapi-app

# Elasticsearch logs
docker logs elasticsearch

# Logstash logs
docker logs logstash

# Kibana logs
docker logs kibana
```

### View Application Logs
```bash
# Real-time log monitoring
tail -f logs/app.log

# Search for errors
grep ERROR logs/app.log

# Count log levels
grep -c INFO logs/app.log
```

### Kibana Setup

1. Open http://localhost:5601
2. Go to **Menu** → **Stack Management** → **Data Views**
3. Create data view with pattern: `fastapi-logs-*`
4. Select `@timestamp` as time field
5. Go to **Discover** to view logs
6. Create visualizations and dashboards

### Sample Kibana Queries
```
# Search for errors
log_level: ERROR

# Search in messages
log_message: "Item created"

# Combined query
log_level: (WARNING OR ERROR) AND application: "fastapi-elk-demo"

# Time-based query
@timestamp >= "now-1h"
```

## 📁 Project Structure
```
fastapi-elk-project/
│
├── app/                          # Application code
│   ├── main.py                   # FastAPI application
│   └── requirements.txt          # Python dependencies
│
├── elk/                          # ELK Stack configurations
│   ├── elasticsearch/
│   │   └── elasticsearch.yml     # Elasticsearch config
│   ├── kibana/
│   │   └── kibana.yml           # Kibana config
│   └── logstash/
│       └── logstash.conf        # Logstash pipeline
│
├── logs/                         # Application logs (gitignored)
│   └── app.log
│
├── Dockerfile                    # FastAPI container definition
├── docker-compose.yml            # Basic Docker Compose
├── docker-compose-elk.yml        # Full stack with ELK
├── .gitignore                    # Git ignore rules
└── README.md                     # This file
```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file (optional):
```env
# FastAPI
FASTAPI_PORT=8000
LOG_LEVEL=INFO

# Elasticsearch
ES_JAVA_OPTS=-Xms512m -Xmx512m

# Logstash
LS_JAVA_OPTS=-Xms256m -Xmx256m
```

### Customize Logging

Edit `app/main.py` to adjust log levels:
```python
logging.basicConfig(
    level=logging.INFO,  # Change to DEBUG, WARNING, ERROR
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
```

### Logstash Patterns

Edit `elk/logstash/logstash.conf` to customize log parsing:
```ruby
filter {
  grok {
    match => { 
      "message" => "YOUR_CUSTOM_PATTERN"
    }
  }
}
```

## 🚀 Deployment

### GCP Deployment
```bash
# Create VM instance
gcloud compute instances create fastapi-elk \
  --zone=us-central1-a \
  --machine-type=e2-medium \
  --image-family=ubuntu-2204-lts \
  --boot-disk-size=20GB

# SSH into instance
gcloud compute ssh fastapi-elk --zone=us-central1-a

# Clone and deploy
git clone <your-repo>
cd fastapi-elk-project
docker-compose -f docker-compose-elk.yml up -d
```

### Production Considerations

- Use environment variables for secrets
- Set up SSL/TLS certificates
- Configure firewall rules properly
- Enable authentication for Elasticsearch/Kibana
- Set up automated backups
- Implement log rotation
- Configure resource limits
- Set up monitoring alerts

## 🐛 Troubleshooting

### Services Won't Start
```bash
# Check container status
docker-compose -f docker-compose-elk.yml ps

# View logs
docker-compose -f docker-compose-elk.yml logs

# Restart services
docker-compose -f docker-compose-elk.yml restart
```

### No Logs in Kibana
```bash
# Check if indices exist
curl http://localhost:9200/_cat/indices?v

# Generate test traffic
for i in {1..50}; do
  curl http://localhost:8000/logs/test
  sleep 1
done

# Wait 30 seconds for processing
```

### High Memory Usage
```bash
# Check resource usage
docker stats

# Reduce Java heap sizes in docker-compose-elk.yml:
# ES_JAVA_OPTS=-Xms256m -Xmx256m
# LS_JAVA_OPTS=-Xms128m -Xmx128m
```

### Container Keeps Restarting
```bash
# Check logs for errors
docker logs <container-name>

# Common fixes:
# 1. Increase vm.max_map_count for Elasticsearch
sudo sysctl -w vm.max_map_count=262144

# 2. Free up disk space
docker system prune -a

# 3. Check port conflicts
sudo netstat -tulpn | grep LISTEN
```

## 🧪 Testing

### Run API Tests
```bash
# Install test dependencies
pip install pytest httpx

# Run tests (create tests/ directory first)
pytest tests/
```

### Load Testing
```bash
# Install Apache Bench
sudo apt-get install apache2-utils

# Run load test
ab -n 1000 -c 10 http://localhost:8000/
```

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Your Name**
- GitHub: [@Omthube23](https://github.com/Omthube23)

## 🙏 Acknowledgments

- FastAPI documentation and community
- Elastic Stack (ELK) team
- Docker community
- All contributors and supporters

## 📞 Support

If you have any questions or issues:
- Review the troubleshooting section

---

**⭐ Star this repository if you find it helpful!**
