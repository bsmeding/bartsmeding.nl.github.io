# Ansible-role: iptv_analyzer (`bsmeding.iptv_analyzer`)

Ansible role to install IPTV Analyzer (https://github.com/bsmeding/IPTV-Analyzer) with Ansible. Original made by netoptimizer / Jesper Dangaard Brouer

- **GitHub:** [ansible_role_iptv_analyzer](https://github.com/bsmeding/ansible_role_iptv_analyzer)
- **Ansible Galaxy:** [bsmeding.iptv_analyzer](https://galaxy.ansible.com/ui/standalone/roles/bsmeding/iptv_analyzer/)

---

## Korte details
- **Role-map:** `ansible_role_iptv_analyzer`
- **Minimale Ansible-versie:** `2.9`
- **Ondersteunde platformen:** Debian
- **Galaxy-tags:** iptv, analyzer, multicast, drops, streams, netoptimizer

---

## Voorbeeldgebruik
```yaml
- hosts: all
  become: true
  roles:
    - role: bsmeding.iptv_analyzer
```

---

## Opmerking
Deze pagina is opgebouwd op basis van role-metadata (`meta/main.yml`) en gelijkgetrokken met de repository-structuur.
