# Ansible-role: ollama (`bsmeding.ollama`)

Deploy Ollama on Linux (local LLM inference server)

- **GitHub:** [ansible_role_ollama](https://github.com/bsmeding/ansible_role_ollama)
- **Ansible Galaxy:** [bsmeding.ollama](https://galaxy.ansible.com/bsmeding/ollama)
- **Laatste tag:** `0.1.0`

---

## Korte details
- **Role-map:** `ansible_role_ollama`
- **Minimale Ansible-versie:** `2.10`
- **Ondersteunde platformen:** Fedora, Debian, Ubuntu, EL
- **Galaxy-tags:** ollama, llm, ai, inference

---

## Voorbeeldgebruik
```yaml
- hosts: all
  become: true
  roles:
    - role: bsmeding.ollama
```

---

## Opmerking
Deze pagina is opgebouwd op basis van role-metadata (`meta/main.yml`) en gelijkgetrokken met de repository-structuur.
