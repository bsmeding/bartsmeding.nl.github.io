---
authors: [bsmeding]
toc: true
draft: false
date: 2024-03-17
layout: single
comments: true
title: Ansible Role - SWAG
summary: How to use the Ansible role for deploying SWAG (Secure Web Application Gateway) with Docker.
tags: ["ansible", "swag", "docker", "linuxserver"]
---

# Ansible-role: SWAG (Secure Web Application Gateway)

Deze Ansible-role deployt de SWAG-reverse-proxy van [linuxserver.io](https://www.linuxserver.io/) op Linux met Docker.

Repository: [linuxserver/docker-swag](https://github.com/linuxserver/docker-swag)

---

## Wat is SWAG?

SWAG (Secure Web Application Gateway, voorheen letsencrypt) zet Nginx als webserver en reverse proxy op met PHP-ondersteuning en een ingebouwde certbot-client voor automatische SSL-certificaten (Let's Encrypt en ZeroSSL). Inclusief fail2ban.

---

## Certbot-plugins

SWAG levert veel Certbot-plugins mee. Ontbreekt er een, gebruik dan de Universal Package Install Docker Mod:

```yaml
environment:
  DOCKER_MODS: linuxserver/mods:universal-package-install
  INSTALL_PIP_PACKAGES: certbot-dns-<plugin>
```

Zet credentials in `/config/dns-conf/<plugin>.ini`. Test eerst met `STAGING=true`.

---

## Beveiliging en wachtwoordbeveiliging

- SWAG detecteert wijzigingen aan URL’s en subdomeinen, trekt certificaten in en maakt nieuwe bij start.
- Wachtwoordbeveiliging met htpasswd:
  ```bash
  docker exec -it swag htpasswd -c /config/nginx/.htpasswd <username>
  ```
- Extra gebruikers: laat `-c` weg.
- LDAP wordt ondersteund (zie `ldap.conf` en image `linuxserver/ldap-auth`).

---

## Siteconfig en reverse proxy

- Standaard siteconfig: `/config/nginx/site-confs/default.conf`
- Voeg conf-bestanden toe of pas ze aan. Verwijderen van de default laat deze bij containerstart opnieuw aanmaken.
- Voorbeeld reverse-proxy-configs staan in `/config/nginx/proxy_confs`.
- Om je site te verbergen voor zoekmachines:
  ```nginx
  add_header X-Robots-Tag "noindex, nofollow, nosnippet, noarchive";
  ```
- HTTP naar HTTPS: expose poort 80.

---

## Certificaten in andere containers

- Mount de SWAG-configmap in andere containers:
  ```bash
  -v /path-to-swag-config:/swag-ssl
  # Use certs from /swag-ssl/keys/letsencrypt/
  ```
- Of mount alleen `/etc` voor meer security:
  ```bash
  -v /path-to-swag-config/etc:/swag-ssl
  # Use certs from /swag-ssl/letsencrypt/live/<your.domain.url>/
  ```

---

## fail2ban

- SWAG bevat fail2ban met 5 standaard jails.
- Status:
  ```bash
  docker exec -it swag fail2ban-client status
  docker exec -it swag fail2ban-client status <jail name>
  ```
- IP deblokkeren:
  ```bash
  docker exec -it swag fail2ban-client set <jail name> unbanip <IP>
  ```
- Meer: [fail2ban commands](https://www.fail2ban.org/wiki/index.php/Commands).

---

## Configuratie bijwerken

- Wijzigingen staan in de changelog maar worden niet automatisch toegepast.
- Heb je een config aangepast, controleer handmatig of verwijder en herstart de container.
- Proxy-voorbeelden: [reverse-proxy-confs commits](https://github.com/linuxserver/reverse-proxy-confs/commits/master).

---

## Voorbeeld-playbook

Installeert Docker en SWAG met veel defaults. Stel `swag__url` en subdomeinen in naar je eigen domein.

> **Let op:** gebruikt role `bsmeding.docker`. Installeer met `ansible-galaxy role install bsmeding.docker` of installeer Docker handmatig en haal de eerste task weg.

```yaml
---
- name: Install DMZ
  hosts: [dmz]
  gather_facts: true
  become: yes
  vars:
    swag__port_web: 80
    swag__port_ssh: 443
    swag__url: 'example.com'
    swag__subdomains: 'www'
    swag__validation: 'http'
  tasks:
    - name: Check if docker is installed
      ansible.builtin.include_role:
        name: bsmeding.docker

    - name: Check if SWAG is installed
      ansible.builtin.include_role:
        name: bsmeding.docker_swag
```

---

## Subdomein reverse-proxy (voorbeeld)

Templates zijn beschikbaar zodat je geen eigen Nginx-config hoeft te schrijven. Bijvoorbeeld `https://dash.example.com` naar `http://192.168.111.241:9090`:

```yaml
swag__proxy_confs_subdomain:
  - server_name: dash.example.com
    listen: 443
    default_upstream_proto: http
    default_upstream_url: 192.168.1.10
    default_upstream_port: 9090
```

---

## Variabelen

Selectie (volledige lijst in de role):

| Variable                            | Default Value                                       | Description                                                                                           |
|-------------------------------------|-----------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| `swag__name`                        | `swag`                                              | The name of the container.                                                                            |
| `swag__image`                       | `lscr.io/linuxserver/swag`                          | The Docker image to use for SWAG.                                                                     |
| `swag__port_web`                    | `80`                                                | Port for web traffic.                                                                                 |
| `swag__port_ssh`                    | `443`                                               | Port for SSH/SSL traffic.                                                                             |
| `swag__skip_setup`                  | `false`                                             | Set to `true` to disable the setup stage of the SWAG image.                                           |
| `swag__url`                         | `'example.com'`                                     | The base URL for the SWAG setup.                                                                      |
| `swag__subdomains`                  | `'www'`                                             | Subdomains for the SWAG setup.                                                                        |
| `swag__validation`                  | `'http'`                                            | Method of validation (`http` or `dns`).                                                               |
| `swag__certprovider`                | `''` (optional)                                     | Certificate provider (e.g., `zerossl`).                                                               |
| `swag__dnsplugin`                   | `''` (optional)                                     | DNS plugin (e.g., `cloudflare`).                                                                      |
| `swag__cloudflare_global_email`     | `''` (optional)                                     | Cloudflare global email (if using Cloudflare DNS plugin).                                             |
| `swag__cloudflare_global_api`       | `''` (optional)                                     | Cloudflare global API key (if using Cloudflare DNS plugin).                                           |
| `swag__cloudflare_api_token`        | `''` (optional)                                     | Cloudflare API token (if using Cloudflare DNS plugin).                                                |
| `swag__email`                       | `'mail@example.com'`                                | Email for certificate provider notifications.                                                          |
| `swag__only_subdomains`             | `'false'`                                           | Use only subdomains for the SSL certificate.                                                          |
| `swag__extra_domain`                | `''`                                                | Additional domains for the SSL certificate.                                                           |
| `swag__staging`                     | `'true'`                                            | Use staging environment (recommended for testing with Let's Encrypt).                                 |
| `swag__docker_mods`                 | `'linuxserver/mods:swag-cloudflare-real-ip'`        | Docker mods to use with SWAG.                                                                         |
| `swag__remove_existing_container`   | `no`                                                | Remove any existing container before creating a new one.                                              |
| `swag__remove_existing_home_dir`    | `no`                                                | Removes the home directory (for testing purposes only!).                                              |
| `swag__pull_image`                  | `yes`                                               | Pull the Docker image if not already pulled.                                                          |
| `swag__network_mode`                | `'default'`                                         | Network mode for Docker container.                                                                    |
| `swag__network_cidr`                | `'172.16.81.0/26'`                                  | CIDR for network configuration.                                                                       |
| `swag__network`                     | `'proxy'`                                           | Network to connect the container to.                                                                  |
| `swag__container_networks`          | `[{'name': 'bridge'}, {'name': swag__network}]`     | List of networks for the container to join.                                                           |
| `swag__purge_networks`              | `no`                                                | Remove all networks upon container removal.                                                           |
| `swag__log_driver`                  | `'json-file'`                                       | Log driver for Docker.                                                                                |
| `swag__log_options`                 | `{}`                                                | Additional options for the log driver.                                                                |
| `swag__home`                        | `"/opt/{{ swag__name }}"`                           | Home directory for SWAG files.                                                                        |
| `swag__use_local_directories_instead_of_volumes` | `true`                  | Use mapped folders instead of volumes (volumes not set up).                                           |
| `swag__directories`                 | List of directories with paths and permissions      | Directories to create with specific permissions.                                                      |
| `swag__ports`                       | `["{{ swag__port_web }}:80", "{{ swag__port_ssh }}:443"]` | Ports to expose for SWAG container.                                                      |
| `swag__directory_volumes`           | `["{{ swag__home }}/config:/config"]`               | Directory volumes for the container.                                                                  |
| `swag__file_volumes`                | `["/var/run/docker.sock:/var/run/docker.sock:ro"]`  | File volumes for the container.                                                                       |
| `swag__default_env`                 | Various defaults (see below)                        | Default environment variables for the SWAG container.                                                 |
| `swag__env`                         | `{}`                                                | Additional environment variables.                                                                     |
| `swag__proxy_confs_subdomain`       | List of subdomain configuration proxies             | Subdomain proxy configurations for different applications.                                            |

### Standaard omgevingsvariabelen (`swag__default_env`)

- `TZ`: tijdzone (default: `Europe/Paris`).
- `PUID`: User ID for Docker (default: `1040`).
- `PGID`: Group ID for Docker (default: `1001`).
- `URL`: Base URL for SWAG.
- `SUBDOMAINS`: Subdomains to use (default: `www`).
- `VALIDATION`: Validation method (default: `http`).
- `CERTPROVIDER`: Certificate provider (optional).
- `DNSPLUGIN`: DNS plugin (optional).
- `EMAIL`: Email for certificate notifications.
- `ONLY_SUBDOMAINS`: Use only subdomains (default: `false`).
- `EXTRA_DOMAINS`: Extra domains for SSL (optional).
- `STAGING`: Use staging environment for testing (default: `false`).
- `DOCKER_MODS`: Docker mods (optional).
- `CF_ZONE_ID`, `CF_ACCOUNT_ID`, `CF_API_TOKEN`: Cloudflare credentials if using Cloudflare DNS validation.

---

## Proxy-configuratievoorbeelden

In `swag__proxy_confs_subdomain` kun je extra subdomeinen zo configureren:

```yaml
swag__proxy_confs_subdomain:
  - server_name: dash.example.com
    listen: 443
    enable_ldap: false
    enable_authelia: true
    default_upstream_proto: http
    default_upstream_url: dashboard
    default_upstream_port: 9090
  - server_name: app1.example.com
    listen: 443
    enable_ldap: false
    enable_authelia: false
    default_upstream_proto: http
    default_upstream_url: 192.168.1.10
    default_upstream_port: 8080
```
