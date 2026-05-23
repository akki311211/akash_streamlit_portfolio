"""
Akash Kumar — Personal Website
Run locally:  streamlit run app.py
Edit content in data/*.py
"""

from pathlib import Path
import streamlit as st

from data.profile import PROFILE
from sections.hero import render_hero
from sections.industry import render_industry
from sections.education import render_education
from sections.teaching import render_teaching
from sections.skills import render_skills
from sections.contact import render_contact
from sections.chat import render_chat_inline
from sections.voice_assistant_inline import render_voice_assistant_inline
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

# 1. Hero
render_hero(PROFILE)

# 2. Inline chat panel — appears right below hero when toggled
if st.session_state.get("chat_open", False):
    st.markdown('<div class="section-spacer"></div>', unsafe_allow_html=True)
    render_chat_inline()

# 3. Inline voice assistant panel — appears right below hero when toggled
if st.session_state.get("voice_open", False):
    st.markdown('<div class="section-spacer"></div>', unsafe_allow_html=True)
    render_voice_assistant_inline()

# Only add spacer before tabs if no panel is open (panels bring their own spacing)
if not st.session_state.get("chat_open", False) and not st.session_state.get("voice_open", False):
    st.markdown('<div class="section-spacer"></div>', unsafe_allow_html=True)

# 4. Section eyebrow label
st.markdown(
    '<div class="tabs-section-label">'
    '<span class="tabs-section-eyebrow">EXPLORE MY BACKGROUND</span>'
    '</div>',
    unsafe_allow_html=True,
)

# 5. Main tabs
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

# 6. Skills
st.markdown('<div class="section-spacer"></div>', unsafe_allow_html=True)
render_skills()

# 7. Contact
st.markdown('<div class="section-spacer"></div>', unsafe_allow_html=True)
render_contact(PROFILE)