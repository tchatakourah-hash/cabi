"""
Composants UI améliorés — KOURA AgriData Impact
Inspirés de kapiconsult.tg + sowing.eu
"""

import base64
import io
from datetime import datetime
from pathlib import Path

import numpy as np
import plotly.graph_objects as go
import streamlit as st
import streamlit.components.v1 as st_components

from icons import icon_html, replace_emojis_with_icons


def img_to_b64(img_path: str) -> str:
    path = Path(__file__).parent / img_path
    if path.exists():
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""


def inject_lucide_icons() -> None:
    st_components.html("""
    <script src="https://unpkg.com/lucide@latest/dist/umd/lucide.js"></script>
    <script>
    function renderLucide() {
      const doc = window.parent.document;
      if (doc.lucideLib === undefined && window.lucide) { doc.lucideLib = window.lucide; }
      const lib = doc.lucideLib || window.lucide;
      if (lib) { lib.createIcons({ context: doc }); }
    }
    renderLucide();
    const observer = new MutationObserver(() => renderLucide());
    observer.observe(window.parent.document.body, { childList: true, subtree: true });
    </script>
    """, height=0, scrolling=False)


def render_navbar(brand_name: str = "AgriData Impact") -> None:
    """Barre de navigation fixe moderne (style kapiconsult)."""
    short = brand_name.replace("KOURA ", "")
    st.markdown(f"""
    <div class="topnav">
        <div class="topnav-brand">🌾 <span>KOURA</span> {short}</div>
        <nav class="topnav-links">
            <a href="#accueil">Accueil</a>
            <a href="#services">Services</a>
            <a href="#realisations">Réalisations</a>
            <a href="#ressources">Ressources</a>
            <a href="#actualites" style="color:#E8A020;font-weight:700;">Actualités</a>
            <a href="#apropos">À propos</a>
            <a href="#contact">Contact</a>
            <a href="#diagnostic" class="topnav-cta">Consultation gratuite</a>
        </nav>
    </div>
    <div class="nav-spacer"></div>
    """, unsafe_allow_html=True)


def render_topbar(logo_path: str = "Mon-logo.png", embleme_path: str = "embleme.png") -> None:
    """Bandeau logo + date/heure + emblème."""
    logo_b64 = img_to_b64(logo_path)
    embleme_b64 = img_to_b64(embleme_path)

    jours = ["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
    mois  = ["janvier","février","mars","avril","mai","juin","juillet",
             "août","septembre","octobre","novembre","décembre"]
    now = datetime.now()
    date_init = (f"{jours[now.weekday()].capitalize()} {now.day} {mois[now.month-1]} "
                 f"{now.year} {now.strftime('%H:%M:%S')}")

    logo_html = (f'<img src="data:image/png;base64,{logo_b64}" alt="Logo">'
                 if logo_b64 else '<div style="width:90px;height:90px;background:var(--green-mid);border-radius:12px;display:flex;align-items:center;justify-content:center;color:white;font-size:2rem;">🌾</div>')
    embleme_html = (f'<img src="data:image/png;base64,{embleme_b64}" alt="Emblème">'
                    if embleme_b64 else '')

    st.markdown(f"""
    <div class="logobar">
        <div>{logo_html}</div>
        <div class="logobar-date" id="datetime">{date_init}</div>
        <div>{embleme_html}</div>
    </div>
    """, unsafe_allow_html=True)

    st_components.html("""
    <script>
    function tick(){
      const el = window.parent.document.getElementById('datetime');
      if(el){
        const d = new Date().toLocaleString('fr-FR',{weekday:'long',day:'numeric',month:'long',year:'numeric',hour:'2-digit',minute:'2-digit',second:'2-digit'});
        el.innerHTML = d.charAt(0).toUpperCase() + d.slice(1);
      }
    }
    tick(); setInterval(tick, 1000);
    </script>
    """, height=0, scrolling=False)


def render_ticker(expertises: list) -> None:
    """Bandeau défilant des expertises (style kapiconsult)."""
    items_html = ""
    for item in expertises * 2:
        items_html += f'{item}<span class="sep">◆</span>'
    st.markdown(f"""
    <div class="ticker-wrap">
      <div class="ticker-content">{items_html}</div>
    </div>
    """, unsafe_allow_html=True)


def render_kpi_bar(kpis: list) -> None:
    """Barre de KPI animés (style kapiconsult compteurs)."""
    items_html = ""
    for kpi in kpis:
        items_html += f"""
        <div class="kpi-item">
            <div class="kpi-icon">{kpi.get('icon','📊')}</div>
            <div class="kpi-number kpi-count" data-target="{kpi.get('value','')}">{kpi.get('value','')}<span>{kpi.get('suffix','')}</span></div>
            <div class="kpi-label">{kpi.get('label','')}</div>
        </div>"""
    st.markdown(f'<div class="kpi-bar">{items_html}</div>', unsafe_allow_html=True)


def _mini_chart_b64(fig: go.Figure) -> str:
    buf = io.BytesIO()
    fig.write_image(buf, format="png", scale=2, width=280, height=100)
    buf.seek(0)
    return base64.b64encode(buf.read()).decode()


def _build_hero_mini_charts() -> tuple:
    x = np.linspace(0, 10, 50)
    y = 800 + 200 * np.sin(x) + np.random.normal(0, 30, 50)
    fig_line = go.Figure()
    fig_line.add_trace(go.Scatter(x=x, y=y, mode="lines",
        line=dict(color="#00D9FF", width=3),
        fill="tozeroy", fillcolor="rgba(0,217,255,0.2)"))
    fig_line.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(visible=False), yaxis=dict(visible=False),
        margin=dict(l=0, r=0, t=0, b=0), height=100)

    fig_gauge = go.Figure(go.Indicator(mode="gauge+number", value=87,
        number=dict(suffix="%", font=dict(color="#00D9FF", size=28)),
        gauge=dict(axis=dict(range=[0,100], visible=False),
                   bar=dict(color="#00D9FF", thickness=0.5),
                   bgcolor="rgba(255,255,255,0.1)", borderwidth=0)))
    fig_gauge.update_layout(paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=0, r=0, t=0, b=0), height=100)

    rng = np.random.default_rng(42)
    xs = rng.normal(1200, 200, 30)
    ys = xs * 350 + rng.normal(0, 30000, 30)
    fig_scatter = go.Figure()
    fig_scatter.add_trace(go.Scatter(x=xs, y=ys, mode="markers",
        marker=dict(color="#00D9FF", size=8, opacity=0.8)))
    fig_scatter.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(visible=False), yaxis=dict(visible=False),
        margin=dict(l=0, r=0, t=0, b=0), height=100)

    return _mini_chart_b64(fig_line), _mini_chart_b64(fig_gauge), _mini_chart_b64(fig_scatter)


def render_hero_video(
    video_filename: str = "istockphoto-2219792088-640_adpp_is.mp4",
    title: str = "AgriData Impact",
    slogan: str = "Transformer les données en décisions pour une agriculture durable",
) -> None:
    video_path = Path(__file__).parent / video_filename
    img_line, img_gauge, img_scatter = _build_hero_mini_charts()

    graphs_html = f"""
    <div class="hero-graphs">
        <a href="#demo-live" class="hero-graph-box">
            <img src="data:image/png;base64,{img_line}" style="width:100%;height:80px;object-fit:contain;">
            <div class="hero-graph-label">Analyse agricole</div>
        </a>
        <a href="#demo-live" class="hero-graph-box">
            <img src="data:image/png;base64,{img_gauge}" style="width:100%;height:80px;object-fit:contain;">
            <div class="hero-graph-label">Suivi-évaluation</div>
        </a>
        <a href="#demo-live" class="hero-graph-box">
            <img src="data:image/png;base64,{img_scatter}" style="width:100%;height:80px;object-fit:contain;">
            <div class="hero-graph-label">Mesure d'impact</div>
        </a>
    </div>"""

    overlay = f"""
    <div class="hero-overlay">
        <div class="hero-eyebrow">🌍 Cabinet Agroéconomie · Data Science · Développement</div>
        <h1 class="hero-title">{title.replace("KOURA ", "<em>KOURA</em> ")}</h1>
        <p class="hero-slogan">{slogan}</p>
        {graphs_html}
        <a href="#accueil" class="hero-btn">Découvrir nos expertises →</a>
    </div>"""

    if not video_path.exists():
        st.markdown(
            f'<div class="hero-wrap" style="background:var(--gradient);">{overlay}</div>',
            unsafe_allow_html=True)
        return

    max_size = 30 * 1024 * 1024
    if video_path.stat().st_size >= max_size:
        st.warning("⚠️ Vidéo trop lourde — limite 30 MB")
        return

    try:
        with open(video_path, "rb") as f:
            vb64 = base64.b64encode(f.read()).decode()
        st.markdown(f"""
        <div class="hero-wrap">
            <video autoplay muted loop playsinline>
                <source src="data:video/mp4;base64,{vb64}" type="video/mp4">
            </video>
            {overlay}
        </div>
        """, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Erreur vidéo : {e}")


def render_service_card(icon: str, title: str, description: str, target: str = "") -> None:
    target_html = f'<span class="card-target">{target}</span>' if target else ""
    st.markdown(f"""
    <div class="card">
        <h3>{icon_html(icon, size=20)} {title}</h3>
        <p>{replace_emojis_with_icons(description)}</p>
        {target_html}
    </div>
    """, unsafe_allow_html=True)


def render_value_card(icon: str, title: str, text: str) -> None:
    st.markdown(f"""
    <div class="value-card">
        <h3>{icon_html(icon, size=20)} {title}</h3>
        <p>{replace_emojis_with_icons(text)}</p>
    </div>
    """, unsafe_allow_html=True)


def render_expandable_card(icon: str, title: str, summary: str, details: str) -> None:
    st.markdown(f"""
    <div class="card">
        <h3>{icon_html(icon, size=20)} {title}</h3>
        <p>{replace_emojis_with_icons(summary)}</p>
    </div>
    """, unsafe_allow_html=True)
    with st.expander("Voir plus"):
        st.markdown(replace_emojis_with_icons(details), unsafe_allow_html=True)


def render_news_card(icon: str, date: str, title: str, text: str) -> None:
    st.markdown(f"""
    <div class="news-card">
        <div class="news-date">{date}</div>
        <h3>{icon_html(icon, size=20)} {title}</h3>
        <p>{replace_emojis_with_icons(text)}</p>
    </div>
    """, unsafe_allow_html=True)


def render_cta_grid(items: list) -> None:
    boxes = "".join(
        f'<div class="cta-box">{replace_emojis_with_icons(item, size=16)}</div>'
        for item in items
    )
    st.markdown(f'<div class="cta-grid">{boxes}</div>', unsafe_allow_html=True)


def render_contact_info_card(title: str, html_body: str) -> None:
    clean = "\n".join(line.strip() for line in html_body.strip().splitlines())
    st.markdown(
        f'<div class="contact-info-card"><h4>{replace_emojis_with_icons(title, size=20)}</h4>{clean}</div>',
        unsafe_allow_html=True,
    )
