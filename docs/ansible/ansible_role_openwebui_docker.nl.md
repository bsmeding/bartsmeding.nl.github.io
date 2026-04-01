# Ansible-role: openwebui_docker (`bsmeding.openwebui_docker`)

Deploy Open WebUI (web interface for Ollama) via Docker container

- **GitHub:** [ansible_role_openwebui_docker](https://github.com/bsmeding/ansible_role_openwebui_docker)
- **Ansible Galaxy:** [bsmeding.openwebui_docker](https://galaxy.ansible.com/ui/standalone/roles/bsmeding/openwebui_docker/)

---

## Korte details
- **Role-map:** `ansible_role_openwebui_docker`
- **Minimale Ansible-versie:** `2.10`
- **Ondersteunde platformen:** Debian, Ubuntu, Fedora, Archlinux
- **Galaxy-tags:** openwebui, ollama, llm, ai, webui

---

## Voorbeeldgebruik
```yaml
- hosts: all
  become: true
  roles:
    - role: bsmeding.openwebui_docker
```

---

## Opmerking
Deze pagina is opgebouwd op basis van role-metadata (`meta/main.yml`) en gelijkgetrokken met de repository-structuur.
