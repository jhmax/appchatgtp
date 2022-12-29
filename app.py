import openai
import streamlit as st
from streamlit_chat import message

# API_KEY
openai.api_key = st.secrets["API_KEY"]

def generate_response(prompt):
    completions = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 540,
        n = 1,
        stop= None,
        temperature=1,  #randomness of the answer
    )
    message = completions.choices[0].text
    return message

st.title("ChatBot : Streamlit + openAi")

# -- CHAT DATA ---
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

# --- GET TEXT ---
def get_text():
    input_text = st.text_input("You: ","", key="input")
    return input_text 

user_input = get_text()


if user_input:
    output = generate_response(user_input) 
    # STORE input and output
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state["generated"]:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
