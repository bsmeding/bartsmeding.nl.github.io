# Ansible Role: `bsmeding.gitea_runner`

- **GitHub:** [ansible_role_gitea_runner](https://github.com/bsmeding/ansible_role_gitea_runner)
- **Ansible Galaxy:** [bsmeding.gitea_runner](https://galaxy.ansible.com/ui/standalone/roles/bsmeding/gitea_runner/)

The following documentation is taken from the repository **README**.

---

This role sets up the [Gitea ACT Runner](https://gitea.com/gitea/act_runner) container using Ansible. ACT Runner is a runner for Gitea Actions, compatible with GitHub Actions workflows.

## Requirements

- Docker must be installed on the target host (see Ansible role [bsmeding.docker](https://galaxy.ansible.com/ui/standalone/roles/bsmeding/docker/)).
- `community.docker` Ansible collection.

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

### Container Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `gitea_runner__name` | `gitea_runner` | Name of the container. |
| `gitea_runner__image` | `gitea/act_runner:latest` | Docker image to use. |
| `gitea_runner__pull_image` | `true` | Pull the image before creating the container. |
| `gitea_runner__network` | `proxy` | Name of the Docker network for the runner. |
| `gitea_runner__network_cidr` | `''` | CIDR for the runner network (optional). |
| `gitea_runner__network_mode` | `default` | Docker network mode (`default`, `bridge`, `host`, etc.). |
| `gitea_runner__home` | `/opt/{{ gitea_runner__name }}` | Host directory for persistent data. |
| `gitea_runner__skip_setup` | `false` | Disable setup stage of the role. |

### Gitea ACT Runner Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `gitea_runner__gitea_url` | `''` | **Required**: Gitea instance URL (e.g., `https://gitea.example.com`). |
| `gitea_runner__gitea_token` | `''` | **Required**: Registration token from Gitea (Settings → Actions → Runners → New Runner). |
| `gitea_runner__runner_name` | `{{ gitea_runner__name }}` | Name of the runner as it appears in Gitea. |
| `gitea_runner__runner_labels` | `[]` | List of labels for the runner (e.g., `['ubuntu-latest', 'docker']`). |
| `gitea_runner__runner_capacity` | `1` | Number of concurrent jobs the runner can handle. |
| `gitea_runner__log_level` | `info` | Log level (`debug`, `info`, `warn`, `error`). |

### Advanced Configuration

- `gitea_runner__default_env`: Default environment variables (PUID/PGID, TZ, etc.).
- `gitea_runner__env`: Custom environment variables to merge/override.
- `docker_uid`: UID for the user inside the container (default: 1040).
- `docker_gid`: GID for the group inside the container (default: 1001).

## Getting a Registration Token

1. Log in to your Gitea instance.
2. Go to **Settings** → **Actions** → **Runners**.
3. Click **New Runner**.
4. Copy the registration token.
5. Set `gitea_runner__gitea_token` in your playbook or host vars.

## Example Playbook

```yaml
- hosts: servers
  roles:
    - role: bsmeding.gitea_runner
      vars:
        gitea_runner__gitea_url: "https://gitea.example.com"
        gitea_runner__gitea_token: "your_registration_token_here"
        gitea_runner__runner_name: "my-runner"
        gitea_runner__runner_labels:
          - ubuntu-latest
          - docker
          - self-hosted
        gitea_runner__runner_capacity: 2
        gitea_runner__network: "proxy"
```

## Network Configuration

The runner needs access to Docker socket (`/var/run/docker.sock`) to run jobs. This is automatically configured via `gitea_runner__file_volumes`.

### Using Custom Networks

```yaml
gitea_runner__network_mode: 'default'
gitea_runner__container_networks:
  - name: bridge
  - name: proxy
```

### Using Network Mode

```yaml
gitea_runner__network_mode: 'host'
```

## License

MIT

## Author Information

This role was created by Bart Smeding.
