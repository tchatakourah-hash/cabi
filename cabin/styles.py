"""
Feuille de style améliorée — KOURA AgriData Impact
Inspirée de kapiconsult.tg + sowing.eu
"""

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Playfair+Display:wght@700;800&display=swap');

:root {
    --green-dark: #0D4A1F;
    --green-mid:  #1E7A3C;
    --green-light:#2ECC71;
    --blue-accent:#1A6FA8;
    --gold:       #E8A020;
    --cream:      #F9F6F0;
    --white:      #FFFFFF;
    --text-dark:  #1A2332;
    --text-mid:   #3D5A47;
    --text-light: #6B7C75;
    --border:     rgba(30,122,60,0.15);
    --shadow-sm:  0 2px 12px rgba(13,74,31,0.08);
    --shadow-md:  0 8px 32px rgba(13,74,31,0.12);
    --shadow-lg:  0 20px 60px rgba(13,74,31,0.18);
    --gradient:   linear-gradient(135deg, #0D4A1F 0%, #1A6FA8 100%);
    --gradient-gold: linear-gradient(135deg, #E8A020 0%, #F4C842 100%);
    --radius:     12px;
}

html, body, [class*="st"] { font-family: 'Inter', sans-serif; }

/* ── Streamlit nettoyage ── */
#MainMenu, header, footer, .stDeployButton { visibility: hidden !important; display: none !important; }
.block-container { padding-top: 0 !important; padding-bottom: 0 !important; max-width: 100% !important; }
.element-container { margin-bottom: 0 !important; }
.stMarkdown { margin-bottom: 0 !important; }
body { padding-top: 0 !important; background: var(--cream); }

/* ══════════════════════════════════════════════════
   BARRE DE NAVIGATION
══════════════════════════════════════════════════ */
.topnav {
    position: fixed; top: 0; left: 0; width: 100vw; z-index: 9999;
    background: rgba(13,74,31,0.97);
    backdrop-filter: blur(12px);
    height: 64px;
    display: flex; align-items: center; justify-content: space-between;
    padding: 0 2.5rem;
    box-shadow: 0 2px 24px rgba(0,0,0,0.2);
    border-bottom: 2px solid rgba(232,160,32,0.3);
}
.topnav-brand {
    font-family: 'Playfair Display', serif;
    color: white; font-weight: 800; font-size: 1.05rem;
    white-space: nowrap; letter-spacing: 0.3px;
    display: flex; align-items: center; gap: 0.6rem;
}
.topnav-brand span { color: var(--gold); }
.topnav-links {
    display: flex; align-items: center; gap: 2rem;
}
.topnav-links a {
    color: rgba(255,255,255,0.85); font-size: 0.82rem; font-weight: 500;
    text-decoration: none; white-space: nowrap;
    transition: color 0.2s;
    letter-spacing: 0.3px;
}
.topnav-links a:hover { color: var(--gold); }
.topnav-links a.active { color: var(--gold); font-weight: 700; }
.topnav-cta {
    background: var(--gradient-gold);
    color: var(--green-dark) !important;
    padding: 8px 20px; border-radius: 8px;
    font-weight: 700 !important; font-size: 0.78rem !important;
    text-decoration: none;
    box-shadow: 0 4px 14px rgba(232,160,32,0.4);
    transition: transform 0.2s, box-shadow 0.2s;
}
.topnav-cta:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(232,160,32,0.55) !important; }
.nav-spacer { height: 64px; }

/* ══════════════════════════════════════════════════
   BANDEAU LOGO / DATE
══════════════════════════════════════════════════ */
.logobar {
    background: white;
    padding: 0 3rem;
    height: 120px;
    display: flex; align-items: center; justify-content: space-between;
    border-bottom: 3px solid var(--green-mid);
    box-shadow: var(--shadow-sm);
}
.logobar img { height: 90px; width: auto; object-fit: contain; }
.logobar-date {
    text-align: center;
    color: var(--green-dark);
    font-weight: 600; font-size: 0.95rem;
    letter-spacing: 0.4px;
}

/* ══════════════════════════════════════════════════
   BANDEAU DÉFILANT EXPERTISES (style kapiconsult)
══════════════════════════════════════════════════ */
.ticker-wrap {
    background: var(--green-dark);
    overflow: hidden; white-space: nowrap;
    padding: 10px 0; border-bottom: 3px solid var(--gold);
}
.ticker-content {
    display: inline-block;
    animation: ticker-move 40s linear infinite;
    font-size: 0.82rem; font-weight: 600; letter-spacing: 1.5px;
    text-transform: uppercase; color: rgba(255,255,255,0.85);
}
.ticker-content span.sep { color: var(--gold); margin: 0 1.5rem; }
@keyframes ticker-move { from { transform: translateX(0); } to { transform: translateX(-50%); } }

/* ══════════════════════════════════════════════════
   HERO VIDEO
══════════════════════════════════════════════════ */
.hero-wrap {
    position: relative; width: 100%; height: 580px;
    overflow: hidden;
}
.hero-wrap video {
    position: absolute; top: 50%; left: 50%;
    min-width: 100%; min-height: 100%;
    width: auto; height: auto;
    transform: translate(-50%,-50%);
    filter: brightness(0.35) saturate(0.8);
    z-index: 0;
}
.hero-overlay {
    position: relative; z-index: 1;
    height: 580px;
    display: flex; flex-direction: column;
    justify-content: center; align-items: center;
    text-align: center; padding: 2rem;
    color: white;
}
.hero-eyebrow {
    background: rgba(232,160,32,0.15);
    border: 1px solid rgba(232,160,32,0.5);
    color: var(--gold);
    font-size: 0.75rem; font-weight: 700; letter-spacing: 2.5px;
    text-transform: uppercase;
    padding: 6px 18px; border-radius: 50px;
    margin-bottom: 1.2rem;
}
.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 3.4rem; font-weight: 800; line-height: 1.15;
    margin-bottom: 1rem;
    text-shadow: 0 2px 20px rgba(0,0,0,0.5);
}
.hero-title em { color: var(--gold); font-style: normal; }
.hero-slogan {
    font-size: 1.1rem; font-weight: 400; opacity: 0.9;
    max-width: 600px; line-height: 1.65;
    margin-bottom: 2rem;
}
.hero-graphs {
    display: flex; gap: 1.2rem; margin-bottom: 2rem;
}
.hero-graph-box {
    border: 1.5px solid rgba(0,217,255,0.4);
    background: rgba(0,0,0,0.3);
    backdrop-filter: blur(6px);
    border-radius: 12px; padding: 0.9rem 1rem;
    width: 220px; height: 160px;
    display: flex; flex-direction: column; justify-content: space-between;
    cursor: pointer; text-decoration: none;
    transition: all 0.25s;
}
.hero-graph-box:hover { border-color: #00D9FF; box-shadow: 0 0 20px rgba(0,217,255,0.5); transform: translateY(-3px); }
.hero-graph-label {
    font-size: 0.72rem; font-weight: 700; letter-spacing: 1.5px;
    text-transform: uppercase; color: #00D9FF; margin-top: 0.4rem;
}
.hero-btn {
    background: transparent;
    color: var(--gold); border: 2px solid var(--gold);
    padding: 14px 36px; border-radius: 10px;
    font-weight: 700; font-size: 0.95rem; cursor: pointer;
    transition: all 0.25s; font-family: 'Inter', sans-serif;
    text-decoration: none; display: inline-block;
    box-shadow: 0 0 20px rgba(232,160,32,0.2);
}
.hero-btn:hover { background: var(--gold); color: var(--green-dark); box-shadow: 0 0 30px rgba(232,160,32,0.6); }

/* ══════════════════════════════════════════════════
   COMPTEURS (style kapiconsult)
══════════════════════════════════════════════════ */
.kpi-bar {
    background: white;
    display: flex; justify-content: center; gap: 0;
    border-bottom: 2px solid var(--border);
    box-shadow: var(--shadow-sm);
}
.kpi-item {
    flex: 1; max-width: 240px;
    text-align: center;
    padding: 2.2rem 1.5rem;
    border-right: 1px solid var(--border);
}
.kpi-item:last-child { border-right: none; }
.kpi-icon { font-size: 1.8rem; margin-bottom: 0.3rem; }
.kpi-number {
    font-family: 'Playfair Display', serif;
    font-size: 2.8rem; font-weight: 800; color: var(--green-dark);
    line-height: 1; margin-bottom: 0.3rem;
}
.kpi-number span { color: var(--gold); }
.kpi-label { font-size: 0.78rem; font-weight: 600; color: var(--text-light); text-transform: uppercase; letter-spacing: 1px; }

/* ══════════════════════════════════════════════════
   SECTIONS
══════════════════════════════════════════════════ */
.section-wrap { padding: 5rem 0 3rem 0; }
.section-eyebrow {
    font-size: 0.72rem; font-weight: 700; letter-spacing: 3px;
    text-transform: uppercase; color: var(--blue-accent);
    margin-bottom: 0.6rem;
}
.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 5.2rem; font-weight: 900; color: var(--green-dark);
    margin-top: 4rem; margin-bottom: 0.5rem;
    position: relative; padding-bottom: 1.2rem;
    line-height: 1.08;
    text-transform: uppercase;
    letter-spacing: 2px;
}
.section-title::after {
    content: '';
    position: absolute; bottom: 0; left: 0;
    width: 80px; height: 6px;
    background: var(--gradient-gold); border-radius: 3px;
}
.section-subtitle {
    color: var(--blue-accent); font-weight: 800;
    font-size: 2.2rem; margin-top: 2rem; margin-bottom: 0.8rem;
    text-transform: uppercase; letter-spacing: 1px;
}
.section-lead {
    color: var(--text-mid); font-size: 1.05rem;
    line-height: 1.7; margin-bottom: 2.5rem;
    max-width: 680px;
}

/* ══════════════════════════════════════════════════
   CARTES SERVICES
══════════════════════════════════════════════════ */
.card {
    background: white;
    border-radius: var(--radius);
    padding: 1.8rem;
    border: 1px solid var(--border);
    border-top: 4px solid var(--green-mid);
    box-shadow: var(--shadow-sm);
    height: 100%; margin-bottom: 1rem;
    transition: all 0.3s ease;
}
.card:hover {
    transform: translateY(-6px);
    box-shadow: var(--shadow-md);
    border-top-color: var(--gold);
}
.card h3 { color: var(--green-dark) !important; font-weight: 800; font-size: 1.15rem; margin-bottom: 0.7rem; text-transform: uppercase; letter-spacing: 0.5px; }
.card p { color: var(--text-mid) !important; font-size: 0.92rem; line-height: 1.65; }
.card b { color: var(--blue-accent) !important; font-size: 0.82rem; font-weight: 600; }
.card-target {
    display: inline-block;
    background: rgba(26,111,168,0.08);
    color: var(--blue-accent); font-size: 0.72rem;
    font-weight: 600; letter-spacing: 0.5px;
    padding: 3px 10px; border-radius: 50px;
    margin-top: 0.7rem;
}

/* ══════════════════════════════════════════════════
   VALEURS
══════════════════════════════════════════════════ */
.value-card {
    background: white; border-radius: var(--radius);
    padding: 1.6rem;
    border-left: 4px solid var(--green-mid);
    box-shadow: var(--shadow-sm);
    height: 100%; margin-bottom: 1rem;
    transition: all 0.3s;
}
.value-card:hover { transform: translateY(-4px); box-shadow: var(--shadow-md); border-left-color: var(--gold); }
.value-card h3 { color: var(--green-dark) !important; font-size: 1rem; font-weight: 700; margin-bottom: 0.5rem; }
.value-card p { color: var(--text-mid) !important; font-size: 0.88rem; line-height: 1.6; }

/* ══════════════════════════════════════════════════
   ACTUALITÉS
══════════════════════════════════════════════════ */
.news-card {
    background: white; border-radius: var(--radius);
    padding: 1.6rem;
    border-top: 4px solid var(--gold);
    box-shadow: var(--shadow-sm);
    height: 100%; margin-bottom: 1rem;
    transition: all 0.3s;
}
.news-card:hover { transform: translateY(-5px); box-shadow: var(--shadow-md); }
.news-date { color: var(--gold); font-weight: 700; font-size: 0.72rem; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 0.5rem; }
.news-card h3 { color: var(--green-dark) !important; font-size: 1.05rem; font-weight: 700; margin-bottom: 0.6rem; }
.news-card p { color: var(--text-mid) !important; font-size: 0.88rem; line-height: 1.6; }

/* ══════════════════════════════════════════════════
   EXPANDER — MASQUAGE COMPLET du natif Streamlit
   On remplace par de vrais boutons via JS (voir components.py)
══════════════════════════════════════════════════ */

/* Masquer tout le widget expander natif */
div[data-testid="stExpander"] {
    border: none !important;
    background: transparent !important;
    box-shadow: none !important;
    margin-bottom: 1.5rem !important;
}
div[data-testid="stExpander"] details {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
}

/* Masquer le summary natif laid et le remplacer visuellement */
div[data-testid="stExpander"] summary {
    /* reset total */
    all: unset !important;
    display: block !important;
    cursor: pointer !important;
    /* Vrai bouton vert dégradé */
    background: linear-gradient(135deg, #1E7A3C 0%, #0D4A1F 100%) !important;
    color: #ffffff !important;
    border-radius: 8px !important;
    padding: 10px 22px !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.8rem !important;
    letter-spacing: 1.2px !important;
    text-transform: uppercase !important;
    box-shadow: 0 4px 16px rgba(13,74,31,0.4) !important;
    transition: background 0.2s ease, transform 0.2s ease, box-shadow 0.2s ease !important;
    width: fit-content !important;
    min-width: 140px !important;
    text-align: center !important;
    user-select: none !important;
    -webkit-tap-highlight-color: transparent !important;
}
div[data-testid="stExpander"] summary::-webkit-details-marker { display: none !important; }
div[data-testid="stExpander"] summary::marker { content: '' !important; display: none !important; }
div[data-testid="stExpander"] summary::before { content: '▶  VOIR PLUS' !important; font-weight: 700 !important; font-size: 0.8rem !important; letter-spacing: 1.2px !important; }
div[data-testid="stExpander"] details[open] > summary::before { content: '▼  MASQUER' !important; }

/* Cacher le texte interne du summary Streamlit (il met son propre label) */
div[data-testid="stExpander"] summary > * { display: none !important; }
div[data-testid="stExpander"] summary > p { display: none !important; }
div[data-testid="stExpander"] summary > div { display: none !important; }
div[data-testid="stExpander"] summary svg { display: none !important; }

div[data-testid="stExpander"] summary:hover {
    background: linear-gradient(135deg, #E8A020 0%, #C4780A 100%) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 22px rgba(232,160,32,0.5) !important;
}

/* Contenu déplié — fond vert sombre et doux */
div[data-testid="stExpanderDetails"] {
    background: #152A1C !important;
    border-radius: 0 8px 8px 8px !important;
    padding: 1.5rem 1.8rem !important;
    margin-top: 2px !important;
    border: none !important;
    border-left: 4px solid var(--gold) !important;
    box-shadow: 0 8px 28px rgba(0,0,0,0.3) !important;
}
div[data-testid="stExpanderDetails"] p {
    color: rgba(255,255,255,0.88) !important;
    font-size: 0.91rem !important;
    line-height: 1.78 !important;
}
div[data-testid="stExpanderDetails"] li {
    color: rgba(255,255,255,0.88) !important;
    font-size: 0.91rem !important;
    line-height: 1.78 !important;
    margin-bottom: 0.3rem !important;
}
div[data-testid="stExpanderDetails"] strong,
div[data-testid="stExpanderDetails"] b {
    color: #F4C842 !important;
    font-weight: 700 !important;
}
div[data-testid="stExpanderDetails"] ul,
div[data-testid="stExpanderDetails"] ol {
    padding-left: 1.3rem !important;
}
div[data-testid="stExpanderDetails"] li::marker {
    color: #E8A020 !important;
}

/* ══════════════════════════════════════════════════
   BOUTONS STREAMLIT
══════════════════════════════════════════════════ */
.stButton>button {
    background: var(--gradient);
    color: white; border-radius: 10px; border: none;
    padding: 0.75rem 2rem; font-weight: 600; font-size: 1rem;
    transition: all 0.3s;
}
.stButton>button:hover { transform: translateY(-3px); box-shadow: var(--shadow-md); }

/* ══════════════════════════════════════════════════
   CTA BANNER + CONTACT
══════════════════════════════════════════════════ */
.cta-banner {
    background: var(--gradient);
    color: white; border-radius: 16px;
    padding: 2rem 2.5rem; text-align: center;
    font-size: 1.1rem; font-weight: 500;
    margin: 2rem 0; box-shadow: var(--shadow-md);
    border: 1px solid rgba(255,255,255,0.08);
}
.cta-grid {
    display: grid; grid-template-columns: repeat(5, 1fr);
    gap: 0.8rem; margin: 1.2rem 0 2rem 0;
}
.cta-box {
    background: white; border: 1.5px solid var(--green-mid);
    border-radius: 10px; padding: 1rem 0.5rem;
    text-align: center; font-weight: 600; font-size: 0.82rem;
    color: var(--green-dark); transition: all 0.25s; cursor: default;
}
.cta-box:hover {
    background: var(--gradient); color: white;
    transform: translateY(-3px); box-shadow: var(--shadow-sm);
    border-color: transparent;
}
.contact-info-card {
    background: white; border-radius: var(--radius);
    padding: 1.5rem;
    border-left: 4px solid var(--green-mid);
    box-shadow: var(--shadow-sm);
    height: 100%; margin-bottom: 1rem;
    transition: all 0.3s;
}
.contact-info-card:hover { transform: translateY(-3px); box-shadow: var(--shadow-md); border-left-color: var(--gold); }
.contact-info-card h4 { color: var(--green-dark); font-weight: 700; margin-bottom: 0.7rem; font-size: 1rem; }
.contact-info-card p, .contact-info-card li { color: var(--text-mid); font-size: 0.9rem; line-height: 1.7; }
.contact-info-card a { color: var(--blue-accent); }

/* ══════════════════════════════════════════════════
   DEMO LIVE
══════════════════════════════════════════════════ */
.demo-wrap {
    background: white; border-radius: 16px;
    padding: 2rem 2rem 1rem 2rem;
    border: 1px solid var(--border);
    box-shadow: var(--shadow-sm);
    margin: 1rem 0;
}
.demo-badge {
    display: inline-flex; align-items: center; gap: 0.4rem;
    background: rgba(46,204,113,0.1); border: 1px solid rgba(46,204,113,0.4);
    color: var(--green-mid); font-size: 0.72rem; font-weight: 700;
    letter-spacing: 1.5px; text-transform: uppercase;
    padding: 4px 14px; border-radius: 50px; margin-bottom: 1rem;
}
.demo-badge::before {
    content: ''; width: 7px; height: 7px;
    border-radius: 50%; background: var(--green-light);
    animation: pulse 1.5s infinite;
}
@keyframes pulse { 0%,100%{opacity:1;transform:scale(1)} 50%{opacity:0.5;transform:scale(1.3)} }

/* ══════════════════════════════════════════════════
   ONGLETS (À propos)
══════════════════════════════════════════════════ */
.stTabs [data-baseweb="tab-list"] { background: white; border-radius: 10px; padding: 4px; box-shadow: var(--shadow-sm); gap: 4px; }
.stTabs [data-baseweb="tab"] { border-radius: 8px; font-weight: 500; font-size: 0.85rem; color: var(--text-mid); padding: 8px 16px; }
.stTabs [aria-selected="true"] { background: var(--gradient) !important; color: white !important; font-weight: 700 !important; }

/* ══════════════════════════════════════════════════
   FOOTER RIBBON
══════════════════════════════════════════════════ */
.footer-ribbon {
    background: var(--green-dark);
    color: rgba(255,255,255,0.7);
    text-align: center; font-size: 0.82rem;
    padding: 1.5rem 1rem;
    border-top: 3px solid var(--gold);
    margin-top: 2rem;
}
.footer-ribbon strong { color: white; }

/* ══════════════════════════════════════════════════
   RESPONSIVE
══════════════════════════════════════════════════ */
@media (max-width: 992px) {
    .topnav-links { gap: 1.2rem; }
    .topnav-links a { font-size: 0.75rem; }
    .hero-graphs { flex-direction: column; align-items: center; }
    .kpi-bar { flex-wrap: wrap; }
    .kpi-item { min-width: 45%; }
}
@media (max-width: 768px) {
    .topnav { padding: 0 1rem; height: 56px; }
    .topnav-links { display: none; }
    .topnav-brand { font-size: 0.85rem; }
    .nav-spacer { height: 56px; }
    .logobar { height: 90px; padding: 0 1rem; }
    .logobar img { height: 65px; }
    .logobar-date { font-size: 0.78rem; }
    .hero-wrap, .hero-overlay { height: 420px; }
    .hero-title { font-size: 2rem; }
    .hero-slogan { font-size: 0.9rem; }
    .hero-graph-box { width: 160px; height: 130px; }
    .section-title { font-size: 3.2rem; }
    .cta-grid { grid-template-columns: 1fr 1fr; }
    .kpi-item { min-width: 50%; }
}
@media (max-width: 480px) {
    .hero-title { font-size: 1.5rem; }
    .hero-graphs { display: none; }
    .kpi-number { font-size: 2.2rem; }
}
</style>
"""
