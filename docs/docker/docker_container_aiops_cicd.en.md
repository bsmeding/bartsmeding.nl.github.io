# AIOps CI/CD Docker Images

The `aiops_cicd` images are built for testing AI-assisted operational pipelines, prompt behavior, agent tool calls, structured output, RAG evaluation, and operational replay in CI/CD.

## Image

- Docker Hub: [bsmeding/aiops_cicd_ubuntu](https://hub.docker.com/repository/docker/bsmeding/aiops_cicd_ubuntu/general)
- Source: [docker_containers_aiops_cicd](https://github.com/bsmeding/docker_containers_aiops_cicd)
- Build status: [![Build and Push AIOps Images](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml/badge.svg)](https://github.com/bsmeding/docker_containers_aiops_cicd/actions/workflows/docker.yml)

## Maintained distro tags

| Family | Active tags | Default alias |
| ------ | ----------- | ------------- |
| Ubuntu | `ubuntu2404`, `ubuntu2604` | `ubuntu` -> Ubuntu 26.04 |
| Debian | `debian12`, `debian13` | `debian` -> Debian 13 / Trixie |
| Rocky Linux | `rockylinux8`, `rockylinux9` | `rockylinux` -> Rocky Linux 9 |
| Alpine | `alpine3.22`, `alpine3.23` | `alpine3` -> Alpine 3.23 |

Older tags remain available on Docker Hub but are no longer updated.

## Included tooling

- LLM clients and routers: OpenAI, Anthropic, LiteLLM
- Evaluation frameworks: DeepEval, Ragas
- Agent workflow tooling: LangChain, LangSmith, LangGraph on Python 3.10+ images
- CI and schemas: pytest, pytest-asyncio, pytest-cov, ruff, mypy, Pydantic, JSON Schema, PyYAML, Jinja2
- Replay and mocking: responses, respx, vcrpy, freezegun, faker
- Data and observability: pandas, NumPy, DuckDB, OpenTelemetry SDK, Prometheus API client
- Operational APIs: pynautobot, pynetbox, requests, HTTPX, python-dotenv, structlog

Heavy local ML stacks such as CUDA, PyTorch, TensorFlow, and Transformers are intentionally not included by default.

## Use cases

- Prompt regression testing
- Agent tool-call tests
- Structured JSON output validation
- Incident replay and log/event classification tests
- RAG evaluation and AI recommendation checks
- Mocked Nautobot and NetBox API tests for operational agents

## Usage

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
