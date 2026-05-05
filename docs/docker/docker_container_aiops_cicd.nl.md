# AIOps CI/CD Docker-images

De `aiops_cicd` images zijn bedoeld voor het testen van AI-ondersteunde operationele pipelines, promptgedrag, agent tool-calls, gestructureerde output, RAG-evaluatie en operationele replay in CI/CD.

## Image

- Docker Hub: [bsmeding/aiops_cicd_ubuntu](https://hub.docker.com/repository/docker/bsmeding/aiops_cicd_ubuntu/general)
- Source: [docker_containers_aiops_cicd](https://github.com/bsmeding/docker_containers_aiops_cicd)
- Buildstatus: [![Build and Push AIOps Images](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml)

## Onderhouden distro-tags

| Familie | Actieve tags | Default alias |
| ------- | ------------ | ------------- |
| Ubuntu | `ubuntu2404`, `ubuntu2604` | `ubuntu` -> Ubuntu 26.04 |
| Debian | `debian12`, `debian13` | `debian` -> Debian 13 / Trixie |
| Rocky Linux | `rockylinux8`, `rockylinux9` | `rockylinux` -> Rocky Linux 9 |
| Alpine | `alpine3.22`, `alpine3.23` | `alpine3` -> Alpine 3.23 |

Oudere tags blijven beschikbaar op Docker Hub maar worden niet meer bijgewerkt.

## Meegeleverde tooling

- LLM-clients en routers: OpenAI, Anthropic, LiteLLM
- Evaluatieframeworks: DeepEval, Ragas
- Agent workflow tooling: LangChain, LangSmith, LangGraph op Python 3.10+-images
- CI en schema's: pytest, pytest-asyncio, pytest-cov, ruff, mypy, Pydantic, JSON Schema, PyYAML, Jinja2
- Replay en mocking: responses, respx, vcrpy, freezegun, faker
- Data en observability: pandas, NumPy, DuckDB, OpenTelemetry SDK, Prometheus API client
- Operationele API's: pynautobot, pynetbox, requests, HTTPX, python-dotenv, structlog

Zware lokale ML-stacks zoals CUDA, PyTorch, TensorFlow en Transformers zijn bewust niet standaard opgenomen.

## Toepassingen

- Prompt-regressietests
- Agent tool-call tests
- Gestructureerde JSON-outputvalidatie
- Incident replay en log-/eventclassificatietests
- RAG-evaluatie en controles op AI-aanbevelingen
- Gemockte Nautobot- en NetBox-API-tests voor operationele agents

## Gebruik

```yaml
jobs:
  eval:
    runs-on: ubuntu-latest
    container:
      image: bsmeding/aiops_cicd_ubuntu:latest
    steps:
      - uses: actions/checkout@v5
      - run: pytest tests/aiops/
      - run: pytest tests/evals/
```
