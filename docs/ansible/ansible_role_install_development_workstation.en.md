# Ansible Role: install_development_workstation (`bsmeding.install_development_workstation`)

Set up a development workstation on macOS and Ubuntu with comprehensive development tools

- **GitHub:** [ansible_role_install_development_workstation](https://github.com/bsmeding/ansible_role_install_development_workstation)
- **Ansible Galaxy:** [bsmeding.install_development_workstation](https://galaxy.ansible.com/ui/standalone/roles/bsmeding/install_development_workstation/)

---

## Quick details
- **Role directory:** `ansible_role_install_development_workstation`
- **Minimum Ansible version:** `2.9`
- **Supported platforms:** MacOSX, Ubuntu, Debian
- **Galaxy tags:** development, workstation, macos, ubuntu, docker, python, nodejs, vscode, cursor, homebrew, setup, devops, containers

---

## Example usage
```yaml
- hosts: all
  become: true
  roles:
    - role: bsmeding.install_development_workstation
```

---

## Notes
This page is generated from role metadata (`meta/main.yml`) and kept in sync with the repository layout.
