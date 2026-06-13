"""
Données de démonstration et graphiques pour la section "Démo Live".
"""

import numpy as np
import pandas as pd
import plotly.express as px


def generate_demo_dataframe(n: int = 200, seed: int = 42) -> pd.DataFrame:
    """Génère un jeu de données simulé sur les revenus agricoles."""
    rng = np.random.default_rng(seed)
    return pd.DataFrame({
        "Culture": rng.choice(["Maïs", "Soja", "Riz", "Coton"], n),
        "Zone": rng.choice(["Savanes", "Kara", "Centrale", "Plateaux"], n),
        "Rendement_kg_ha": rng.normal(1200, 300, n).astype(int),
        "Revenu_FCFA": rng.normal(450000, 120000, n).astype(int),
        "Année": rng.choice([2022, 2023, 2024], n),
    })


def generate_yield_revenue_dataframe(n: int = 200, seed: int = 123) -> pd.DataFrame:
    """Génère un jeu de données avec corrélation rendement/revenu par zone."""
    rng = np.random.default_rng(seed)
    rendements = rng.normal(1200, 250, n)

    effet_zone = {"Savanes": -50000, "Kara": 0, "Centrale": 30000, "Plateaux": 60000}
    zones = rng.choice(["Savanes", "Kara", "Centrale", "Plateaux"], n)
    revenus = rendements * 350 + np.array([effet_zone[z] for z in zones]) + rng.normal(0, 40000, n)

    return pd.DataFrame({
        "Rendement_kg_ha": rendements.astype(int),
        "Revenu_FCFA": revenus.astype(int),
        "Zone": zones,
    })


def build_yield_distribution_chart(df: pd.DataFrame) -> "px.Figure":
    """Box plot : distribution des rendements par culture."""
    fig = px.box(
        df, x="Culture", y="Rendement_kg_ha", color="Culture",
        title="Distribution des Rendements par Culture",
        color_discrete_sequence=px.colors.sequential.Greens,
    )
    fig.update_layout(showlegend=False, height=350)
    return fig


def build_yield_vs_revenue_chart(df: pd.DataFrame) -> "px.Figure":
    """Scatter plot avec régression : rendement vs revenu par zone."""
    fig = px.scatter(
        df, x="Rendement_kg_ha", y="Revenu_FCFA", color="Zone",
        title="Rendement vs Revenu par Zone", trendline="ols",
        labels={"Rendement_kg_ha": "Rendement (kg/ha)", "Revenu_FCFA": "Revenu (FCFA)"},
    )
    fig.update_layout(height=350)
    return fig
