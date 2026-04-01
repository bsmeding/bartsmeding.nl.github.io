# Ansible-role: nautobot_docker (`bsmeding.nautobot_docker`)

Role to install Nautobot CMDB in Docker container

- **GitHub:** [ansible_role_nautobot_docker](https://github.com/bsmeding/ansible_role_nautobot_docker)
- **Ansible Galaxy:** [bsmeding.nautobot_docker](https://galaxy.ansible.com/bsmeding/nautobot_docker)
- **Laatste tag:** `1.4.0`

---

## Korte details
- **Role-map:** `ansible_role_nautobot_docker`
- **Minimale Ansible-versie:** `2.10`
- **Ondersteunde platformen:** Fedora, Debian, Ubuntu, Alpine, ArchLinux
- **Galaxy-tags:** nautobot, docker, ssot, ipam, dcim, netdevops

---

## Voorbeeldgebruik
```yaml
- hosts: all
  become: true
  roles:
    - role: bsmeding.nautobot_docker
```

---

## Opmerking
Deze pagina is opgebouwd op basis van role-metadata (`meta/main.yml`) en gelijkgetrokken met de repository-structuur.
