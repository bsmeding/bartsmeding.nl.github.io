# Ansible Role: ollama (`bsmeding.ollama`)

Deploy Ollama on Linux (local LLM inference server)

- **GitHub:** [ansible_role_ollama](https://github.com/bsmeding/ansible_role_ollama)
- **Ansible Galaxy:** [bsmeding.ollama](https://galaxy.ansible.com/bsmeding/ollama)
- **Latest tag:** `0.1.0`

---

## Quick details
- **Role directory:** `ansible_role_ollama`
- **Minimum Ansible version:** `2.10`
- **Supported platforms:** Fedora, Debian, Ubuntu, EL
- **Galaxy tags:** ollama, llm, ai, inference

---

## Example usage
```yaml
- hosts: all
  become: true
  roles:
    - role: bsmeding.ollama
```

---

## Notes
This page is generated from role metadata (`meta/main.yml`) and kept in sync with the repository layout.
