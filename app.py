import os
from dotenv import load_dotenv
import streamlit as st
from elevenlabs.client import ElevenLabs
from elevenlabs import play
from openai import OpenAI
import time

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
gpt_client = OpenAI(api_key=openai_api_key)

elevenlabs_api_key = os.getenv("ELEVEN_LABS_KEY")

def how_long(question):
    
    completion = gpt_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a trained fitness coach designed to provide general health information and fitness advice to users. Your primary goal is to offer helpful guidance and support while encouraging users. Your tone should be empathetic, reassuring, and non-judgmental. Responses should only be 25 seconds or 100 words."},
            {"role": "user", "content": question},
        ]
    )
    t_input = completion.choices[0].message.content

    
    client = ElevenLabs(api_key=elevenlabs_api_key)

    
    audio = client.generate(
        text=t_input,
        voice="Charlie",
        model="eleven_multilingual_v2"
    )

    
    play(audio)


with st.sidebar:
    st.title("Dashboard")
    

st.title("HealthChat")
st.subheader("You're #1 health companion")


user_question = st.text_input("Enter your question here:")

if user_question:
    start_time = time.time()
    how_long(user_question)
    end_time = time.time()
    elapsed_time = end_time - start_time
    st.write(f"Function execution time: {elapsed_time} seconds")
