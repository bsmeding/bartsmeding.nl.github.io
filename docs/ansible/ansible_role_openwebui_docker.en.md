# Ansible Role: openwebui_docker (`bsmeding.openwebui_docker`)

Deploy Open WebUI (web interface for Ollama) via Docker container

- **GitHub:** [ansible_role_openwebui_docker](https://github.com/bsmeding/ansible_role_openwebui_docker)
- **Ansible Galaxy:** [bsmeding.openwebui_docker](https://galaxy.ansible.com/bsmeding/openwebui_docker)
- **Latest tag:** `none yet`

---

## Quick details
- **Role directory:** `ansible_role_openwebui_docker`
- **Minimum Ansible version:** `2.10`
- **Supported platforms:** Debian, Ubuntu, Fedora, Archlinux
- **Galaxy tags:** openwebui, ollama, llm, ai, webui

---

## Example usage
```yaml
- hosts: all
  become: true
  roles:
    - role: bsmeding.openwebui_docker
```

---

## Notes
This page is generated from role metadata (`meta/main.yml`) and kept in sync with the repository layout.
