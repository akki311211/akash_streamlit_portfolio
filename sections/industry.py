"""Industry tab — renders all roles from data/industry.py"""

import streamlit as st
from data.industry import INDUSTRY
from components.card import render_card


def render_industry() -> None:
    st.markdown('<div class="section-intro">', unsafe_allow_html=True)
    st.markdown(
        '<p class="section-lede">'
        'Senior Backend Engineer with 12+ years of experience building scalable distributed systems '
        'and cloud-native backend platforms.'
        'Specialized in Java, Kafka, microservices, and platform engineering.'
        '</p>',
        unsafe_allow_html=True,
    )
    st.markdown('</div>', unsafe_allow_html=True)

    for item in INDUSTRY:
        render_card(item, kind="industry")
