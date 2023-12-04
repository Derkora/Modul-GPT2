from transformers import pipeline, set_seed
import streamlit as st

def askGPT(chat):
  path = "akahana/gpt2-indonesia"
  generator = pipeline('text-generation', 
                      model=path)
  set_seed(42)

  preds = generator(chat, 
                    max_length=128,
                    num_return_sequences=1)
  for data in preds:
    generated_text = data.get('generated_text', None)
    
  return generated_text
  
st.title("💬 IT-GPT")
st.caption("Powered by GPT-Indonesia by Akahana")

if "messages" not in st.session_state:
  st.session_state.messages = [{"role": "assistant", "content": "Butuh apa nih bang?"}]
  
for message in st.session_state.messages:
  with st.chat_message(message["role"]):
      st.markdown(message["content"])
          
prompt = st.chat_input("Say something")
answer = None
if prompt:
  with st.chat_message(name = "user"):
    st.markdown(prompt) 

  st.session_state.messages.append({"role": "user", "content": prompt})
  answer = askGPT(prompt)
  
if answer is not None:
  with st.chat_message(name = "assistant"): 
    st.markdown(answer)

  st.session_state.messages.append({"role": "assistant", "content": answer})
  
