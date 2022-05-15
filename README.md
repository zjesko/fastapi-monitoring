# FastAPI Monitoring

A stack for monitoring FASTapi applications using prometheus and grafana.

## Files
.
├── README.md
├── api                             # fastapi application
│   ├── Dockerfile                  # Dockerfile to build the api
│   ├── main.py                     # main file to run api
│   ├── requirements.txt            # pip requirements for api
│   └── server                      # server files for api
│       ├── crud.py                 # crud to handle db operations
│       ├── database.py             # database config
│       ├── models.py               # sql models
│       └── schemas.py              # pydantic schemas
├── dashboards                      # grafana dashboard configs
│   └── fastapi-dashboard.json      # main fastapi monitoring dashboard
├── datasource.yml                  # prom datasource config for grafana
├── docker-compose.yml              # docker-compose file
├── env.example                     # template for env variables
└── prometheus.yml                  # prometheus config

## Running
```bash
cp env.example .env
docker-compose up -d --build
```

### Endpoints
- FastAPI endpoint: `localhost:8888`
- FastAPI metrics endpoint: `localhost:8888/metrics`
- Prometheus endpoint: `localhost:9090`
- Grafana Endpoint: `localhost: 3000`

Login into grafana using the creds mentioned in the `.env` file and import the dashboards using `dashbords/*.json`


## Credits
Done as part of IS (Independant Study) at SERC IIIT Hyderabad.