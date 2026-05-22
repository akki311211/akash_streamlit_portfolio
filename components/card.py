"""
Reusable card component.
Each section (industry/education/teaching) renders an item using this card.
Layout: compact logo on the left, all content on the right.
Sub-projects use st.expander — reliable across all Streamlit versions.
"""

import streamlit as st
from utils.images import image_path


def _tag_chips(tags, css_class="chip"):
    if not tags:
        return ""
    chips = "".join(f'<span class="{css_class}">{t}</span>' for t in tags)
    return f'<div class="chips">{chips}</div>'


def _render_subprojects(sub: list) -> None:
    if not sub:
        return

    count = len(sub)
    st.markdown(
        f'<div class="subprojects-label">&#9660;&nbsp; {count} Key Project{"s" if count != 1 else ""}</div>',
        unsafe_allow_html=True,
    )

    for sp in sub:
        with st.expander(sp.get("name", ""), expanded=False):
            st.markdown(
                f'<div class="sub-desc">{sp.get("description", "")}</div>',
                unsafe_allow_html=True,
            )
            if sp.get("tags"):
                sub_chips = "".join(
                    f'<span class="sub-chip">{t}</span>' for t in sp["tags"]
                )
                st.markdown(
                    f'<div class="sub-chips">{sub_chips}</div>',
                    unsafe_allow_html=True,
                )


def render_card(item: dict, *, kind: str = "industry"):
    """
    kind: 'industry' | 'education' | 'teaching'
    item: a dict — see data/*.py for shapes.
    """
    if kind == "industry":
        title    = item.get("company", "")
        subtitle = item.get("role", "")
    elif kind == "education":
        title    = item.get("institution", "")
        subtitle = f'{item.get("degree", "")} · {item.get("score", "")}'.strip(" ·")
    else:
        title    = item.get("organisation", "")
        subtitle = item.get("role", "")

    location   = item.get("location", "")
    dates      = item.get("dates", "")
    rtype      = item.get("type", "")
    summary    = item.get("summary", "")
    highlights = item.get("highlights", []) or []
    tags       = item.get("tags", []) or []
    sub        = item.get("subprojects", []) or []
    img        = item.get("logo") or item.get("photo") or ""
    kicker     = item.get("kicker", "")

    st.markdown('<div class="card">', unsafe_allow_html=True)

    if kicker:
        st.markdown(
            f'<div class="card-kicker">{kicker}</div>',
            unsafe_allow_html=True,
        )

    if img:
        col_img, col_body = st.columns([0.55, 4], gap="medium")
        with col_img:
            st.image(image_path(img), use_container_width=True)
    else:
        col_body = st.columns(1)[0]

    with col_body:
        dates_badge = f'<span class="card-dates">{dates}</span>' if dates else ""
        meta_parts  = [p for p in [location, rtype] if p]
        meta_str    = " · ".join(meta_parts)

        st.markdown(
            f'''
            <div class="card-head">
              <div class="card-title">{title}</div>
              {dates_badge}
            </div>
            <div class="card-subtitle">{subtitle}</div>
            <div class="card-meta">{meta_str}</div>
            ''',
            unsafe_allow_html=True,
        )

        if summary:
            st.markdown(f'<div class="card-summary">{summary}</div>', unsafe_allow_html=True)

        if highlights:
            bullets = "".join(f"<li>{h}</li>" for h in highlights)
            st.markdown(f'<ul class="card-bullets">{bullets}</ul>', unsafe_allow_html=True)

        if tags:
            st.markdown(_tag_chips(tags), unsafe_allow_html=True)

        if sub:
            _render_subprojects(sub)

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="card-spacer"></div>', unsafe_allow_html=True)
