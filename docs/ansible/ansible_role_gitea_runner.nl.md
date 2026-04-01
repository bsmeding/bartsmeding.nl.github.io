# Ansible-role: gitea_runner (`bsmeding.gitea_runner`)

Gitea ACT Runner running in docker container

- **GitHub:** [ansible_role_gitea_runner](https://github.com/bsmeding/ansible_role_gitea_runner)
- **Ansible Galaxy:** [bsmeding.gitea_runner](https://galaxy.ansible.com/ui/standalone/roles/bsmeding/gitea_runner/)

---

## Korte details
- **Role-map:** `ansible_role_gitea_runner`
- **Minimale Ansible-versie:** `2.10`
- **Ondersteunde platformen:** Fedora, Debian, Ubuntu, Alpine, ArchLinux
- **Galaxy-tags:** ci, cd, gitea, actions, runner, docker

---

## Voorbeeldgebruik
```yaml
- hosts: all
  become: true
  roles:
    - role: bsmeding.gitea_runner
```

---

## Opmerking
Deze pagina is opgebouwd op basis van role-metadata (`meta/main.yml`) en gelijkgetrokken met de repository-structuur.
