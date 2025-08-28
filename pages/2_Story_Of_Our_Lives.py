import streamlit as st
from pathlib import Path
from utils import carousel

st.set_page_config(page_title="Story Of Our Lives | CTP011", page_icon="📸", layout="wide")
st.title("Story Of Our Lives")

base = Path(__file__).resolve().parent.parent

# Carrossel 1 - Social
social_dir = base / "Fotos_Social"
social_imgs = sorted([str(p) for p in social_dir.glob("*") if p.suffix.lower() in {".png",".jpg",".jpeg",".webp"}])
social_caps = [Path(p).stem.replace("_"," ") for p in social_imgs]
if social_imgs:
    carousel("Social", social_imgs, social_caps, key_prefix="social")
else:
    st.warning("Sem imagens no diretório 'Fotos_Social'.")

st.divider()

# Carrossel 2 - Inside the Job
job_dir = base / "Fotos_Job"
job_imgs = sorted([str(p) for p in job_dir.glob("*") if p.suffix.lower() in {".png",".jpg",".jpeg",".webp"}])
job_caps = [Path(p).stem.replace("_"," ") for p in job_imgs]
if job_imgs:
    carousel("Inside the Job", job_imgs, job_caps, key_prefix="inside")
else:
    st.warning("Sem imagens no diretório 'Fotos_Job'.")

st.divider()

# Carrossel 3 - Everybody
every_dir = base / "Fotos_Everybody"
every_imgs = sorted([str(p) for p in every_dir.glob("*") if p.suffix.lower() in {".png",".jpg",".jpeg",".webp"}])
every_caps = [Path(p).stem.replace("_"," ") for p in every_imgs]
if every_imgs:
    carousel("Everybody", every_imgs, every_caps, key_prefix="everybody")
else:
    st.warning("Sem imagens no diretório 'Fotos_Everybody'.")
