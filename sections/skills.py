"""Skills / tech-stack section — compact 2-column grid."""

import streamlit as st
from data.skills import SKILLS


def render_skills() -> None:
    st.markdown(
        '<h2 class="section-heading">Tech Stack</h2>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="section-lede">Tools and frameworks I use day-to-day to build production AI systems.</p>',
        unsafe_allow_html=True,
    )

    categories = list(SKILLS.items())
    # Pair categories side by side
    for i in range(0, len(categories), 2):
        left_cat, left_items = categories[i]
        has_right = (i + 1) < len(categories)

        cols = st.columns(2, gap="medium")

        with cols[0]:
            chips_html = "".join(f'<span class="skill-chip">{item}</span>' for item in left_items)
            st.markdown(
                f'''
                <div class="skill-block">
                  <div class="skill-cat-label">{left_cat}</div>
                  <div class="skill-chips">{chips_html}</div>
                </div>
                ''',
                unsafe_allow_html=True,
            )

        if has_right:
            right_cat, right_items = categories[i + 1]
            with cols[1]:
                chips_html = "".join(f'<span class="skill-chip">{item}</span>' for item in right_items)
                st.markdown(
                    f'''
                    <div class="skill-block">
                      <div class="skill-cat-label">{right_cat}</div>
                      <div class="skill-chips">{chips_html}</div>
                    </div>
                    ''',
                    unsafe_allow_html=True,
                )
