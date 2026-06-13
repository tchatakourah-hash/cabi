"""
Mapping des emojis vers des icônes Lucide (https://lucide.dev) et helper
pour générer des icônes SVG inline professionnelles, en remplacement
des emojis Unicode (📊, 🌱, etc.).
"""

# Mapping emoji -> nom d'icône Lucide
EMOJI_TO_LUCIDE = {
    "📊": "bar-chart-3",
    "📈": "trending-up",
    "🌱": "sprout",
    "🌾": "wheat",
    "🌍": "globe",
    "🌐": "globe-2",
    "🎓": "graduation-cap",
    "🎯": "target",
    "💎": "gem",
    "👤": "user",
    "💡": "lightbulb",
    "💬": "message-circle",
    "💻": "laptop",
    "📂": "folder-open",
    "📄": "file-text",
    "📅": "calendar",
    "📌": "pin",
    "📍": "map-pin",
    "📑": "clipboard-list",
    "📘": "book-open",
    "📝": "edit-3",
    "📞": "phone",
    "📧": "mail",
    "📨": "send",
    "📰": "newspaper",
    "📹": "video",
    "🔄": "refresh-cw",
    "🔍": "search",
    "🗺": "map",
    "🚀": "rocket",
    "🤝": "handshake",
    "🧠": "brain",
    "🧭": "compass",
    "🧹": "brush",
    "🎁": "gift",
    "☎": "phone-call",
    "⚠": "alert-triangle",
    "✔": "check",
}

# Source CDN pour la bibliothèque Lucide (chargée une seule fois)
LUCIDE_CDN_SCRIPT = """
<script src="https://unpkg.com/lucide@latest/dist/umd/lucide.js"></script>
<script>
  if (window.lucide) { window.lucide.createIcons(); }
</script>
"""


def icon_html(emoji: str, size: int = 18, color: str = "currentColor", extra_class: str = "") -> str:
    """
    Retourne le HTML d'une icône Lucide correspondant à l'emoji donné.
    Si l'emoji n'a pas de correspondance, il est renvoyé tel quel (fallback).
    """
    name = EMOJI_TO_LUCIDE.get(emoji)
    if not name:
        return emoji
    return (
        f'<i data-lucide="{name}" '
        f'style="width:{size}px;height:{size}px;vertical-align:-3px;'
        f'stroke:{color};" class="{extra_class}"></i>'
    )


def replace_emojis_with_icons(text: str, size: int = 18, color: str = "currentColor") -> str:
    """
    Remplace toutes les occurrences d'emojis connus dans `text` par des
    icônes Lucide inline. Utile pour les titres/descriptions contenant
    un emoji en préfixe.
    """
    result = text
    for emoji, name in EMOJI_TO_LUCIDE.items():
        if emoji in result:
            result = result.replace(
                emoji,
                f'<i data-lucide="{name}" '
                f'style="width:{size}px;height:{size}px;vertical-align:-3px;'
                f'stroke:{color};"></i>'
            )
    return result
