---
title: "Grote woning & thuiswerkkantoor"
tags: ["diensten", "netwerken", "unifi", "smart home", "thuiswerken", "grote woning", "managed services"]
summary: Professioneel beheerde UniFi-netwerken voor grote woningen, zakelijke thuisomgevingen en hybride thuis/zakelijke netwerken.
---

# Grote woning & thuiswerkkantoor

Professioneel beheerde netwerken voor **grote woningen**, **zakelijke thuisomgevingen** en **hybride thuis/zakelijke netwerken** — waar stabiliteit, snelheid en betrouwbaarheid cruciaal zijn. Denk aan meerdere verdiepingen, veel aangesloten apparaten, thuiswerken en zakelijk gebruik vanuit huis.

Wij leveren en beheren **UniFi-infrastructuren** met centrale monitoring, een beveiligde management-VPN en lifecycle-automatisering. Geen consumenten-mesh: **gestandaardiseerde, enterprise-achtige infrastructuur** voor veeleisende woningen en thuiswerkplekken.

Wij hebben **voorkeur voor UniFi**; zakelijke merken (Arista, Juniper, Cisco, …) zijn **in overleg** mogelijk. Door veel te **automatiseren** houden we de beheerkosten laag — dat lukt niet met standaard consumenten-netwerkapparatuur. Hardware leveren is optioneel; zie [dienstenoverzicht](index.md) voor platform, enterprise en hardware.

Alle doorlopende beheer vindt plaats via **remote support** (ticket/e-mail) en een beveiligde managementverbinding.

---

## Voor wie zijn deze pakketten

| Profiel | Typische situatie | Startpunt |
|---------|-------------------|-----------|
| **Grote woning** | Gateway, switches, meerdere AP's, IoT en gast-WiFi | Network Essential |
| **Zakelijk thuis of hybride netwerk** | Meerdere verdiepingen, VLANs, thuiswerk en zakelijk gebruik, veel AP's | Network Professional |
| **Smart home add-on** | Home Assistant in gebruik of gepland | Smart Home Essential of Estate |
| **Volledige stack** | Netwerk + Home Assistant onder één beheerdienst | Connected Home of Connected Estate |

Device-telling omvat gateways, switches en access points in UniFi. Extra apparaten boven het pakket worden apart geoffreerd.

---

## Netwerkpakketten

[[ card_grid(
    card("Network Essential",
        price="€65", period="/ maand",
        tagline="Stabiel beheerd netwerk voor grote moderne woningen.",
        features=[
            "Remote beheer via management VPN",
            "Monitoring van netwerkapparatuur",
            "Configuratie back-ups",
            "Firmware &amp; lifecycle updates",
            "VLAN-segmentatie LAN/gast <em>(max 2 VLAN's — gasten standaard gescheiden)</em>",
            "Ticket support (best effort)",
            "Kleine wijzigingen inbegrepen <em>(fair use, max 30 min/maand)</em>",
            "Tot <strong>10</strong> UniFi devices",
        ]
    ),
    card("Network Professional",
        price="€119", period="/ maand",
        featured=True,
        badge="Meest gekozen",
        tagline="Grote woningen met zakelijk thuisgebruik en hybride netwerken.",
        features=[
            "Alles uit Essential",
            "Uitgebreide VLAN-segmentatie (IoT / werk / gast en meer)",
            "Geavanceerde WiFi-optimalisatie",
            "VPN-beheer en remote access",
            "Prioriteit in support",
            "Uitgebreide remote troubleshooting",
            "Tot <strong>20</strong> UniFi devices",
        ]
    )
) ]]

---

## Smart Home <span class="pricing-optional">(optioneel)</span>

[[ card_grid(
    card("Smart Home Essential",
        price="€39", period="/ maand",
        tagline="Basis Home Assistant — één omgeving, beperkte scope.",
        features=[
            "Alleen <strong>basis Home Assistant</strong> en <strong>basisautomatiseringen</strong>",
            "Geen add-ons, geen HACS of custom integraties",
            "Onderhoud van het systeem, beveiligingsupdates",
            "<strong>Interne</strong> back-ups van de HA-omgeving",
            "Wijzigingen &amp; support <em>(max 1 uur/maand)</em>",
            "Ticket/e-mail support",
        ]
    ),
    card("Smart Home Estate",
        price="€79", period="/ maand",
        tagline="Uitgebreide Home Assistant — add-ons, HACS en complexiteit.",
        features=[
            "Alles uit Essential, plus <strong>add-ons en HACS</strong> (binnen scope)",
            "Complexere automatiseringen, dashboards, multi-zone",
            "Onderhoud van het systeem, beveiligingsupdates",
            "<strong>Interne</strong> back-ups; <strong>externe back-ups</strong> optioneel",
            "Wijzigingen &amp; support <em>(max 2 uur/maand)</em>",
            "Prioriteitsverwerking",
        ]
    )
) ]]

Bij **Essential** beperken we ons tot de standaard Home Assistant-kern en eenvoudige automatiseringen — geen community-add-ons of HACS. **Estate** dekt uitbreidingen en maatwerk binnen de inbegrepen uren; tijd boven het maandmaximum wordt apart geoffreerd.

!!! note "Toegang tot Home Assistant"
    Voor smart home-beheer moet **remote toegang tot Home Assistant** beschikbaar zijn.

    - Neemt u **ook netwerkbeheer** af, dan is toegang doorgaans al ingericht via de **management-VPN**.
    - Alleen **Smart Home** zonder netwerkpakket: toegang wordt bij **eenmalige onboarding** ingericht (indien nog niet aanwezig; apart geoffreerd).

    Veilige toegang op afstand hoort bij de opzet — bijvoorbeeld via **Nabu Casa**, een **eigen VPN**, **Cloudflare Tunnel**, **Tailscale** of vergelijkbaar. Geen open poorten of onbeveiligde exposure naar het internet.

---

## Bundels

Voordeliger dan losse netwerk- en smart home-pakketten.

[[ card_grid(
    card("Connected Home",
        price="€95", period="/ maand",
        tagline="Network Essential + Smart Home Essential",
        features=[
            "Network Essential + Smart Home Essential (basis HA, geen HACS)",
            "Netwerk: kleine wijzigingen <em>(fair use, max 30 min/maand)</em>",
            "HA: wijzigingen <em>(max 1 uur/maand)</em>, interne HA-back-ups",
            "Ticket/e-mail support",
            "Tot <strong>10</strong> UniFi devices",
        ]
    ),
    card("Connected Estate",
        price="€169", period="/ maand",
        featured=True,
        badge="Beste waarde",
        tagline="Network Professional + Smart Home Estate",
        features=[
            "Network Professional + Smart Home Estate (incl. add-ons/HACS)",
            "HA: wijzigingen <em>(max 2 uur/maand)</em>, optionele externe back-ups",
            "Prioriteit support voor netwerk en HA",
            "Tot <strong>20</strong> UniFi devices",
        ]
    )
) ]]

!!! note "Prijzen"
    Maandbedragen zijn **indicatief** voor managed services en sluiten aan bij de scope van grote en veeleisende woningen (aantal devices, segmentatie en supportniveau). **Initieel ontwerp, hardware en werk op locatie** worden apart geoffreerd.

    **Netwerk:** kleine wijzigingen fair use (max 30 min/maand). **Smart Home Essential:** max 1 uur/maand; **Estate:** max 2 uur/maand. Extra tijd is in overleg beschikbaar of bij te kopen.

    Neem contact op via **[Over](../about.md)** voor een offerte op maat.

---

## Niet inbegrepen

Dit is een **beheerde netwerk- en smart home infrastructuurdienst** — geen consumenten IT-support.

Het volgende valt **buiten** de scope van deze pakketten:

- Support voor internetprovider storingen (ISP)
- Eindgebruikersapparaten (laptops, telefoons, printers)
- Windows / macOS ondersteuning
- Consumenten-mesh, ISP-routers en niet-ondersteunde netwerkapparatuur (zakelijke merken in overleg — zie [dienstenoverzicht](index.md))
- Add-ons, HACS en custom integraties onder **Smart Home Essential** (wel inbegrepen bij **Estate**, binnen de uren)
- Maatwerk automation of scripts buiten de pakketuren (projectbasis)
- Ad-hoc "computerhulp" werkzaamheden

---

## Positionering

| Focus | Wat u krijgt |
|-------|----------------|
| **Stabiliteit** | Enterprise UniFi-ontwerp, monitoring en lifecycle-beheer |
| **Performance** | WiFi en segmentatie afgestemd op werk, IoT en gasten |
| **Smart home** | Optioneel Home Assistant-beheer, afgestemd op uw netwerk |

---

[Neem contact op](../about.md){ .md-button .md-button--primary }
