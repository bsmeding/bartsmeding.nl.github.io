# Ansible-role: install_development_workstation (`bsmeding.install_development_workstation`)

Set up a development workstation on macOS and Ubuntu with comprehensive development tools

- **GitHub:** [ansible_role_install_development_workstation](https://github.com/bsmeding/ansible_role_install_development_workstation)
- **Ansible Galaxy:** [bsmeding.install_development_workstation](https://galaxy.ansible.com/bsmeding/install_development_workstation)
- **Laatste tag:** `none yet`

---

## Korte details
- **Role-map:** `ansible_role_install_development_workstation`
- **Minimale Ansible-versie:** `2.9`
- **Ondersteunde platformen:** MacOSX, Ubuntu, Debian
- **Galaxy-tags:** development, workstation, macos, ubuntu, docker, python, nodejs, vscode, cursor, homebrew, setup, devops, containers

---

## Voorbeeldgebruik
```yaml
- hosts: all
  become: true
  roles:
    - role: bsmeding.install_development_workstation
```

---

## Opmerking
Deze pagina is opgebouwd op basis van role-metadata (`meta/main.yml`) en gelijkgetrokken met de repository-structuur.
