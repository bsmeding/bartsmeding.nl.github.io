# Ansible-role: tickg_stack_docker (`bsmeding.tickg_stack_docker`)

Ansible Role to install Telegraf, InfluxDB, Chronograf, Kapacitor and Grafana (TICK+G) as docker containers

- **GitHub:** [ansible_role_tickg_stack_containers](https://github.com/bsmeding/ansible_role_tickg_stack_containers)
- **Ansible Galaxy:** [bsmeding.tickg_stack_docker](https://galaxy.ansible.com/bsmeding/tickg_stack_docker)
- **Laatste tag:** `none yet`

---

## Korte details
- **Role-map:** `ansible_role_tickg_stack_containers`
- **Minimale Ansible-versie:** `2.9`
- **Ondersteunde platformen:** Debian, Ubuntu
- **Galaxy-tags:** system, telegraf, influxdb, kapacitor, chronograf, grafana, monitoring, snmp

---

## Voorbeeldgebruik
```yaml
- hosts: all
  become: true
  roles:
    - role: bsmeding.tickg_stack_docker
```

---

## Opmerking
Deze pagina is opgebouwd op basis van role-metadata (`meta/main.yml`) en gelijkgetrokken met de repository-structuur.
