import streamlit as st
from pathlib import Path
import csv

st.set_page_config(page_title="Biografy | CTP011", page_icon="🧑‍🤝‍🧑", layout="wide")
st.title("Biografy")

BASE = Path(__file__).resolve().parent.parent
BIO_DIR = BASE / "Biografy_folder"
CSV_PATH = BIO_DIR / "bios.csv"

# Lê bios.csv (opcional)
def load_bios(csv_path: Path):
    bios = {}
    if csv_path.exists():
        with open(csv_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # chave = stem do filename (ex.: Aluno_01.png -> Aluno_01)
                stem = Path(row.get("filename", "").strip()).stem
                if not stem:
                    continue
                bios[stem] = {
                    "name": (row.get("name") or stem.replace("_", " ")).strip(),
                    "bio": (row.get("bio") or "").strip(),
                    "instagram": (row.get("instagram") or "").strip(),
                    "order": int(row.get("order", 999999)) if (row.get("order") or "").isdigit() else 999999,
                }
    return bios

bios = load_bios(CSV_PATH)

# Carrega imagens
imgs = sorted([p for p in BIO_DIR.glob("*") if p.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}])

if not imgs:
    st.warning("Sem imagens no diretório 'Biografy_folder'.")
    st.stop()

# Monta itens (aplica metadata do CSV quando existir)
items = []
for p in imgs:
    stem = p.stem  # ex.: Aluno_01
    meta = bios.get(stem, {})
    items.append({
        "path": p,
        "name": meta.get("name", stem.replace("_", " ")),
        "bio": meta.get("bio", f"Descrição de {stem.replace('_', ' ')}. Adicione no arquivo bios.csv."),
        "instagram": meta.get("instagram", ""),
        "order": meta.get("order", 999999),
    })

# Ordena por 'order' e depois por nome
items.sort(key=lambda x: (x["order"], x["name"].lower()))

# Renderiza em grade 3 por linha
CARDS_PER_ROW = 3
for i in range(0, len(items), CARDS_PER_ROW):
    cols = st.columns(CARDS_PER_ROW)
    for j, col in enumerate(cols):
        idx = i + j
        if idx >= len(items):
            break
        it = items[idx]
        with col:
            st.image(str(it["path"]), use_container_width=True)
            with st.expander(it["name"]):
                st.write(it["bio"])
                if it["instagram"]:
                    st.markdown(f"[Instagram]({it['instagram']})")
