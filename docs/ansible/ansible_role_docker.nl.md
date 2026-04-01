# Ansible-role: docker (`bsmeding.docker`)

Docker for Linux, Forked from geerlingguy.docker.

- **GitHub:** [ansible_role_docker](https://github.com/bsmeding/ansible_role_docker)
- **Ansible Galaxy:** [bsmeding.docker](https://galaxy.ansible.com/ui/standalone/roles/bsmeding/docker/)

---

## Korte details
- **Role-map:** `ansible_role_docker`
- **Minimale Ansible-versie:** `2.10`
- **Ondersteunde platformen:** Fedora, Debian, Ubuntu, Alpine, ArchLinux
- **Galaxy-tags:** web, system, containers, docker, orchestration, compose, server

---

## Voorbeeldgebruik
```yaml
- hosts: all
  become: true
  roles:
    - role: bsmeding.docker
```

---

## Opmerking
Deze pagina is opgebouwd op basis van role-metadata (`meta/main.yml`) en gelijkgetrokken met de repository-structuur.
