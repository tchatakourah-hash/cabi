"""
Contenu textuel du cabinet AgriData Impact.
Centraliser ces données ici permet de les modifier sans toucher à la logique
d'affichage (app.py / components.py).
"""

# ------------------------------------------------------------------
# Identité générale
# ------------------------------------------------------------------
CABINET_NOM = "KOURA AgriData Impact"
CABINET_SLOGAN = "Transformer les données en décisions pour une agriculture durable"
CABINET_ANNEE_CREATION = "2026"
CABINET_LOCALISATION = "Dapaong, Togo"

# ------------------------------------------------------------------
# Contact
# ------------------------------------------------------------------
CONTACT = {
    "telephone": "+228 91 40 56 52",
    "telephone_2": "+228 96 33 95 02",
    "whatsapp": "+228 91 40 56 52",
    "email": "tchatakourah@gmail.com",
    "site_web": "www.agridataimpact.com",
    "site_web_url": "https://www.agridataimpact.com",
    "linkedin_label": "housseine-tchatakoura-a25a6a334",
    "linkedin_url": "https://www.linkedin.com/in/housseine-tchatakoura-a25a6a334",
    "github_label": "tchatakourah-hash_",
    "github_url": "https://github.com/tchatakourah-hash_",
    "adresse_nom": "Koura AgriDigit Impact",
    "adresse_quartier": "Quartier Bodjopal",
    "adresse_ville": "Dapaong",
    "adresse_pays": "Togo",
    "horaires": [
        ("Lundi – Vendredi", "08h00 – 17h30"),
        ("Samedi", "09h00 – 13h00"),
        ("Dimanche", "Fermé"),
    ],
    "localisation": CABINET_LOCALISATION,
}

# ------------------------------------------------------------------
# ACTUALITÉS (contenu d'exemple, à remplacer par le cabinet)
# ------------------------------------------------------------------
ACTUALITES = [
    {
        "icon": "🚀",
        "date": "Juin 2026",
        "title": "Lancement officiel du cabinet AgriData Impact",
        "text": (
            "AgriData Impact ouvre ses portes à Dapaong avec une mission claire : "
            "mettre la donnée au service de l'agriculture et du développement rural "
            "en Afrique de l'Ouest."
        ),
    },
    {
        "icon": "📊",
        "date": "À venir",
        "title": "Publication du premier rapport d'analyse régionale",
        "text": (
            "Un rapport sur les tendances de rendement agricole dans la région des "
            "Savanes est en préparation, basé sur des données de terrain."
        ),
    },
    {
        "icon": "🤝",
        "date": "À venir",
        "title": "Partenariats en cours de discussion",
        "text": (
            "Des échanges sont en cours avec des ONG et institutions locales pour "
            "des missions de suivi-évaluation et d'appui en data science."
        ),
    },
]

# ------------------------------------------------------------------
# À PROPOS
# ------------------------------------------------------------------
APROPOS_INTRO = (
    "Le cabinet **AgriData Impact** est spécialisé en data science appliquée à "
    "l'agriculture, au suivi-évaluation et à l'analyse d'impact des projets de "
    "développement rural. Nous accompagnons les institutions publiques, ONG, "
    "projets agricoles et acteurs du développement dans la transformation de "
    "leurs données en outils d'aide à la décision simples, fiables et puissants."
)

APROPOS_OBJECTIF = (
    "Rendre la data accessible et utile au service du développement agricole, "
    "afin d'améliorer la productivité, la résilience des systèmes agricoles et "
    "l'efficacité des politiques publiques."
)

APROPOS_CE_QUE_NOUS_FAISONS = [
    "📊 Collecte et structuration de données agricoles et socio-économiques",
    "🧹 Nettoyage et traitement de données",
    "📈 Analyse statistique et data science appliquée",
    "📊 Création de dashboards interactifs (Streamlit, Power BI, Plotly)",
    "🌱 Suivi-évaluation (S&E) de projets de développement",
    "📍 Analyse d'impact et aide à la décision",
    "🌍 Visualisation de données géospatiales et territoriales",
]

APROPOS_APPROCHE = [
    "✔️ La rigueur scientifique",
    "✔️ L'approche orientée impact",
    "✔️ La simplicité des résultats pour les décideurs",
    "✔️ L'innovation technologique",
    "✔️ L'adaptation au contexte africain",
]

APROPOS_VISION = (
    "Devenir un centre de référence en Afrique de l'Ouest dans l'analyse de "
    "données agricoles et l'évaluation d'impact, en contribuant activement à "
    "la transformation digitale du secteur agricole."
)

APROPOS_VISION_LONGUE = (
    "Le Cabinet AgriData Impact ambitionne de devenir un acteur de référence en "
    "Afrique de l'Ouest dans l'exploitation intelligente des données agricoles et "
    "socio-économiques pour un développement durable, inclusif et innovant.\n\n"
    "Nous aspirons à construire un écosystème où la data devient un levier "
    "stratégique de transformation du secteur agricole, permettant aux "
    "institutions publiques, aux ONG, aux projets et aux agriculteurs de prendre "
    "des décisions éclairées, rapides et efficaces."
)

APROPOS_VISION_OBJECTIFS = [
    "Moderniser l'agriculture grâce à la data et aux technologies numériques",
    "Améliorer la productivité et la résilience des systèmes agricoles face au changement climatique",
    "Renforcer la transparence et l'efficacité des projets de développement rural",
    "Faciliter la prise de décision basée sur des preuves (evidence-based policy)",
    "Contribuer à la sécurité alimentaire et à la réduction de la pauvreté en milieu rural",
]

APROPOS_MISSION = (
    "Accompagner les acteurs du secteur agricole et du développement rural dans "
    "l'exploitation stratégique des données afin d'améliorer la performance des "
    "projets, la prise de décision et l'impact sur les populations."
)

APROPOS_MISSION_ENGAGEMENTS = [
    "📊 Collecter, structurer et analyser des données agricoles et socio-économiques fiables",
    "📈 Concevoir des tableaux de bord interactifs pour le suivi et l'évaluation des projets",
    "🌱 Appuyer les institutions, ONG et programmes agricoles dans la mesure d'impact",
    "🧠 Transformer les données en insights clairs pour orienter les politiques et stratégies",
    "🚀 Promouvoir l'innovation digitale et la culture de la data dans l'agriculture",
    "🌍 Contribuer à un développement rural durable, inclusif et résilient face aux défis climatiques",
]

APROPOS_VALEURS = [
    {
        "icon": "🔍",
        "title": "Transparence & Éthique",
        "text": "Nous garantissons la transparence, l'éthique et la fiabilité dans la collecte, l'analyse et la restitution des données. La confiance est au cœur de nos relations.",
    },
    {
        "icon": "📊",
        "title": "Excellence analytique",
        "text": "Nous nous engageons à produire des analyses rigoureuses, précises et utiles, basées sur des méthodes scientifiques et des outils de data science modernes.",
    },
    {
        "icon": "🌱",
        "title": "Impact durable",
        "text": "Chaque projet doit avoir un effet concret et mesurable sur les populations rurales, l'agriculture et le développement durable.",
    },
    {
        "icon": "🚀",
        "title": "Innovation",
        "text": "Nous utilisons les technologies numériques, la data science et la visualisation avancée pour proposer des solutions modernes et efficaces.",
    },
    {
        "icon": "🤝",
        "title": "Collaboration",
        "text": "Nous croyons au travail en réseau avec les institutions, ONG, chercheurs et communautés pour maximiser l'impact des projets.",
    },
    {
        "icon": "🌍",
        "title": "Engagement pour le développement",
        "text": "Nous plaçons l'amélioration des conditions de vie des populations rurales et la sécurité alimentaire au centre de notre mission.",
    },
]

APROPOS_POURQUOI_NOUS_CHOISIR = [
    "Une expertise combinant agriculture + data science + développement",
    "Des solutions adaptées aux réalités du terrain",
    "Une approche orientée résultats et impact",
    "Des outils modernes de visualisation et d'aide à la décision",
]

APROPOS_PARTENAIRES = [
    "Ministères de l'agriculture",
    "ONG et organisations internationales",
    "Projets de développement rural",
    "Instituts de recherche",
    "Coopératives agricoles",
]

# ------------------------------------------------------------------
# FONDATEUR
# ------------------------------------------------------------------
FONDATEUR_NOM = "TCHATAKOURA Housseïne"
FONDATEUR_TITRE = "Agroéconomiste, Data Scientist et Suivi-évaluateur de projets et programmes de développement"
FONDATEUR_PHOTO = "moi.jpg"

FONDATEUR_PARCOURS = (
    "Le parcours du fondateur s'inscrit dans une double expertise :\n\n"
    "🎓 Une formation en **agroéconomie**, axée sur l'analyse des systèmes "
    "agricoles, les politiques de développement rural et la sécurité alimentaire.\n\n"
    "📊 Une spécialisation en **data science et analyse de données**, permettant "
    "de transformer les données brutes en informations utiles à la prise de décision.\n\n"
    "📈 Une expérience en **suivi-évaluation (S&E)** de projets et programmes de "
    "développement.\n\n"
    "Ce parcours est fortement ancré dans les réalités du terrain africain, avec "
    "une compréhension des défis majeurs : faible disponibilité des données "
    "fiables, besoin de suivi efficace des projets, nécessité d'outils simples "
    "pour les décideurs, et importance de l'impact mesurable.\n\n"
    "Aujourd'hui, AgriData Impact se positionne comme un pont entre la data "
    "science et le développement rural, en rendant les données accessibles, "
    "compréhensibles et utiles pour tous les acteurs du secteur."
)

FONDATEUR_DIPLOMES_ACADEMIQUES = [
    {
        "icon": "🎓",
        "title": "Agroéconomie",
        "text": "Spécialisation en analyse des systèmes agricoles, économie rurale et politiques de développement.",
    },
    {
        "icon": "🎓",
        "title": "Analyse de données / Data Science",
        "text": "Acquisition de compétences en traitement de données, statistiques et visualisation.",
    },
    {
        "icon": "🎓",
        "title": "Suivi-Évaluation de projets et programmes",
        "text": "Méthodes de conception, suivi des indicateurs et évaluation d'impact.",
    },
]

FONDATEUR_CERTIFICATIONS = [
    "📌 Data Science et analyse de données (Python, Pandas, NumPy)",
    "📌 Visualisation de données (Plotly, Power BI, Tableau, Streamlit)",
    "📌 Git et GitHub pour la gestion de projets",
    "📌 Méthodologie de recherche et évaluation d'impact (CRISP-DM / approche projet)",
    "📌 Jupyter Notebook et environnement de travail data",
]

FONDATEUR_FORMATION_CONTINUE = [
    "Les outils de data science avancés",
    "Les méthodes modernes de suivi-évaluation",
    "Les innovations en agriculture digitale (AgriTech)",
    "L'intelligence artificielle appliquée au développement",
]

# ------------------------------------------------------------------
# SERVICES
# ------------------------------------------------------------------
SERVICES = [
    {
        "icon": "📊",
        "title": "Analyse de données agricoles & socio-économiques",
        "description": (
            "Nous collectons, nettoyons et analysons des données pour produire "
            "des indicateurs fiables et exploitables pour la prise de décision."
        ),
        "target": "Institutions, ONG, projets agricoles",
    },
    {
        "icon": "📈",
        "title": "Tableaux de bord interactifs",
        "description": (
            "Conception de dashboards dynamiques (Streamlit, Power BI, Plotly) "
            "pour le suivi en temps réel des projets et programmes agricoles."
        ),
        "target": "Projets de développement, coopératives",
    },
    {
        "icon": "🌱",
        "title": "Suivi & Évaluation (S&E) de projets",
        "description": (
            "Mise en place de systèmes complets : définition des indicateurs, "
            "suivi des performances, analyse des résultats et rapports d'impact."
        ),
        "target": "ONG, programmes de développement",
    },
    {
        "icon": "📍",
        "title": "Analyse d'impact des programmes",
        "description": (
            "Évaluation de l'efficacité des projets agricoles et ruraux pour "
            "mesurer leur impact réel sur les populations bénéficiaires."
        ),
        "target": "Bailleurs, institutions publiques",
    },
    {
        "icon": "🧠",
        "title": "Data science appliquée à l'agriculture",
        "description": (
            "Statistiques, modélisation, analyse prédictive, visualisation et "
            "exploration de données massives appliquées au secteur rural."
        ),
        "target": "Ministères, instituts de recherche",
    },
    {
        "icon": "🌍",
        "title": "Appui aux projets de développement",
        "description": (
            "Accompagnement technique des ONG et institutions dans la "
            "planification, le suivi opérationnel et l'évaluation des résultats."
        ),
        "target": "ONG locales et internationales",
    },
    {
        "icon": "🎓",
        "title": "Formation & renforcement de capacités",
        "description": (
            "Formation des équipes sur la data science, le suivi-évaluation et "
            "les outils de visualisation (Excel, Power BI, Python, Streamlit)."
        ),
        "target": "Équipes projets, coopératives",
    },
]

# ------------------------------------------------------------------
# RÉALISATIONS
# ------------------------------------------------------------------
REALISATIONS = [
    {
        "icon": "🌾",
        "title": "Dashboard d'analyse de données agricoles",
        "summary": "Tableau de bord interactif pour analyser production, rendement et évolution saisonnière.",
        "details": (
            "**Outils :** Python, Pandas, Plotly, Streamlit\n\n"
            "**Objectif :** visualiser les performances agricoles et aider à la "
            "prise de décision.\n\n"
            "**Résultat :** dashboard dynamique et interactif, utilisable par des "
            "équipes non techniques."
        ),
    },
    {
        "icon": "📊",
        "title": "Système de suivi-évaluation de projets",
        "summary": "Modèle de suivi des indicateurs de performance pour projets agricoles.",
        "details": (
            "- Définition des indicateurs clés (KPI)\n"
            "- Suivi des résultats et impacts\n"
            "- Visualisation des performances en continu"
        ),
    },
    {
        "icon": "🌍",
        "title": "Analyse d'impact de projets agricoles",
        "summary": "Simulation d'une étude d'impact sur des programmes agricoles.",
        "details": (
            "- Analyse avant / après intervention\n"
            "- Comparaison de résultats entre groupes\n"
            "- Interprétation des effets sur les bénéficiaires"
        ),
    },
    {
        "icon": "📈",
        "title": "Analyse de données socio-économiques en Afrique",
        "summary": "Exploration de jeux de données sur le développement et l'économie agricole.",
        "details": (
            "- Nettoyage et traitement des données\n"
            "- Analyse statistique approfondie\n"
            "- Création de visualisations explicatives pour décideurs"
        ),
    },
    {
        "icon": "🧠",
        "title": "Dashboard Climat & Agriculture",
        "summary": "Outil d'analyse des données climatiques et de leur impact sur l'agriculture.",
        "details": (
            "- Corrélation climat–rendement\n"
            "- Visualisation des tendances climatiques\n"
            "- Outil d'aide à la décision pour les exploitants"
        ),
    },
    {
        "icon": "💻",
        "title": "Portfolio GitHub & projets data",
        "summary": "Mise en ligne de projets de data science et dashboards sur GitHub.",
        "details": (
            "- Gestion de version avec Git\n"
            "- Publication de projets analytiques\n"
            "- Présentation de dashboards interactifs"
        ),
    },
]

# ------------------------------------------------------------------
# RESSOURCES / PUBLICATIONS
# ------------------------------------------------------------------
RESSOURCES = [
    {
        "icon": "📊",
        "title": "Articles analytiques",
        "summary": "Analyses basées sur les données agricoles et socio-économiques d'Afrique de l'Ouest.",
        "details": (
            "- Analyse des tendances agricoles en Afrique de l'Ouest\n"
            "- Impact des projets de développement rural\n"
            "- Lecture des indicateurs de performance agricole\n"
            "- Data-driven insights pour les décideurs"
        ),
    },
    {
        "icon": "📑",
        "title": "Rapports techniques",
        "summary": "Production de rapports structurés pour projets et études de terrain.",
        "details": (
            "- Rapports de suivi-évaluation\n"
            "- Études d'impact de programmes agricoles\n"
            "- Analyses statistiques de terrain\n"
            "- Synthèses de données pour ONG et institutions"
        ),
    },
    {
        "icon": "📘",
        "title": "Guides et documents PDF",
        "summary": "Guides pratiques pour appliquer la data science à l'agriculture (en développement).",
        "details": (
            "- Introduction à la data science appliquée à l'agriculture\n"
            "- Guide de suivi-évaluation de projets\n"
            "- Méthodologie d'analyse de données agricoles\n"
            "- Utilisation de Python pour l'analyse de données rurales"
        ),
    },
    {
        "icon": "🧠",
        "title": "Tutoriels Python / Data Science",
        "summary": "Tutoriels pour la communauté autour de l'analyse de données et des dashboards.",
        "details": (
            "- Analyse de données avec Pandas\n"
            "- Visualisation avec Plotly et Matplotlib\n"
            "- Création de dashboards avec Streamlit\n"
            "- Introduction au machine learning appliqué au développement"
        ),
    },
    {
        "icon": "📂",
        "title": "Jeux de données (Data for Good)",
        "summary": "Datasets ouverts utiles pour la recherche et l'analyse en agriculture.",
        "details": (
            "- Données agricoles régionales\n"
            "- Indicateurs socio-économiques\n"
            "- Données climatiques et environnementales\n"
            "- Jeux de données pour projets étudiants"
        ),
    },
    {
        "icon": "🌍",
        "title": "Actualités du cabinet",
        "summary": "Suivez les activités, projets et collaborations du cabinet.",
        "details": (
            "- Nouveaux projets en cours\n"
            "- Collaborations et partenariats\n"
            "- Lancements de dashboards\n"
            "- Publications récentes"
        ),
    },
]
