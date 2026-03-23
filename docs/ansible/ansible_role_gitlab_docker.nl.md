# Ansible-role: GitLab CE Docker (`bsmeding.gitlab_ce_docker`)

Deze Ansible-role deployt GitLab Community Edition in een Docker-container. Geschikt voor labs, demo’s of productie.

- **GitHub:** [bsmeding/ansible_role_gitlab_ce_docker](https://github.com/bsmeding/ansible_role_gitlab_ce_docker)
- **Ansible Galaxy:** [bsmeding.gitlab_ce_docker](https://galaxy.ansible.com/bsmeding/gitlab_ce_docker)

---

## Kenmerken
- GitLab CE in Docker
- Hostname, poorten en SSL instelbaar
- LDAP en registry-ondersteuning
- Persistentie via volumes
- Combineert met Docker, Nginx, SWAG, enz.

---

## Vereisten
- Linux met Docker (role `bsmeding.docker`)
- Python en Ansible

---

## Veelgebruikte variabelen
Zie [role-README](https://github.com/bsmeding/ansible_role_gitlab_ce_docker#role-variables).

```yaml
# Name of the container
gitlab__name: gitlab

# Docker image to use
gitlab__image: 'gitlab/gitlab-ce:latest'

# Hostname and ports
gitlab__hostname: git.example.com
gitlab__port_web_http: 9081
gitlab__port_web_https: 9444
gitlab__port_ssh: 2222

# LDAP integration
gitlab__ldap_server_host_ip: ''
gitlab__ldap_auth_bind_dn: ''
gitlab__ldap_auth_bind_pass: ''

# Volumes to mount
gitlab__directory_volumes:
  - "{{ gitlab__home }}/config:/etc/gitlab"
  - "{{ gitlab__home }}/logs:/var/log/gitlab"
  - "{{ gitlab__home }}/data:/var/opt/gitlab"
```

---

## Voorbeeld-playbook
```yaml
- hosts: all
  become: true
  roles:
    - role: bsmeding.docker
    - role: bsmeding.gitlab_ce_docker
      vars:
        gitlab__hostname: git.example.com
        gitlab__port_web_http: 9081
        gitlab__port_web_https: 9444
        gitlab__port_ssh: 2222
```

---

## Tips
- Gebruik `bsmeding.docker` eerst.
- Zie [role-README](https://github.com/bsmeding/ansible_role_gitlab_ce_docker#role-variables).

---

## Meer informatie
- [GitHub-repository](https://github.com/bsmeding/ansible_role_gitlab_ce_docker)
- [Ansible Galaxy](https://galaxy.ansible.com/bsmeding/gitlab_ce_docker)

---

*MIT-licentie. Bart Smeding.*
