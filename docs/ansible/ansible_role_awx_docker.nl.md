# Ansible-role: awx_docker (`bsmeding.awx_docker`)

Role to Install Ansible AWX (opensource Tower) in Docker container

- **GitHub:** [ansible_role_awx_docker](https://github.com/bsmeding/ansible_role_awx_docker)
- **Ansible Galaxy:** [bsmeding.awx_docker](https://galaxy.ansible.com/ui/standalone/roles/bsmeding/awx_docker/)

---

## Korte details
- **Role-map:** `ansible_role_awx_docker`
- **Minimale Ansible-versie:** `2.10`
- **Ondersteunde platformen:** Fedora, Debian, Ubuntu, Alpine, ArchLinux
- **Galaxy-tags:** awx, tower, ansible, docker, awx_version_17

---

## Voorbeeldgebruik
```yaml
- hosts: all
  become: true
  roles:
    - role: bsmeding.awx_docker
```

---

## Opmerking
Deze pagina is opgebouwd op basis van role-metadata (`meta/main.yml`) en gelijkgetrokken met de repository-structuur.
