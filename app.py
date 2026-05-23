"""
Akash Kumar — Personal Website
Run locally:  streamlit run app.py
Edit content in data/*.py
"""

from pathlib import Path
import streamlit as st
from sections.chat import render_chat_inline

from data.profile import PROFILE
from sections.hero import render_hero
from sections.industry import render_industry
from sections.education import render_education
from sections.teaching import render_teaching
# from sections.achievements import render_achievements
# from sections.gallery import render_gallery
from sections.skills import render_skills
from sections.contact import render_contact
from sections.chat import render_chat_inline
from utils.images import ensure_placeholders


# ── Page config ───────────────────────────────────────────────
st.set_page_config(
    page_title=f'{PROFILE["name"]} · Personal Website · {PROFILE["title"]}',
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── One-time setup ────────────────────────────────────────────
@st.cache_resource
def _bootstrap():
    ensure_placeholders()
    return True

_bootstrap()

# ── Inject CSS ────────────────────────────────────────────────
css_path = Path(__file__).parent / "styles.css"
if css_path.exists():
    st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)

# Hide the sidebar page navigation Streamlit auto-generates for multi-page apps
st.markdown(
    "<style>[data-testid='stSidebarNav']{display:none!important}</style>",
    unsafe_allow_html=True,
)

# ═══════════════════════════════════════════════════════════════
# PAGE LAYOUT
# ═══════════════════════════════════════════════════════════════

# 1. Hero (photo, name, summary, stats, resume + chat toggle buttons)
render_hero(PROFILE)

# 2. Inline chat panel — appears right below hero when toggled
if st.session_state.get("chat_open", False):
    st.markdown('<div class="section-spacer"></div>', unsafe_allow_html=True)
    render_chat_inline()

st.markdown('<div class="section-spacer"></div>', unsafe_allow_html=True)

# 3. Section eyebrow label
st.markdown(
    '<div class="tabs-section-label">'
    '<span class="tabs-section-eyebrow">EXPLORE MY BACKGROUND</span>'
    '</div>',
    unsafe_allow_html=True,
)

# # 4. Main tabs
# tab_industry, tab_education, tab_teaching, tab_achievements, tab_gallery = st.tabs([
#     "💼  Industry Experience",
#     "🎓  Education",
#     "👨‍🏫  Teaching & Mentoring",
#      "🏆  Academic Achievements",
#      "📸  Gallery",
# ])

# 4. Main tabs
tab_industry, tab_education, tab_teaching = st.tabs([
    "💼  Industry Experience",
    "🎓  Education",
    "👨‍🏫  Teaching & Mentoring",
])

with tab_industry:
    render_industry()

with tab_education:
    render_education()

with tab_teaching:
    render_teaching()

# with tab_achievements:
#     render_achievements()
#
# with tab_gallery:
#     render_gallery()

# 5. Skills
st.markdown('<div class="section-spacer"></div>', unsafe_allow_html=True)
render_skills()

# 6. Contact (no chat placeholder — chat is in hero now)
st.markdown('<div class="section-spacer"></div>', unsafe_allow_html=True)
render_contact(PROFILE)
