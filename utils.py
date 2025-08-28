import streamlit as st

def carousel(title, images, captions=None, key_prefix="carousel"):
    st.markdown(f"### {title}")
    if "indexes" not in st.session_state:
        st.session_state["indexes"] = {}
    idx = st.session_state["indexes"].get(key_prefix, 0)

    left, mid, right = st.columns([1, 6, 1])
    with mid:
        st.image(images[idx], use_container_width=True, caption=(captions[idx] if captions else None))
    with left:
        if st.button("◀", key=f"{key_prefix}_prev"):
            idx = (idx - 1) % len(images)
    with right:
        if st.button("▶", key=f"{key_prefix}_next"):
            idx = (idx + 1) % len(images)

    st.session_state["indexes"][key_prefix] = idx