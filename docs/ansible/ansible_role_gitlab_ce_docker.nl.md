_De technische inhoud hieronder is hetzelfde als de Engelse README in de Git-repository._

---

# Ansible Role: `bsmeding.gitlab_docker`

- **GitHub:** [ansible_role_gitlab_ce_docker](https://github.com/bsmeding/ansible_role_gitlab_ce_docker)
- **Ansible Galaxy:** [bsmeding.gitlab_docker](https://galaxy.ansible.com/ui/standalone/roles/bsmeding/gitlab_docker/)

The following documentation is taken from the repository **README**.

---

This role installs GitLab Community Edition (CE) on a Docker host.

## 🛠️ Features

- Deploy GitLab CE in Docker
- Optional support for:
  - Custom ports
  - SSL (incl. registry certs)
  - LDAP (including Active Directory)
- Optional GitLab Registry
- Custom `gitlab.rb` configuration support
- Simple environment variable configuration

## 🔐 Root Password

If the root password is **not** set via the `GITLAB_ROOT_PASSWORD` environment variable or in `gitlab.rb` (`gitlab_rails['initial_root_password']`), GitLab will auto-generate it.

The auto-generated password can be retrieved (within 24 hours) from:

```
/etc/gitlab/initial_root_password
```

To retrieve:
1. SSH into the host
2. Access the container:
    ```bash
    docker exec -it gitlab /bin/bash
    ```
3. Display the password:
    ```bash
    cat /etc/gitlab/initial_root_password
    ```

## 🔒 Disabling Signup

To manually disable public user signups, refer to the GitLab issue:
📎 [Disable signups](https://gitlab.com/gitlab-org/omnibus-gitlab/-/issues/2837)

## 👥 LDAP Support

LDAP is enabled when both of the following are set:

```yaml
gitlab__ldap_server_host_ip
gitlab__ldap_server_host_port
```

### Common LDAP Variables

| Variable | Description |
|---|---|
| `gitlab__ldap_search_users` | Base DN to search for users |
| `gitlab__ldap_search_groups` | (Not implemented yet) |
| `gitlab__ldap_auth_bind_dn` | Bind DN for the LDAP search |
| `gitlab__ldap_auth_bind_pass` | Bind password |
| `gitlab__ldap_user_filter` | LDAP filter to limit access (e.g., by group) |
| `gitlab__ldap_is_ad` | Set to `true` for Microsoft Active Directory |

### 🧑‍💼 Microsoft Active Directory

When using AD:

- Set `gitlab__ldap_is_ad: true`
- Use the proper `memberOf` OID for filters:
  ```ldif
  (memberOf:1.2.840.113556.1.4.194:=CN=...)
  ```

## ⚙️ gitlab.rb Configuration

By default, the role does **not** overwrite `gitlab.rb` if it already exists. Manual changes will persist across playbook runs unless related variables (like LDAP) are updated.

Custom settings can be injected via `gitlab__gitlab_rb_user_config`.

## 🔐 SSL Support

To enable SSL:

1. Place certificate files in `./files/certs/`
2. Define in your playbook:

```yaml
gitlab__ssl_cert_file: 'git.example.com.crt'
gitlab__ssl_cert_key_file: 'git.example.com.key'
```

To enable registry SSL:

```yaml
gitlab__registery_ssl_cert_file: 'registry.example.com.crt'
gitlab__registery_ssl_cert_key_file: 'registry.example.com.key'
```

### Trusted Root Certificates

To add trusted root CAs, place them in:

```
./files/certs/trusted-certs/
```

These will be copied into the container.

## 📦 Example Playbook

```yaml
---
- name: Install GitLab CE
  hosts: gitlab_hosts
  become: true
  gather_facts: true

  vars:
    gitlab__hostname: git.example.com
    gitlab__env:
      GITLAB_ROOT_PASSWORD: 'pleasechangeme'

  tasks:
    - name: Install Docker
      ansible.builtin.include_role:
        name: bsmeding.docker

    - name: Deploy GitLab
      ansible.builtin.include_role:
        name: bsmeding.gitlab_docker
```

> ⚠️ First-time setup may take 5–10 minutes for GitLab to fully initialize.

## 🧪 TODO

- Test without automatic user generation
- Mount `/etc/passwd` to container for user mapping

## 📄 Available Variables

For a full list of variables and their defaults, see `defaults/main.yml`.
