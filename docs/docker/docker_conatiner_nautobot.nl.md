# Nautobot in Docker met Ansible

![Nautobot-logo](https://raw.githubusercontent.com/nautobot/nautobot/develop/nautobot/docs/nautobot_logo.svg)


# docker_container_nautobot
Nautobot Docker-container met extra netwerktooling.

Deze container bouwt voort op de upstream Nautobot-base-images; ik heb tooling toegevoegd die in een ge-dockerized Nautobot-omgeving handig is. Veel Nautobot-plugins staan standaard geïnstalleerd—activeer ze in `nautobot_config.py` of gebruik dit image via mijn [Ansible-role voor Nautobot](https://galaxy.ansible.com/ui/standalone/roles/bsmeding/nautobot_docker/).

## OS-pakketten
* net-tools 
* iputils-ping  
* dnsutils

## PIP-pakketten
* ansible-core==2.15.11
* nautobot[napalm]
* nautobot[sso]
* social-auth-core[openidconnect]
* social-auth-core[saml]
* social-auth-core[azuread]
* social-auth-core[google]

# Extra pakketten voor Jobs
* pandas
* xlrd
* openpyxl
* fuzzywuzzy
* python-Levenshtein
* hier-config
* pyntc
* pyats
* scrapli scrapli[ssh2]
* pysnmp


## Nautobot-plugins
* nornir-nautobot
* [nautobot-ssot](https://docs.nautobot.com/projects/ssot/en/latest/)
* [nautobot-plugin-nornir](https://docs.nautobot.com/projects/plugin-nornir/en/latest/)
* [nautobot-golden-config](https://docs.nautobot.com/projects/golden-config/en/latest/)
* [nautobot-device-lifecycle-mgmt](https://docs.nautobot.com/projects/device-lifecycle/en/latest/)
* [nautobot-bgp-models](https://docs.nautobot.com/projects/bgp-models/en/latest/)
* [nautobot-device-onboarding](https://docs.nautobot.com/projects/device-onboarding/en/latest/)
* [nautobot-data-validation-engine]()
* [nautobot-plugin-floorplan](https://docs.nautobot.com/projects/floor-plan/en/latest/)
* [nautobot-firewall-models](https://docs.nautobot.com/projects/firewall-models/en/latest/)
* [todo: chatops](https://docs.nautobot.com/projects/chatops/en/latest/)


# Docker-compose
Voor een werkende omgeving met database en redis: [voorbeeld docker-compose voor Nautobot](https://gist.github.com/bsmeding/d60cf4f23519c75ca2339148d6efd7fe)

# Meer flexibiliteit nodig?
Zie mijn Ansible-role om Nautobot op Docker te deployen: [GitHub](https://github.com/bsmeding/ansible_role_nautobot_docker) of [Ansible Galaxy](https://galaxy.ansible.com/ui/standalone/roles/bsmeding/nautobot_docker/)

Voorbeeld-playbook om Docker en Nautobot in één keer te installeren (defaults).

Eerst de roles installeren:

- `ansible-galaxy role install bsmeding.docker`
- `ansible-galaxy role install bsmeding.nautobot_docker`

Daarna het playbook:

```yaml
---
- name: Install Nautobot
  hosts: [nautobot]
  gather_facts: true
  become: yes
  tasks:
    - name: Check if Docker is installed
      include_role:
        name: bsmeding.docker

    - name: Check if Nautobot is installed
      include_role:
        name: bsmeding.nautobot_docker
```
