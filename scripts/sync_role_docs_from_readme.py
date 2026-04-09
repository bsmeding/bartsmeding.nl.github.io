#!/usr/bin/env python3
"""Generate docs/ansible/*.en.md and *.nl.md from ANSIBLE_ROLES/*/README.md.

Run from any cwd; expects this repo at .../bartsmeding.nl.github.io/ and
ANSIBLE_ROLES as a sibling of the parent folder that contains this repo, e.g.:
  git/WEBSITE_BLOG/bartsmeding.nl.github.io/  (this script)
  git/ANSIBLE_ROLES/                             (role repos)
"""
from __future__ import annotations

from pathlib import Path

SITE_ROOT = Path(__file__).resolve().parents[1]
DOCS_ANSIBLE = SITE_ROOT / "docs" / "ansible"
# bartsmeding.nl.github.io -> WEBSITE_BLOG -> git -> ANSIBLE_ROLES
ANSIBLE_ROLES = SITE_ROOT.parent.parent / "ANSIBLE_ROLES"

# (repo_dir_name, galaxy_slug, en_md_filename)
ROLES: list[tuple[str, str, str]] = [
    ("ansible_role_awx_docker", "awx_docker", "ansible_role_awx_docker.en.md"),
    ("ansible_role_container_lab_docker", "container_lab_docker", "ansible_role_container_lab_docker.en.md"),
    ("ansible_role_docker", "docker", "ansible_role_docker.en.md"),
    ("ansible_role_gitea_runner", "gitea_runner", "ansible_role_gitea_runner.en.md"),
    ("ansible_role_gitlab_ce_docker", "gitlab_docker", "ansible_role_gitlab_ce_docker.en.md"),
    ("ansible_role_install_development_workstation", "install_development_workstation", "ansible_role_install_development_workstation.en.md"),
    ("ansible_role_iptv_analyzer", "iptv_analyzer", "ansible_role_iptv_analyzer.en.md"),
    ("ansible_role_librechat_docker", "librechat_docker", "ansible_role_librechat_docker.en.md"),
    ("ansible_role_nautobot_docker", "nautobot_docker", "ansible_role_nautobot_docker.en.md"),
    ("ansible_role_nginx_docker", "nginx_docker", "ansible_role_nginx_docker.en.md"),
    ("ansible_role_ollama", "ollama", "ansible_role_ollama.en.md"),
    ("ansible_role_openwebui_docker", "openwebui_docker", "ansible_role_openwebui_docker.en.md"),
    ("ansible_role_swag_docker", "swag_docker", "ansible_role_swag_docker.en.md"),
    ("ansible_role_tig_stack_containers", "tig_stack_docker", "ansible_role_tig_stack_containers.en.md"),
    ("ansible-role-webmin", "webmin", "ansible-role-webmin.en.md"),
]


def normalize_readme(raw: str) -> str:
    text = raw.replace("\r\n", "\n")
    lines = text.split("\n")
    if lines and lines[0].strip() == "---":
        lines = lines[1:]
        text = "\n".join(lines).lstrip("\n")
    return text


def strip_first_atx_h1(text: str) -> str:
    """Remove one leading '# title' line so we do not duplicate the page H1."""
    lines = text.split("\n")
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i < len(lines):
        line = lines[i]
        if line.startswith("# ") and not line.startswith("## "):
            del lines[i]
            while i < len(lines) and not lines[i].strip():
                del lines[i]
    return "\n".join(lines).lstrip("\n").rstrip() + "\n"


def header_block(galaxy_slug: str, repo: str) -> str:
    gh = f"https://github.com/bsmeding/{repo}"
    gal = f"https://galaxy.ansible.com/ui/standalone/roles/bsmeding/{galaxy_slug}/"
    return (
        f"# Ansible Role: `bsmeding.{galaxy_slug}`\n\n"
        f"- **GitHub:** [{repo}]({gh})\n"
        f"- **Ansible Galaxy:** [bsmeding.{galaxy_slug}]({gal})\n\n"
        f"The following documentation is taken from the repository **README**.\n\n"
        f"---\n\n"
    )


def nl_prefix() -> str:
    return (
        "_De technische inhoud hieronder is hetzelfde als de Engelse README in de Git-repository._\n\n"
        "---\n\n"
    )


def main() -> None:
    if not ANSIBLE_ROLES.is_dir():
        raise SystemExit(f"ANSIBLE_ROLES not found: {ANSIBLE_ROLES}")

    DOCS_ANSIBLE.mkdir(parents=True, exist_ok=True)

    for repo, galaxy_slug, en_name in ROLES:
        readme = ANSIBLE_ROLES / repo / "README.md"
        if not readme.is_file():
            raise SystemExit(f"Missing README: {readme}")

        body = strip_first_atx_h1(normalize_readme(readme.read_text(encoding="utf-8")))
        en_path = DOCS_ANSIBLE / en_name
        nl_path = DOCS_ANSIBLE / en_name.replace(".en.md", ".nl.md")

        en_content = header_block(galaxy_slug, repo) + body
        en_path.write_text(en_content, encoding="utf-8")

        nl_content = nl_prefix() + en_content
        nl_path.write_text(nl_content, encoding="utf-8")

        print(f"Wrote {en_path.name} + {nl_path.name}")


if __name__ == "__main__":
    main()
