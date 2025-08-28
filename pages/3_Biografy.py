import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Biografy | CTP011", page_icon="🧑‍🤝‍🧑", layout="wide")
st.title("Biografy")

base = Path(__file__).resolve().parent.parent
bio_dir = base / "Biografy_folder"

imgs = sorted([p for p in bio_dir.glob("*") if p.suffix.lower() in {".png",".jpg",".jpeg",".webp"}])
if not imgs:
    st.warning("Sem imagens no diretório 'Biografy_folder'.")
else:
    names = [p.stem.replace("_"," ") for p in imgs]
    cards_per_row = 3
    for i in range(0, len(imgs), cards_per_row):
        cols = st.columns(cards_per_row)
        for j, col in enumerate(cols):
            idx = i + j
            if idx >= len(imgs):
                break
            with col:
                st.image(str(imgs[idx]), use_container_width=True)
                with st.expander(names[idx]):
                    st.write(f"Descrição de {names[idx]}. Adicione aqui a bio dessa pessoa.")