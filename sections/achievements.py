"""Academic Achievements tab — renders entries from data/achievements.py."""

import streamlit as st
from data.achievements import ACHIEVEMENTS


def render_achievements() -> None:
    st.markdown(
        '<div class="section-intro">'
        '<p class="section-lede">Consistently ranked among the top performers in every '
        'major academic and competitive examination, from school years through national '
        'entrance exams and international executive programs.</p>'
        '</div>',
        unsafe_allow_html=True,
    )

    parts = ['<div class="achv-grid">']
    for item in ACHIEVEMENTS:
        accent = item.get("accent", "")
        card_cls = f"achv-card achv-accent-{accent}" if accent else "achv-card"
        parts.append(
            f'<div class="{card_cls}">'
            f'<div class="achv-icon">{item.get("icon", "★")}</div>'
            f'<div class="achv-value">{item.get("value", "")}</div>'
            f'<div class="achv-title">{item.get("title", "")}</div>'
            f'<div class="achv-subtitle">{item.get("subtitle", "")}</div>'
            f'<div class="achv-context">{item.get("context", "")}</div>'
            '</div>'
        )
    parts.append('</div>')
    st.markdown("".join(parts), unsafe_allow_html=True)
