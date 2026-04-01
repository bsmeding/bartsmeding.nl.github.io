# Ansible-role: librechat_docker (`bsmeding.librechat_docker`)

Deploy LibreChat (ChatGPT-style UI with multi-provider AI) via Docker Compose

- **GitHub:** [ansible_role_librechat_docker](https://github.com/bsmeding/ansible_role_librechat_docker)
- **Ansible Galaxy:** [bsmeding.librechat_docker](https://galaxy.ansible.com/ui/standalone/roles/bsmeding/librechat_docker/)

---

## Korte details
- **Role-map:** `ansible_role_librechat_docker`
- **Minimale Ansible-versie:** `2.10`
- **Ondersteunde platformen:** Debian, Ubuntu, Fedora, Archlinux
- **Galaxy-tags:** librechat, chatgpt, ai, llm, docker, docker-compose

---

## Voorbeeldgebruik
```yaml
- hosts: all
  become: true
  roles:
    - role: bsmeding.librechat_docker
```

---

## Opmerking
Deze pagina is opgebouwd op basis van role-metadata (`meta/main.yml`) en gelijkgetrokken met de repository-structuur.
