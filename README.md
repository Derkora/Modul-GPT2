# Modul-GPT2

## Pre-requisites

- Python 3.6+ (3.10/3.11 Recommended)
- PyTorch/TensorFlow/Flax

## Instalasi

**Mulai dengan membuat Virtual Environment Python di direktori project**

```bash
python -m venv .env
```

**Aktifkan Virtual Environment**

Windows

```
.env/Scripts/activate
```

Linux and MacOs

```
source .env/bin/activate
```

**Install Transformers**

```
pip install transformers
```

**Install Streamlit**

```
pip install streamlit
```

**Cek Instalasi Transformers dan Streamlit**

```bash
pip list
```

## Import Model

Pada modul kali ini kita akan menggunakan pre-trained model yang sudah dibuat akahana dari <a href="https://huggingface.co/akahana/gpt2-indonesia">HuggingFace</a>.

```py
from transformers import pipeline, set_seed

path = "akahana/gpt2-indonesia"
generator = pipeline('text-generation', 
                     model=path)
set_seed(42)

kalimat = "dahulu kala ada sebuah"
preds = generator(kalimat, 
                  max_length=64,
                  num_return_sequences=3)
for data in preds:
  print(data)
```

Run code dengan menjalankan code berikut pada terminal:

```bash
python [namafile].py
```

## Streamlit

Untuk mendeploy model pada web, langkah pertama kita akan menggunakan library <a href="https://streamlit.io">**Streamlit**</a>

```py
import streamlit as st

st.write("""
# First Streamlit
Hello""")
```

Run Code dengan Streamlit

```bash
streamlit run [namafile].py
```
