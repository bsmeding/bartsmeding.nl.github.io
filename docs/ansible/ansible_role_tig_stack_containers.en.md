# Ansible Role: tig_stack_docker (`bsmeding.tig_stack_docker`)

Ansible Role to install Telegraf, InfluxDB and Grafana (TIG) as docker containers

- **GitHub:** [ansible_role_tig_stack_containers](https://github.com/bsmeding/ansible_role_tig_stack_containers)
- **Ansible Galaxy:** [bsmeding.tig_stack_docker](https://galaxy.ansible.com/bsmeding/tig_stack_docker)
- **Latest tag:** `none yet`

---

## Quick details
- **Role directory:** `ansible_role_tig_stack_containers`
- **Minimum Ansible version:** `2.9`
- **Supported platforms:** Debian, Ubuntu
- **Galaxy tags:** system, telegraf, influxdb, grafana, monitoring, snmp

---

## Example usage
```yaml
- hosts: all
  become: true
  roles:
    - role: bsmeding.tig_stack_docker
```

---

## Notes
This page is generated from role metadata (`meta/main.yml`) and kept in sync with the repository layout.
