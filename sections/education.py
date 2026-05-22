"""Education tab — renders all entries from data/education.py"""

import streamlit as st
from data.education import EDUCATION
from components.card import render_card


def render_education() -> None:
    st.markdown('<div class="section-intro">', unsafe_allow_html=True)
    st.markdown(
        '<p class="section-lede">B.Tech graduate with a strong foundation in computer science, '
        'distributed systems, backend engineering, and scalable platform development, backed by '
        '12+ years of hands-on industry experience across high-scale enterprise systems.</p>',
        unsafe_allow_html=True,
    )
    st.markdown('</div>', unsafe_allow_html=True)

    for item in EDUCATION:
        render_card(item, kind="education")
