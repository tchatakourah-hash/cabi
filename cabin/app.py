"""
KOURA AgriData Impact — Site vitrine amélioré
Style inspiré de kapiconsult.tg + sowing.eu
"""

from pathlib import Path

import streamlit as st
import streamlit.components.v1 as st_components

from styles import CUSTOM_CSS
from components import (
    render_navbar,
    render_topbar,
    render_hero_video,
    render_service_card,
    render_value_card,
    render_expandable_card,
    render_news_card,
    render_cta_grid,
    render_contact_info_card,
    render_ticker,
    render_kpi_bar,
    inject_lucide_icons,
)
from icons import icon_html, replace_emojis_with_icons
from demo_data import (
    generate_demo_dataframe,
    generate_yield_revenue_dataframe,
    build_yield_distribution_chart,
    build_yield_vs_revenue_chart,
)
import content as c

# ── Configuration ──────────────────────────────────────────────────
st.set_page_config(
    page_title=f"{c.CABINET_NOM} | Agroéconomie & Data Science",
    page_icon="🌾", layout="wide", initial_sidebar_state="collapsed",
)

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
inject_lucide_icons()

# ── Navigation ─────────────────────────────────────────────────────
render_navbar(brand_name=c.CABINET_NOM)
render_topbar()

# ── Bandeau défilant expertises ────────────────────────────────────
EXPERTISES = [
    "Analyse de données agricoles",
    "Tableaux de bord interactifs",
    "Suivi & Évaluation de projets",
    "Analyse d'impact",
    "Data Science appliquée",
    "Formation & Renforcement de capacités",
    "Développement rural",
    "Visualisation géospatiale",
]
render_ticker(EXPERTISES)

# ── Hero vidéo ─────────────────────────────────────────────────────
render_hero_video(title=c.CABINET_NOM, slogan=c.CABINET_SLOGAN)

# ── Compteurs KPI (style kapiconsult) ──────────────────────────────
KPIS = [
    {"icon": "🚀", "value": "2026", "suffix": "", "label": "Année de création"},
    {"icon": "🌍", "value": "7",    "suffix": "+", "label": "Services proposés"},
    {"icon": "📊", "value": "6",    "suffix": "+", "label": "Projets réalisés"},
    {"icon": "🎓", "value": "5",    "suffix": "+", "label": "Certifications"},
]
render_kpi_bar(KPIS)

# ════════════════════════════════════════════════════════════════════
# SECTION ACCUEIL — Nos Expertises (résumé)
# ════════════════════════════════════════════════════════════════════
st.markdown('<div id="accueil"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-eyebrow">Ce que nous faisons</div>', unsafe_allow_html=True)
st.markdown('<p class="section-title">Nos Expertises</p>', unsafe_allow_html=True)
st.markdown('<p class="section-lead">Nous accompagnons les institutions, ONG et projets agricoles dans la transformation de leurs données en outils d\'aide à la décision simples, fiables et puissants.</p>', unsafe_allow_html=True)

cols = st.columns(3)
for col, service in zip(cols, c.SERVICES[:3]):
    with col:
        render_service_card(
            icon=service["icon"], title=service["title"],
            description=service["description"], target=service["target"]
        )

# ════════════════════════════════════════════════════════════════════
# SECTION SERVICES (complet)
# ════════════════════════════════════════════════════════════════════
st.markdown('<div id="services"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-eyebrow">Notre offre</div>', unsafe_allow_html=True)
st.markdown('<p class="section-title">Nos Services</p>', unsafe_allow_html=True)

cols_services = st.columns(3)
for i, service in enumerate(c.SERVICES):
    with cols_services[i % 3]:
        render_service_card(
            icon=service["icon"], title=service["title"],
            description=service["description"], target=service["target"]
        )

# ── Démo Live ──────────────────────────────────────────────────────
st.markdown('<div id="demo-live"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-eyebrow">Démonstration interactive</div>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">📊 Démo Live : Analyse des Revenus Agricoles</p>', unsafe_allow_html=True)

st.markdown("""
<div class="demo-wrap">
<div class="demo-badge">EN DIRECT — Données interactives</div>
""", unsafe_allow_html=True)

st.write("Filtrez et visualisez comme dans vos vrais projets. Cette démo illustre notre maîtrise de la data appliquée à l'agriculture.")

df_demo = generate_demo_dataframe()
col_f1, col_f2 = st.columns(2)
with col_f1:
    culture_sel = st.multiselect("Filtrer par culture", df_demo["Culture"].unique(), default=df_demo["Culture"].unique())
with col_f2:
    zone_sel = st.multiselect("Filtrer par zone", df_demo["Zone"].unique(), default=df_demo["Zone"].unique())

df_filtre = df_demo[df_demo["Culture"].isin(culture_sel) & df_demo["Zone"].isin(zone_sel)]

col_g1, col_g2 = st.columns(2)
with col_g1:
    st.plotly_chart(build_yield_distribution_chart(df_filtre), use_container_width=True)
with col_g2:
    df_scatter = generate_yield_revenue_dataframe()
    st.plotly_chart(build_yield_vs_revenue_chart(df_scatter), use_container_width=True)

st.info("💡 Cette démo tourne sur des données simulées. Imaginez avec vos vraies données d'enquête KoboToolbox.")
st.markdown("</div>", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════
# SECTION RÉALISATIONS
# ════════════════════════════════════════════════════════════════════
st.markdown('<div id="realisations"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-eyebrow">Portfolio</div>', unsafe_allow_html=True)
st.markdown('<p class="section-title">Nos Réalisations</p>', unsafe_allow_html=True)
st.write("Projets et expériences pratiques en data science, suivi-évaluation et analyse agricole.")

cols_real = st.columns(3)
for i, real in enumerate(c.REALISATIONS):
    with cols_real[i % 3]:
        render_expandable_card(
            icon=real["icon"], title=real["title"],
            summary=real["summary"], details=real["details"]
        )

# ════════════════════════════════════════════════════════════════════
# SECTION RESSOURCES
# ════════════════════════════════════════════════════════════════════
st.markdown('<div id="ressources"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-eyebrow">Publications & Ressources</div>', unsafe_allow_html=True)
st.markdown('<p class="section-title">Ressources & Publications</p>', unsafe_allow_html=True)
st.write("Articles, rapports, guides et jeux de données partagés par le cabinet.")

cols_res = st.columns(3)
for i, res in enumerate(c.RESSOURCES):
    with cols_res[i % 3]:
        render_expandable_card(
            icon=res["icon"], title=res["title"],
            summary=res["summary"], details=res["details"]
        )

# ════════════════════════════════════════════════════════════════════
# SECTION ACTUALITÉS
# ════════════════════════════════════════════════════════════════════
st.markdown('<div id="actualites"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-eyebrow" style="color:#E8A020;">Dernières nouvelles</div>', unsafe_allow_html=True)
st.markdown('<p class="section-title" style="color:#0D4A1F;">Actualités</p>', unsafe_allow_html=True)

cols_actu = st.columns(3)
for i, actu in enumerate(c.ACTUALITES):
    with cols_actu[i % 3]:
        render_news_card(
            icon=actu["icon"], date=actu["date"],
            title=actu["title"], text=actu["text"]
        )

# ════════════════════════════════════════════════════════════════════
# SECTION À PROPOS
# ════════════════════════════════════════════════════════════════════
st.markdown('<div id="apropos"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-eyebrow">Notre identité</div>', unsafe_allow_html=True)
st.markdown(f'<p class="section-title">À propos de {c.CABINET_NOM}</p>', unsafe_allow_html=True)
st.markdown(c.APROPOS_INTRO)

tab_vision, tab_mission, tab_valeurs, tab_fondateur, tab_diplomes = st.tabs(
    ["🌍 Vision", "🎯 Mission", "💎 Valeurs", "👤 Fondateur", "🎓 Diplômes & Certifications"]
)

with tab_vision:
    st.markdown(c.APROPOS_VISION_LONGUE)
    st.markdown("**Nos ambitions :**")
    for item in c.APROPOS_VISION_OBJECTIFS:
        st.markdown(f"- {item}")
    st.markdown("---")
    st.markdown("**Ce que nous faisons :**")
    cols_cqnf = st.columns(2)
    for i, item in enumerate(c.APROPOS_CE_QUE_NOUS_FAISONS):
        with cols_cqnf[i % 2]:
            st.markdown(f"- {item}")

with tab_mission:
    st.markdown(c.APROPOS_MISSION)
    st.markdown("**Nos engagements :**")
    for item in c.APROPOS_MISSION_ENGAGEMENTS:
        st.markdown(f"- {item}")
    st.markdown("---")
    st.markdown(f"**🎯 Notre objectif :** {c.APROPOS_OBJECTIF}")
    st.markdown("---")
    st.markdown("**Notre approche :**")
    for item in c.APROPOS_APPROCHE:
        st.markdown(f"- {item}")

with tab_valeurs:
    st.write("Les valeurs qui guident chacune de nos missions :")
    cols_val = st.columns(3)
    for i, val in enumerate(c.APROPOS_VALEURS):
        with cols_val[i % 3]:
            render_value_card(val["icon"], val["title"], val["text"])
    st.markdown("---")
    st.markdown("**💡 Pourquoi nous choisir ?**")
    for item in c.APROPOS_POURQUOI_NOUS_CHOISIR:
        st.markdown(f"- {item}")
    st.markdown("**🤝 Nos partenaires cibles :**")
    st.write(" • ".join(c.APROPOS_PARTENAIRES))

with tab_fondateur:
    col_photo, col_bio = st.columns([1, 3])
    with col_photo:
        photo_path = Path(__file__).parent / c.FONDATEUR_PHOTO
        if photo_path.exists():
            st.image(str(photo_path), use_container_width=True)
        else:
            st.markdown(
                '<div style="height:200px;background:var(--gradient);'
                'border-radius:15px;display:flex;align-items:center;justify-content:center;'
                'color:white;font-size:3rem;">👤</div>',
                unsafe_allow_html=True,
            )
    with col_bio:
        st.markdown(f"### {c.FONDATEUR_NOM}")
        st.markdown(f"*{c.FONDATEUR_TITRE}*")
        st.markdown(c.FONDATEUR_PARCOURS)

with tab_diplomes:
    st.markdown("**📘 Diplômes académiques**")
    cols_dipl = st.columns(3)
    for i, dipl in enumerate(c.FONDATEUR_DIPLOMES_ACADEMIQUES):
        with cols_dipl[i % 3]:
            render_value_card(dipl["icon"], dipl["title"], dipl["text"])
    st.markdown("---")
    st.markdown("**📊 Certifications professionnelles**")
    for cert in c.FONDATEUR_CERTIFICATIONS:
        st.markdown(f"- {cert}")
    st.markdown("---")
    st.markdown("**🌍 Formation continue — Veille active sur :**")
    for item in c.FONDATEUR_FORMATION_CONTINUE:
        st.markdown(f"- {item}")

# ════════════════════════════════════════════════════════════════════
# SECTION DIAGNOSTIC GRATUIT
# ════════════════════════════════════════════════════════════════════
st.markdown('<div id="diagnostic"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-eyebrow">Offre de lancement</div>', unsafe_allow_html=True)
st.markdown('<p class="section-title">Diagnostic Data Gratuit — 15 min</p>', unsafe_allow_html=True)

if "diagnostic_form_count" not in st.session_state:
    st.session_state.diagnostic_form_count = 0

with st.form(f"diagnostic_form_{st.session_state.diagnostic_form_count}"):
    colA, colB = st.columns(2)
    with colA:
        nom_org = st.text_input("Nom de votre organisation *")
        type_org = st.selectbox("Type de structure *",
            ["ONG Internationale","ONG Locale","Institution Publique","Coopérative Agricole","Bureau d'études","Autre"])
        contact_diag = st.text_input("Email / Téléphone *")
    with colB:
        projet = st.text_input("Nom du projet / Programme")
        zone = st.text_input("Zone d'intervention")
        indicateurs = st.text_area("Quels indicateurs voulez-vous suivre ?",
            placeholder="Ex: Rendement agricole, Taux d'adoption, Revenu ménage...")

    soumis = st.form_submit_button("Réserver mon diagnostic gratuit")
    if soumis:
        if nom_org and contact_diag:
            st.success(f"Merci {nom_org}. Demande enregistrée. Je vous contacte sous 24h.")
            st.balloons()
            st.session_state.diagnostic_form_count += 1
            st.rerun()
        else:
            st.error("Veuillez renseigner au minimum le nom de l'organisation et un contact.")

# ── Pourquoi me faire confiance ────────────────────────────────────
st.markdown('<div class="section-eyebrow">Crédibilité & Expertise</div>', unsafe_allow_html=True)
st.markdown('<p class="section-title">Pourquoi me faire confiance</p>', unsafe_allow_html=True)

from pathlib import Path as _Path
import base64 as _b64

def _trust_img(filename, height=80):
    """Retourne un tag <img> base64 ou un placeholder si le fichier est absent."""
    p = _Path(__file__).parent / filename
    if p.exists():
        data = _b64.b64encode(p.read_bytes()).decode()
        ext = p.suffix.lstrip(".")
        return f'<img src="data:image/{ext};base64,{data}" style="height:{height}px;width:auto;object-fit:contain;max-width:100%;">'
    return f'<div style="height:{height}px;display:flex;align-items:center;justify-content:center;color:#6B7C75;font-size:0.78rem;font-style:italic;">{filename}</div>'

def _trust_card(label, title, subtitle, *imgs_html):
    imgs_block = "".join(
        f'<div style="display:flex;align-items:center;justify-content:center;">{img}</div>'
        for img in imgs_html
    )
    return f"""
    <div style="background:white;border-radius:12px;padding:1.5rem;border-top:4px solid #1E7A3C;
                box-shadow:0 4px 18px rgba(13,74,31,0.1);text-align:center;height:100%;
                transition:all 0.3s;" onmouseover="this.style.transform='translateY(-5px)';this.style.boxShadow='0 12px 32px rgba(13,74,31,0.18)'"
         onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='0 4px 18px rgba(13,74,31,0.1)'">
        <div style="display:flex;align-items:center;justify-content:center;gap:1rem;margin-bottom:1rem;flex-wrap:wrap;min-height:90px;">
            {imgs_block}
        </div>
        <div style="font-size:0.7rem;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#1A6FA8;margin-bottom:0.3rem;">{label}</div>
        <div style="font-size:1rem;font-weight:800;color:#0D4A1F;margin-bottom:0.2rem;">{title}</div>
        <div style="font-size:0.82rem;color:#3D5A47;">{subtitle}</div>
    </div>"""

cT1, cT2, cT3, cT4 = st.columns(4)

with cT1:
    st.markdown(_trust_card(
        "Certification",
        "IBM Data Science",
        "Obtenu — 2026",
        _trust_img("ibm.png", 75)
    ), unsafe_allow_html=True)

with cT2:
    st.markdown(_trust_card(
        "Expérience Terrain",
        "ONG RAFIA — Étude PROSAD",
        "Université Catholique de Louvain",
        _trust_img("rafia.png", 55),
        _trust_img("louvin.png", 55)
    ), unsafe_allow_html=True)

with cT3:
    st.markdown(_trust_card(
        "Outils maîtrisés",
        "Python · Plotly · Tableau · Power BI",
        "Stack data science complet",
        _trust_img("python3.png", 50),
        _trust_img("plotly.png", 50)
    ), unsafe_allow_html=True)

with cT4:
    st.markdown(_trust_card(
        "Formation académique",
        "Université de Lomé & Kara",
        "Agroéconomie & Data Science",
        _trust_img("ul.jpg", 55),
        _trust_img("kara.png", 55)
    ), unsafe_allow_html=True)

st.write("")
st.markdown("*Stack technique* : Python • Pandas • Plotly • SPSS • STATA • Tableau • Power BI • KoboToolbox")

# ════════════════════════════════════════════════════════════════════
# SECTION CONTACT
# ════════════════════════════════════════════════════════════════════
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-eyebrow">Travaillons ensemble</div>', unsafe_allow_html=True)
st.markdown('<p class="section-title">Contactez-nous</p>', unsafe_allow_html=True)

st.markdown("""
<div class="cta-banner">
    Vous avez un projet agricole, une étude ou un besoin en analyse de données ?<br>
    Notre équipe est à votre écoute pour vous accompagner avec des solutions adaptées.
</div>
""", unsafe_allow_html=True)

st.markdown('<p class="section-subtitle">💬 Contact rapide</p>', unsafe_allow_html=True)
render_cta_grid([
    "📝 Demander un devis",
    "📅 Prendre un rendez-vous",
    "🎁 Consultation gratuite",
    "💬 Échanger avec un expert",
    "📄 Proposition technique",
])

st.markdown('<p class="section-subtitle">📍 Informations de contact</p>', unsafe_allow_html=True)
col_addr, col_tel, col_web = st.columns(3)

with col_addr:
    render_contact_info_card("📍 Adresse du cabinet", f"""
        <p><b>{c.CONTACT['adresse_nom']}</b><br>
        {c.CONTACT['adresse_quartier']}<br>
        {c.CONTACT['adresse_ville']}, {c.CONTACT['adresse_pays']}</p>""")

with col_tel:
    render_contact_info_card("☎️ Téléphone", f"""
        <p>{c.CONTACT['telephone_2']}<br>
        WhatsApp : {c.CONTACT['whatsapp']}</p>""")

with col_web:
    render_contact_info_card("📧 Email & Web", f"""
        <p>{c.CONTACT['email']}<br>
        <a href="{c.CONTACT['site_web_url']}" target="_blank">{c.CONTACT['site_web']}</a></p>""")

col_social, col_horaires = st.columns(2)

with col_social:
    render_contact_info_card("🌐 Réseaux professionnels", f"""
        <p>LinkedIn : <a href="{c.CONTACT['linkedin_url']}" target="_blank">{c.CONTACT['linkedin_label']}</a><br>
        GitHub : <a href="{c.CONTACT['github_url']}" target="_blank">{c.CONTACT['github_label']}</a></p>""")

with col_horaires:
    horaires_html = "".join(f"<li>{j} : {h}</li>" for j, h in c.CONTACT["horaires"])
    render_contact_info_card("📅 Horaires d'ouverture",
        f"<ul style='padding-left:1.2rem;margin:0;'>{horaires_html}</ul>")

# ── Formulaire de contact complet ──────────────────────────────────
st.markdown('<p class="section-subtitle">📝 Formulaire de contact</p>', unsafe_allow_html=True)

if "contact_form_count" not in st.session_state:
    st.session_state.contact_form_count = 0

with st.form(f"contact_form_{st.session_state.contact_form_count}"):
    col1, col2 = st.columns(2)
    with col1:
        c_nom   = st.text_input("Nom et prénom *")
        c_org   = st.text_input("Organisation / entreprise")
        c_poste = st.text_input("Poste / fonction")
        c_email = st.text_input("Adresse e-mail *")
        c_tel   = st.text_input("Téléphone")
        c_pays  = st.text_input("Pays")
    with col2:
        c_sujet = st.text_input("Sujet de la demande *")
        c_type_service = st.selectbox("Type de service recherché", [
            "Analyse de données agricoles & socio-économiques",
            "Tableaux de bord interactifs",
            "Suivi & Évaluation (S&E) de projets",
            "Analyse d'impact des programmes",
            "Data science appliquée à l'agriculture",
            "Appui aux projets de développement",
            "Formation & renforcement de capacités",
            "Autre",
        ])
        c_description = st.text_area("Description détaillée du besoin *",
            placeholder="Décrivez votre projet, vos objectifs et vos attentes...", height=120)
        c_fichier = st.file_uploader("Pièce jointe (cahier des charges, termes de référence...)",
            type=["pdf","doc","docx","xls","xlsx"])

    c_consentement = st.checkbox(
        "J'accepte que mes données personnelles soient traitées dans le cadre de ma demande *")

    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        c_envoyer = st.form_submit_button("📨 Envoyer la demande", use_container_width=True)
    with col_btn2:
        c_reset = st.form_submit_button("🔄 Réinitialiser le formulaire", use_container_width=True)

    if c_envoyer:
        if c_nom and c_email and c_sujet and c_description and c_consentement:
            st.success(f"Merci {c_nom}, votre demande a bien été envoyée. Nous vous répondrons dans les plus brefs délais.")
            st.balloons()
            st.session_state.contact_form_count += 1
            st.rerun()
        else:
            st.error("Veuillez remplir tous les champs obligatoires (*) et accepter le traitement des données.")

    if c_reset:
        st.session_state.contact_form_count += 1
        st.rerun()

# ── Localisation ───────────────────────────────────────────────────
st.markdown('<p class="section-subtitle">🗺 Localisation</p>', unsafe_allow_html=True)
LATITUDE, LONGITUDE = 10.8614, 0.2042
st.markdown(f"📍 **{c.CONTACT['adresse_nom']}** — {c.CONTACT['adresse_quartier']}, {c.CONTACT['adresse_ville']}, {c.CONTACT['adresse_pays']}", unsafe_allow_html=True)
st_components.iframe(
    f"https://www.google.com/maps?q={LATITUDE},{LONGITUDE}&hl=fr&z=14&output=embed",
    height=350,
)
st.markdown(f"[🧭 Obtenir l'itinéraire vers le cabinet](https://www.google.com/maps/dir/?api=1&destination={LATITUDE},{LONGITUDE})")

# ── Pied de page ───────────────────────────────────────────────────
st.markdown(f"""
<div class="footer-ribbon">
    <strong>{c.CABINET_NOM}</strong> — Fondé en {c.CABINET_ANNEE_CREATION} &nbsp;•&nbsp; {c.CONTACT['localisation']}
    &nbsp;•&nbsp; {c.CONTACT['email']} &nbsp;•&nbsp; {c.CONTACT['whatsapp']}
</div>
""", unsafe_allow_html=True)
