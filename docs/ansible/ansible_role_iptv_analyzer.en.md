# Ansible Role: iptv_analyzer (`bsmeding.iptv_analyzer`)

Ansible role to install IPTV Analyzer (https://github.com/bsmeding/IPTV-Analyzer) with Ansible. Original made by netoptimizer / Jesper Dangaard Brouer

- **GitHub:** [ansible_role_iptv_analyzer](https://github.com/bsmeding/ansible_role_iptv_analyzer)
- **Ansible Galaxy:** [bsmeding.iptv_analyzer](https://galaxy.ansible.com/ui/standalone/roles/bsmeding/iptv_analyzer/)

---

## Quick details
- **Role directory:** `ansible_role_iptv_analyzer`
- **Minimum Ansible version:** `2.9`
- **Supported platforms:** Debian
- **Galaxy tags:** iptv, analyzer, multicast, drops, streams, netoptimizer

---

## Example usage
```yaml
- hosts: all
  become: true
  roles:
    - role: bsmeding.iptv_analyzer
```

---

## Notes
This page is generated from role metadata (`meta/main.yml`) and kept in sync with the repository layout.
