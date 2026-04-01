# Ansible-role: gitlab_docker (`bsmeding.gitlab_docker`)

Manage and run the gitlab ce docker container with Postgres container as backend.

- **GitHub:** [ansible_role_gitlab_ce_docker](https://github.com/bsmeding/ansible_role_gitlab_ce_docker)
- **Ansible Galaxy:** [bsmeding.gitlab_docker](https://galaxy.ansible.com/ui/standalone/roles/bsmeding/gitlab_docker/)

---

## Korte details
- **Role-map:** `ansible_role_gitlab_ce_docker`
- **Minimale Ansible-versie:** `2.11`
- **Ondersteunde platformen:** Ubuntu, Debian
- **Galaxy-tags:** gitlab, docker

---

## Voorbeeldgebruik
```yaml
- hosts: all
  become: true
  roles:
    - role: bsmeding.gitlab_docker
```

---

## Opmerking
Deze pagina is opgebouwd op basis van role-metadata (`meta/main.yml`) en gelijkgetrokken met de repository-structuur.
