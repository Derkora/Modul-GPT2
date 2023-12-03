from transformers import pipeline, set_seed
import streamlit as st

if "messages" not in st.session_state:
  st.session_state.messages = []

for message in st.session_state.messages:
  with st.chat_message(message["role"]):
      st.markdown(message["content"])
          
prompt = st.chat_input("Say something")
if prompt:
  with st.chat_message(name = "user"):
    st.markdown(prompt) 

  st.session_state.messages.append({"role": "user", "content": prompt})
  
path = "akahana/gpt2-indonesia"
generator = pipeline('text-generation', 
                    model=path)
set_seed(42)

preds = generator(prompt, 
                  max_length=64,
                  num_return_sequences=3)
for data in preds:
  print(data)
    
  with st.chat_message(name = "assistant"): 
    st.markdown(data)

  st.session_state.messages.append({"role": "assistant", "content": data})
  
