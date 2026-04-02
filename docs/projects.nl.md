# Projecten

**bartsmeding IT** publiceert en onderhoudt **open-source-automatisering** (Ansible-roles, Docker-images) die we ook in **klantopdrachten** en **training** gebruiken. Zo blijven voorbeelden eerlijk: wat u hier ziet is dezelfde stack als onder echte randvoorwaarden.

Hieronder een **NetDevOps-georiënteerd overzicht** van uitgelichte opdrachten. Meer achtergrond: **[LinkedIn](https://www.linkedin.com/in/bartsmeding/)**.

De rest van deze pagina blijft uw **plattegrond** naar open assets; volledige overzichten en CI-status staan onder **Ansible-roles & -collections** en **Docker-images** in de navigatie.

---

## Uitgelichte klantwerkzaamheden (NetDevOps)

| | |
|:--:|---|
| ![Centraal Orgaan opvang asielzoekers](images/clients/coa.png){ width="72" } | **Centraal Orgaan opvang asielzoekers (COA)** — **Nautobot**-gedreven automatiseringsframework (HLD/LLD) voor nieuwe locaties, uitfaseren en **brownfield**; **Ansible** met **Tower/AWX** of **GitLab CI/CD** en koppeling naar **Cisco DNA Center**, **Infoblox**, **Panorama** en **SolarWinds**; **7.000+** apparaten, **250+** locaties; driftbeheer, closed-loop change, **NOC**-tests via de UI en **training** van teams. |
| ![LeasePlan](images/clients/leaseplan.png){ width="72" } | **LeasePlan** — Wereldwijde **geautomatiseerde configuratie**, validatie en **auto-remediation** over **on-prem**, **datacenter** en **cloud** met **NetBox**, **Git**, **Itential** en **Ansible**, plus **Linux**-serverlifecycle (**RHEL/CentOS**), agile in sprints geleverd. |
| ![DELTA Fiber](images/clients/delta_fiber.png){ width="72" } | **DELTA Fiber Nederland** — **FTTH**- en **wholesale**-automatisering: **Cisco IOS/XR**-provisioning op templates, **NetBox** → **AWX**, telemetry (**Influx**, **Grafana**), access-laagcontroles en Ansible-patronen voor core, distributie en access—o.a. wholesale-**onboardingprofielen**. |
| ![ProRail](images/clients/prorail.png){ width="72" } | **ProRail** — **Capaciteitsplanning** en **landelijke monitoring**: rapportage, geautomatiseerde drempels op MAN-segmenten en metingen (**SNMP**, **NetFlow**, **NBAR**, **QoS**, vertraging/jitter) op Cisco- en Alcatel-apparatuur, met **SevOne** en ondersteunende tooling. |
| ![YaWorks](images/clients/yaworks.png){ width="72" } | **YaWorks** — Langdurig **netwerkautomatisering**-advies: taakautomatisering, **auto-remediation**, uitrol van **nieuwe sites** en **training**; basis voor o.a. **DELTA Fiber** en **ProRail**. |

---

## Ansible (open source)

- **[Ansible-roles & -collections](ansible_roles_and_collections.md)** — Galaxy-overzicht, CI-badges, downloads en links naar documentatie per role (AWX, Nautobot, GitLab, Docker-host, observability-stacks, enz.).

---

## Docker

- **[Docker-images](docker_images.md)** — **CI/CD-images** rond Ansible (meerdere distro’s, netwerkbibliotheken) en **applicatie-images** (o.a. uitgebreide Nautobot).
- **[Nautobot-containerimage](docker/docker_conatiner_nautobot.md)** — Inhoud van het image en relatie met de Ansible-role.

---

## Schrijven & cursussen (NetDevOps.it)

| Bron | URL |
|------|-----|
| Blog, tutorials, cursussen | [netdevops.it](https://netdevops.it/) |

Diepgaande educatie en community-content blijft op **NetDevOps.it**; **bartsmeding.nl** richt zich op **diensten**, **onderhouden assets** en **contact**.

---

*Meer achtergrond en hoe u ons inschakelt: zie [Over](about.md).*
