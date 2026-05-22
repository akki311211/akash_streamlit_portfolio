"""Teaching tab — renders all entries from data/teaching.py"""

import streamlit as st
from data.teaching import TEACHING, TEACHING_STATS
from components.card import render_card


def render_teaching() -> None:
    st.markdown('<div class="section-intro">', unsafe_allow_html=True)
    st.markdown(
        '<p class="section-lede"></p>',
        unsafe_allow_html=True,
    )
    st.markdown('</div>', unsafe_allow_html=True)

    # Mini stats row
    cols = st.columns(len(TEACHING_STATS))
    for col, stat in zip(cols, TEACHING_STATS):
        with col:
            st.markdown(
                f'''
                <div class="stat-card stat-card-small">
                  <div class="stat-value">{stat["value"]}</div>
                  <div class="stat-label">{stat["label"]}</div>
                </div>
                ''',
                unsafe_allow_html=True,
            )

    st.markdown('<div class="section-spacer"></div>', unsafe_allow_html=True)

    for item in TEACHING:
        render_card(item, kind="teaching")
