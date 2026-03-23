# Ansible-role: Nginx Docker (`bsmeding.nginx_docker`)

Deze Ansible-role deployt Nginx als reverse proxy in een Docker-container. Flexibel inzetbaar als standalone proxy of onderdeel van een grotere stack.

- **GitHub:** [bsmeding/ansible_role_nginx_docker](https://github.com/bsmeding/ansible_role_nginx_docker)
- **Ansible Galaxy:** [bsmeding.nginx_docker](https://galaxy.ansible.com/bsmeding/nginx_docker)

---

## Kenmerken
- Nginx in een Docker-container
- Eigen Nginx-config via templates
- Poorten en volumes instelbaar
- Let’s Encrypt, SSL en eigen certificaten
- Combineert met Docker, SWAG, GitLab, enz.

---

## Vereisten
- Linux met Docker (role `bsmeding.docker`)
- Python en Ansible

---

## Veelgebruikte variabelen
Zie [role-README](https://github.com/bsmeding/ansible_role_nginx_docker#role-variables).

```yaml
# Name of the container
nginx__name: nginx

# Docker image to use
nginx__image: linuxserver/nginx:latest

# Ports to expose
nginx__ports:
  - "80:80"
  - "443:443"

# Volumes to mount
nginx__directory_volumes:
  - "/etc/nginx/conf.d:/etc/nginx/conf.d"
  - "/etc/letsencrypt:/etc/letsencrypt"

# Custom environment variables
nginx__env: {}

# Custom Nginx config template
nginx__config_template: "nginx.conf.j2"
```

---

## Voorbeeld-playbook
```yaml
- hosts: all
  become: true
  roles:
    - role: bsmeding.docker
    - role: bsmeding.nginx_docker
      vars:
        nginx__ports:
          - "80:80"
          - "443:443"
        nginx__directory_volumes:
          - "/etc/nginx/conf.d:/etc/nginx/conf.d"
          - "/etc/letsencrypt:/etc/letsencrypt"
```

---

## Tips
- Gebruik `bsmeding.docker` eerst.
- Pas templates of gemounte config aan voor je omgeving.
- Zie [role-README](https://github.com/bsmeding/ansible_role_nginx_docker#role-variables).

---

## Meer informatie
- [GitHub-repository](https://github.com/bsmeding/ansible_role_nginx_docker)
- [Ansible Galaxy](https://galaxy.ansible.com/bsmeding/nginx_docker)

---

*MIT-licentie. Bart Smeding.*
