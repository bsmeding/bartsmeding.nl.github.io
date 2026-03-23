# AI in netwerken: van inzicht naar actie

Kunstmatige intelligentie (AI) verandert netwerken snel. Wat vroeger teams engineers kostte—logs doorspitten, scripts draaien, configuraties nalopen—kan nu worden versneld, verrijkt of zelfs door AI-agents worden overgenomen.

Dit artikel beschrijft de rol van AI in netwerken, hoe systemen zoals [Nautobot](https://nautobot.com/) (als CMDB en automatiseringsplatform) daarbij passen, en wat je nodig hebt om agents te bouwen die netwerkdata bevragen en met echte devices praten.

---

## 🤖 Wat kan AI in netwerken?

Op hoofdlijnen past AI hier:

- **Observability & monitoring**: afwijkingen in verkeer, voorspellende analyses, inzicht uit logs en metrics.
- **Intent verification**: continu controleren of het netwerk zich gedraagt volgens beleid.
- **Natuurlijke taal**: vragen als *“Welke switches op locatie A draaien verouderde firmware?”*
- **Gedetailleerde troubleshooting**: agents die diagnostiek draaien en resultaten samenvatten.
- **Configuratie**: op basis van input of geleerd gedrag veilig configuraties voorstellen of toepassen.

---

## 🔗 Samenwerken met Nautobot (CMDB)

[Nautobot](https://github.com/nautobot/nautobot) is een krachtige source of truth. Met API en plugins is het een logische partner voor AI-gestuurde systemen.

### Use case: AI-agent die Nautobot bevraagt

Een conversationele agent zou kunnen antwoorden op:

- “Geef alle devices op site **Berlijn**.”
- “Welke devices zijn de laatste 24 uur niet gebackupt?”
- “Zijn er devices met end-of-support binnen 6 maanden?”

#### Hoe het werkt

1. **Natural language parsing**: het model herkent intent en entiteiten (site, device type, enz.).
2. **Nautobot API**: vertaling naar GraphQL of REST.
3. **Antwoord**: leesbare output, eventueel met links naar de Nautobot UI.

> **Tip:** met **Nautobot ChatOps** kan AI ook via Slack of Microsoft Teams werken.

---

## ⚙️ Praten met netwerkdevices

Nautobot beschrijft **wat hoort**; devices tonen **wat er is**.

AI kan via SSH, NETCONF of REST o.a.:

- Softwareversies controleren
- Interface-status uitlezen
- BGP-buren bekijken
- Configfragmenten verzamelen

### Use case: device-inspectie

Een agent kan bijvoorbeeld:

- Via SSH op een switch inloggen
- Commando’s als `show version` of `show interface status` uitvoeren
- Output vergelijken met de bedoelde staat in Nautobot
- Afwijkingen markeren of acties voorstellen

### Tooling

- **NAPALM**: multi-vendor abstractie om devices uit te lezen
- **Scrapli**: flexibele Python-library voor CLI
- **Netmiko / Paramiko**: SSH op lager niveau

> **Tip:** herbruikbare prompt-templates per device type of vendor.

---

## 🧠 AI-agents voor netwerken bouwen

### Architectuur (globaal)

1. **Frontend** (optioneel): chatbot of web-UI
2. **LLM**: GPT-4, Claude, of open-source modellen
3. **Tools/plugins**: functies die APIs aanroepen of naar devices verbinden
4. **Geheugen** (optioneel): eerdere interacties, veelgestelde queries, snapshots

### Frameworks

- **LangChain / LlamaIndex**: agents met tools en geheugen
- **Semantic Kernel**: .NET / C#
- **AutoGen**: multi-agent samenwerking (Microsoft)

---

## 🛠 Voorbeeldprompts

```text
> Welke devices zitten in site "NYC-Core"?
→ [agent roept Nautobot GraphQL aan]

> Log in op router R1 en check of interface Gi0/1 up is.
→ [agent gebruikt Scrapli om te verbinden en te parsen]

> Samenvatting van alle devices met CVE’s in de laatste 90 dagen.
→ [agent bevraagt Nautobot Software Inventory + CVE-plugins]

```
Zie het [YouTube-kanaal van John Capobianco](https://www.youtube.com/@johncapobianco2527) voor voorbeelden van AI-agents op netwerkdevices.

---

## 🔒 Security

AI geeft kracht, maar ook risico:

- Geef een LLM geen onbeperkte shell
- Strikte function calling met duidelijke rechten
- Valideer input en output bij device-interactie

---

## 🧩 Slotwoord

AI in netwerken gaat niet over engineers vervangen, maar over **hun werk versterken**. Door natuurlijke taal, gestructureerde API’s (zoals Nautobot) en veilige device-communicatie te combineren, kun je agents bouwen die vragen beantwoorden, issues signaleren en soms actie ondernemen.

De toekomst is er al—experimenteer ermee.

---

## 📚 Meer lezen
- [John Capobianco op YouTube](https://www.youtube.com/@johncapobianco2527)
- [Nautobot-documentatie](https://docs.nautobot.com/)
- [LangChain (Python)](https://python.langchain.com/)
- [NAPALM](https://github.com/napalm-automation/napalm)
- [Scrapli](https://github.com/carlmontanari/scrapli)
- [OpenAI Function Calling](https://platform.openai.com/docs/guides/function-calling)
