# CTP011 Site (Streamlit) — GitHub/Streamlit Cloud Ready

Estrutura esperada no repositório:
- `Home.py`
- `pages/`
  - `2_Story_Of_Our_Lives.py`
  - `3_Biografy.py`
  - `4_Presentatios.py`
- **Pastas de conteúdo** (no raiz do repo):
  - `Fotos_Social/`
  - `Fotos_Job/`
  - `Fotos_Everybody/`
  - `Biografy_folder/`
  - `Presentation_Folder/`
- `utils.py`
- `requirements.txt`

## Rodando localmente
```bash
pip install -r requirements.txt
streamlit run Home.py
```

## Deploy no Streamlit Cloud
1. Suba este projeto para um repositório GitHub.
2. No Streamlit Cloud, crie um app apontando para `Home.py` na branch principal.
3. Confirme o Python 3.10+ e o arquivo `requirements.txt`.