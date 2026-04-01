# Ansible Role: gitea_runner (`bsmeding.gitea_runner`)

Gitea ACT Runner running in docker container

- **GitHub:** [ansible_role_gitea_runner](https://github.com/bsmeding/ansible_role_gitea_runner)
- **Ansible Galaxy:** [bsmeding.gitea_runner](https://galaxy.ansible.com/bsmeding/gitea_runner)
- **Latest tag:** `0.1.0`

---

## Quick details
- **Role directory:** `ansible_role_gitea_runner`
- **Minimum Ansible version:** `2.10`
- **Supported platforms:** Fedora, Debian, Ubuntu, Alpine, ArchLinux
- **Galaxy tags:** ci, cd, gitea, actions, runner, docker

---

## Example usage
```yaml
- hosts: all
  become: true
  roles:
    - role: bsmeding.gitea_runner
```

---

## Notes
This page is generated from role metadata (`meta/main.yml`) and kept in sync with the repository layout.
