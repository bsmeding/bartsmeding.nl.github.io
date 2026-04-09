# Ansible Role: `bsmeding.openwebui_docker`

- **GitHub:** [ansible_role_openwebui_docker](https://github.com/bsmeding/ansible_role_openwebui_docker)
- **Ansible Galaxy:** [bsmeding.openwebui_docker](https://galaxy.ansible.com/ui/standalone/roles/bsmeding/openwebui_docker/)

The following documentation is taken from the repository **README**.

---

Deploys [Open WebUI](https://docs.openwebui.com/) (web interface for Ollama) via Docker. Requires `bsmeding.docker` role run first.

Source repository: [github.com/bsmeding/ansbile_role_openwebui_docker](https://github.com/bsmeding/ansbile_role_openwebui_docker).

See the [Open WebUI documentation](https://docs.openwebui.com/) for full reference.

## Requirements

- Ollama installed and running (e.g. via `bsmeding.ollama` role)
- Docker (via `bsmeding.docker` role)
- `community.docker` and `community.general` collections

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `openwebui__name` | `open-webui` | Container name. |
| `openwebui__image` | `ghcr.io/open-webui/open-webui:main` | Docker image. |
| `openwebui__home` | `/opt/{{ openwebui__name }}` | Persistent data directory. |
| `openwebui__port` | `8080` | WebUI listen port. |
| `openwebui__ollama_port` | `11434` | Ollama API port (same host). |
| `openwebui__ollama_base_url` | `http://host.docker.internal:{{ openwebui__ollama_port }}` | Ollama backend URL. Override when Ollama is on another host. |
| `openwebui__enable_persistent_config` | `true` | When `false`, env vars override DB on every restart. Use to fix "backend required" if DB has wrong config. |
| `openwebui__auth` | `false` | Require login. Set `true` for multi-user. |
| `openwebui__webui_url` | `""` | Access URL for external access (e.g. `http://192.168.210.38:8080`). |
| `openwebui__cors_allow_origin` | `""` | Semicolon-separated CORS origins. Auto-set from webui_url when set. |
| `openwebui__firewall_allow` | `false` | Allow port in ufw when true. |
| `openwebui__env` | `{}` | Additional env vars (merged last, overrides defaults). |
| `openwebui__remove_existing_container` | `false` | Remove container before create. |
| `openwebui__remove_existing_home_dir` | `false` | **DANGER** Remove data dir (for tests only). |
| `openwebui__gpu` | `false` | When `true`: use `:cuda` image and `--gpus all`. |
| `openwebui__gpu_image` | `ghcr.io/open-webui/open-webui:cuda` | Image used when `openwebui__gpu` is true. |

## Health Check

The Open WebUI Docker image includes a built-in `HEALTHCHECK`. When the container is healthy, `docker ps` shows `(healthy)`. No extra configuration needed.

## GPU Support

For NVIDIA GPU support (e.g. embedding models, hybrid search), set `openwebui__gpu: true`. This will:

- Use the `:cuda` image instead of `:main`
- Pass `--gpus all` to the container

**Requirements:**

- [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html) installed on the host
- Docker Engine on Linux (Docker Desktop on Linux/macOS does not support GPUs)

**Example:**

```yaml
openwebui__gpu: true
```

For custom GPU configuration, override `openwebui__device_requests`. See [community.docker.docker_container](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_container_module.html#parameter-device_requests).

## Adding Backends (Ollama, OpenAI-compatible)

### Ollama (local, same host)

Ollama on the same host is configured by default via `OLLAMA_BASE_URL` → `http://host.docker.internal:11434`. No extra configuration needed if Ollama runs on port 11434.

If you see "Open WebUI Backend required" or "Serve the WebUI from the backend":

1. **Clear browser cache** – This fixes the error in most cases. Hard refresh (Ctrl+Shift+R / Cmd+Shift+R) or clear cache for the site. The frontend may be cached from a previous broken state.
2. **Reset persisted config** – Set `openwebui__enable_persistent_config: false`, then re-run the playbook. Env vars will be read on every start.
3. **Or clear data and recreate** (deletes all data):
   ```yaml
   openwebui__remove_existing_container: true
   openwebui__remove_existing_home_dir: true
   ```

4. **Or configure in Admin UI** – Open WebUI → Admin → Connections → add Ollama with URL `http://host.docker.internal:11434` (or your Ollama URL).

### Ollama on another host

```yaml
openwebui__ollama_base_url: "http://192.168.1.50:11434"
```

### OpenAI-compatible API (OpenAI, vLLM, etc.)

Add via `openwebui__env`:

```yaml
openwebui__env:
  OPENAI_API_BASE: "https://api.openai.com/v1"
  # OPENAI_API_KEY: "sk-..."  # if required
```

Or configure in Admin → Connections after first login.

### Common `openwebui__env` options

| Env var | Description |
|---------|-------------|
| `OLLAMA_BASE_URL` | Ollama backend URL (also set via `openwebui__ollama_base_url`). |
| `OPENAI_API_BASE` | OpenAI-compatible API base URL. |
| `OPENAI_API_KEY` | API key for OpenAI/compatible services. |
| `ENABLE_PERSISTENT_CONFIG` | `false` to always use env vars. |
| `WEBUI_URL` | Set via `openwebui__webui_url`. |
| `HF_TOKEN` | Hugging Face token (higher rate limits). |

See [Open WebUI env configuration](https://docs.openwebui.com/reference/env-configuration/) for the full list.

## Example Playbook

```yaml
- hosts: ollama_servers
  roles:
    - bsmeding.ollama
    - bsmeding.docker
    - bsmeding.openwebui_docker
```

## Example host_vars (Ollama + Open WebUI, external access)

```yaml
# Ollama
ollama__port: 11434
ollama__host: 0.0.0.0

# Open WebUI
openwebui__ollama_port: "11434"
openwebui__webui_url: "http://192.168.210.38:8080"
openwebui__firewall_allow: true
# Fix "backend required" when DB has old config:
# openwebui__enable_persistent_config: false
```

## Troubleshooting

### `no such column: user.profile_banner_image_url` (or similar)

The SQLite database schema is outdated (created by an older Open WebUI). Reset the data to run migrations on a fresh DB:

```yaml
# In host_vars - ONE-TIME reset (deletes all users, chats, settings)
openwebui__remove_existing_container: true
openwebui__remove_existing_home_dir: true
```

Run the playbook once, then set both back to `false`. Or manually on the host:

```bash
docker stop open-webui && docker rm open-webui
rm -rf /opt/open-webui/*
```

Then re-run the playbook (without remove_existing, so it creates a fresh container).

### `GET /api/config HTTP/1.1" 500`

Usually caused by the database schema mismatch above. Same fix: reset data directory.

## License

MIT
