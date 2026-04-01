# Ansible-role: container_lab_docker (`bsmeding.container_lab_docker`)

Role to install container_lab in Docker container

- **GitHub:** [ansible_role_container_lab_docker](https://github.com/bsmeding/ansible_role_container_lab_docker)
- **Ansible Galaxy:** [bsmeding.container_lab_docker](https://galaxy.ansible.com/ui/standalone/roles/bsmeding/container_lab_docker/)

---

## Korte details
- **Role-map:** `ansible_role_container_lab_docker`
- **Minimale Ansible-versie:** `2.10`
- **Ondersteunde platformen:** Fedora, Debian, Ubuntu
- **Galaxy-tags:** docker, container_lab

---

## Voorbeeldgebruik
```yaml
- hosts: all
  become: true
  roles:
    - role: bsmeding.container_lab_docker
```

---

## Opmerking
Deze pagina is opgebouwd op basis van role-metadata (`meta/main.yml`) en gelijkgetrokken met de repository-structuur.
