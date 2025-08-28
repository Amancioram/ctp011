import streamlit as st

st.set_page_config(page_title="CTP011", page_icon="✈️", layout="wide")

st.title("CTP011")
st.write("Curso CTP011 - Agosto de 2025")

st.divider()
st.subheader("Navegue pelas páginas")
cols = st.columns(3)
with cols[0]:
    st.page_link("pages/2_Story_Of_Our_Lives.py", label="Story Of Our Lives", icon="📸")
with cols[1]:
    st.page_link("pages/3_Biografy.py", label="Biografy", icon="🧑‍🤝‍🧑")
with cols[2]:
    st.page_link("pages/4_Presentations.py", label="Presentations", icon="📂")

st.info("Use o menu lateral para navegar também.")
