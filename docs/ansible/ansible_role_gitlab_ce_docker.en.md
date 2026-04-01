# Ansible Role: gitlab_docker (`bsmeding.gitlab_docker`)

Manage and run the gitlab ce docker container with Postgres container as backend.

- **GitHub:** [ansible_role_gitlab_ce_docker](https://github.com/bsmeding/ansible_role_gitlab_ce_docker)
- **Ansible Galaxy:** [bsmeding.gitlab_docker](https://galaxy.ansible.com/ui/standalone/roles/bsmeding/gitlab_docker/)

---

## Quick details
- **Role directory:** `ansible_role_gitlab_ce_docker`
- **Minimum Ansible version:** `2.11`
- **Supported platforms:** Ubuntu, Debian
- **Galaxy tags:** gitlab, docker

---

## Example usage
```yaml
- hosts: all
  become: true
  roles:
    - role: bsmeding.gitlab_docker
```

---

## Notes
This page is generated from role metadata (`meta/main.yml`) and kept in sync with the repository layout.
