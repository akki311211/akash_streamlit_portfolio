"""Contact section — clean contact card + footer."""

import streamlit as st


def render_contact(profile: dict) -> None:
    st.markdown('<h2 class="section-heading">Get in Touch</h2>', unsafe_allow_html=True)

    medium_url = profile.get("medium", "")
    medium_line = (
        f'<div class="contact-line">'
        f'<a href="{medium_url}" target="_blank">✍️ Medium</a></div>'
        if medium_url else ""
    )

    st.markdown(
        f'''
        <div class="contact-card contact-card-full">
          <div class="contact-card-title">Contact Akash</div>
          <div class="contact-cols">
            <div>
              <div class="contact-line">📍 {profile["location"]}</div>
              <div class="contact-line">📧 <a href="mailto:{profile["email"]}">{profile["email"]}</a></div>
              <div class="contact-line">📱 {profile["phone"]}</div>
            </div>
            <div>
              <div class="contact-line"><a href="{profile["linkedin"]}" target="_blank">💼 LinkedIn</a></div>
              <div class="contact-line"><a href="{profile["github"]}" target="_blank">💻 GitHub</a></div>
            </div>
          </div>
        </div>
        ''',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="footer">Built with Streamlit &nbsp;·&nbsp; © 2026 Akash Kumar</div>',
        unsafe_allow_html=True,
    )
