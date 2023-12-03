from transformers import pipeline, set_seed
import streamlit as st

def askGPT(chat):
  path = "akahana/gpt2-indonesia"
  generator = pipeline('text-generation', 
                      model=path)
  set_seed(42)
  
  preds = generator(chat, 
                    max_length=64,
                    num_return_sequences=3)
  for data in preds:
    print(data)
     
    st.write(data)
    
while True:    
  chat = input("Masukkan Kalimat:")
  if chat == 'exit':
    break
  askGPT(chat)
  
