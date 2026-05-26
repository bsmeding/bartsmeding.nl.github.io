"""
mkdocs-macros definitions for bartsmeding.nl
=============================================

Usage in any Markdown page:
-----------------------------

Single card:
    [[card("Title", price="€39", period="/ month", tagline="...", features=["Feature 1", "Feature 2"]) ]]

Grid of cards (pricing, courses, services, …):
    [[card_grid(
        card("Basic",    price="€39",  period="/ month", features=["..."]),
        card("Pro",      price="€79",  period="/ month", features=["..."], featured=True),
        card("Enterprise", price="€149", period="/ month", features=["..."]),
    ) ]]

Non-pricing card (courses, trainingen, etc.) — omit price/period:
    [[card_grid(
        card("NetDevOps Basics",
            tagline="2-day workshop",
            features=["Ansible fundamentals", "Hands-on labs", "Certificate"],
        ),
        card("NetDevOps Advanced",
            tagline="5-day programme",
            featured=True,
            badge="Most popular",
            features=["CI/CD pipelines", "Nautobot as source of truth"],
        ),
    ) ]]

Parameters:
    title    (str)       Required. Card heading.
    price    (str)       Optional. Price string, e.g. "€39". Omit for non-pricing cards.
    period   (str)       Optional. Period label shown next to price, e.g. "/ month".
    tagline  (str)       Optional. Short subtitle shown below the price.
    features (list[str]) Optional. Bullet-point list. HTML is allowed inside strings.
    featured (bool)      Optional. Highlight this card with accent border. Default False.
    badge    (str)       Optional. Small label badge top-right, e.g. "Most popular".
    cta      (str)       Optional. Call-to-action button label.
    cta_url  (str)       Optional. URL for the CTA button.
"""


def define_env(env):

    @env.macro
    def card(
        title,
        price=None,
        period=None,
        tagline=None,
        features=None,
        featured=False,
        badge=None,
        cta=None,
        cta_url=None,
    ):
        css = "pricing-card pricing-card--featured" if featured else "pricing-card"
        parts = [f'<div class="{css}">']

        if badge:
            parts.append(f'    <span class="card-badge">{badge}</span>')

        parts.append(f"    <h3>{title}</h3>")

        if price is not None:
            period_html = f' <span>{period}</span>' if period else ""
            parts.append(f'    <p class="pricing-price">{price}{period_html}</p>')

        if tagline:
            parts.append(f'    <p class="pricing-tagline">{tagline}</p>')

        if features:
            items = "\n        ".join(f"<li>{f}</li>" for f in features)
            parts.append(f'    <ul class="pricing-features">\n        {items}\n    </ul>')

        if cta and cta_url:
            parts.append(
                f'    <a href="{cta_url}" class="md-button md-button--primary card-cta">{cta}</a>'
            )

        parts.append("</div>")
        return "\n".join(parts)

    @env.macro
    def card_grid(*cards):
        """Wrap card() calls in a responsive CSS grid."""
        inner = "\n".join(cards)
        return f'<div class="pricing-grid">\n{inner}\n</div>'
