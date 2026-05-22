"""Hero / landing section."""

from pathlib import Path
import streamlit as st
from utils.images import image_path


def render_hero(profile: dict) -> None:
    # ── Photo + action buttons column | Info column ──────────
    col_photo, col_info = st.columns([1, 3.2], gap="large")

    with col_photo:
        st.markdown('<div class="hero-photo">', unsafe_allow_html=True)
        st.image(image_path(profile["photo"]), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div style="height:0.7rem"></div>', unsafe_allow_html=True)

        # ── Resume download ──
        resume_path = Path(__file__).parent.parent / profile.get("resume_pdf", "assets/Akash_Kumar_Resume_IC.pdf")
        if resume_path.exists():
            with open(resume_path, "rb") as f:
                st.download_button(
                    label="⬇️  Download Resume",
                    data=f,
                    file_name="Akash_Kumar_Resume_IC.pdf",
                    mime="application/pdf",
                    use_container_width=True,
                    key="resume_dl_btn",
                )
        else:
            # Placeholder — disappears once PDF is dropped in assets/
            st.markdown(
                '<div class="resume-missing-note">📄 Resume PDF not found.<br>'
                'Drop <code>Akash_Kumar_Resume_IC.pdf</code><br>into <code>assets/</code> to enable.</div>',
                unsafe_allow_html=True,
            )

        st.markdown('<div style="height:0.4rem"></div>', unsafe_allow_html=True)

        # ── Chat toggle button ── visible, prominent
        chat_open = st.session_state.get("chat_open", False)
        btn_label = "✕  Close Chat" if chat_open else "💬  AI Chat with Akash"
        if st.button(btn_label, use_container_width=True, key="chat_toggle_btn",
                     type="primary" if not chat_open else "secondary"):
            st.session_state["chat_open"] = not chat_open
            st.rerun()

    # ── Info column ─────────────────────────────────────────
    with col_info:
        st.markdown(
            f'''
            <div class="hero-name">{profile["name"]}</div>
            <div class="hero-title">{profile["title"]}</div>
            <div class="hero-tagline">{profile["tagline"]}</div>
            <div class="hero-location">📍 {profile["location"]}</div>
            ''',
            unsafe_allow_html=True,
        )

        # Contact pills — email, LinkedIn, GitHub, Medium, phone
        medium_url = profile.get("medium", "")
        medium_pill = (
            f'<a class="contact-link" href="{medium_url}" target="_blank">✍️ Medium</a>'
            if medium_url else ""
        )
        contact_html = (
            f'<a class="contact-link" href="mailto:{profile["email"]}">📧 {profile["email"]}</a>'
            f'<a class="contact-link" href="{profile["linkedin"]}" target="_blank">💼 LinkedIn'
            f'<span class="li-follow">7k+ followers</span></a>'
            f'<a class="contact-link" href="{profile["github"]}" target="_blank">💻 GitHub</a>'
            + medium_pill +
            f'<a class="contact-link" href="tel:{profile["phone"].replace(" ","")}">📱 {profile["phone"]}</a>'
        )
        st.markdown(f'<div class="contact-row">{contact_html}</div>', unsafe_allow_html=True)

        # Summary glass card
        st.markdown(
            f'''
            <div class="summary-glass">
              <div class="summary-eyebrow">Professional Summary</div>
              <div class="summary-text">{profile["summary"]}</div>
            </div>
            ''',
            unsafe_allow_html=True,
        )

    # ── Stats row ────────────────────────────────────────────
    st.markdown('<div class="stats-spacer"></div>', unsafe_allow_html=True)
    cols = st.columns(len(profile["stats"]))
    for col, stat in zip(cols, profile["stats"]):
        with col:
            st.markdown(
                f'''
                <div class="stat-card">
                  <div class="stat-value">{stat["value"]}</div>
                  <div class="stat-label">{stat["label"]}</div>
                </div>
                ''',
                unsafe_allow_html=True,
            )
