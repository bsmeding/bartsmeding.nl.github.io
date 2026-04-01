# Ansible Role: librechat_docker (`bsmeding.librechat_docker`)

Deploy LibreChat (ChatGPT-style UI with multi-provider AI) via Docker Compose

- **GitHub:** [ansible_role_librechat_docker](https://github.com/bsmeding/ansible_role_librechat_docker)
- **Ansible Galaxy:** [bsmeding.librechat_docker](https://galaxy.ansible.com/bsmeding/librechat_docker)
- **Latest tag:** `none yet`

---

## Quick details
- **Role directory:** `ansible_role_librechat_docker`
- **Minimum Ansible version:** `2.10`
- **Supported platforms:** Debian, Ubuntu, Fedora, Archlinux
- **Galaxy tags:** librechat, chatgpt, ai, llm, docker, docker-compose

---

## Example usage
```yaml
- hosts: all
  become: true
  roles:
    - role: bsmeding.librechat_docker
```

---

## Notes
This page is generated from role metadata (`meta/main.yml`) and kept in sync with the repository layout.
