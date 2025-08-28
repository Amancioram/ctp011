import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Presentations | CTP011", page_icon="📂", layout="wide")
st.title("Presentations")

base = Path(__file__).resolve().parent.parent
pres_dir = base / "Presentation_Folder"
files = sorted([p for p in pres_dir.glob("*.pdf")])

if not files:
    st.warning("Nenhum trabalho encontrado em 'Presentation_Folder'.")
else:
    names = [f.stem.replace("_", " ") for f in files]
    choice = st.selectbox("Selecione um trabalho", options=names, index=0)
    chosen_file = next((f for f in files if f.stem.replace("_", " ") == choice), None)

    st.write(f"**Trabalho selecionado:** {choice}")
    if chosen_file and chosen_file.exists():
        with open(chosen_file, "rb") as f:
            st.download_button(
                label="⬇️ Baixar trabalho (PDF)",
                data=f.read(),
                file_name=chosen_file.name,
                mime="application/pdf"
            )

st.info("Para adicionar novos trabalhos, coloque arquivos PDF na pasta `Presentation_Folder/`.")
