import streamlit as st
import numpy as np
import os
import time

# Hide streamlit logo and menu
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🍀 Charlo's Stag 🍀")
st.header("🍻🍷🍸🍹🍺🥃🥤🧃🍻")

tabs = ["DRINKS", "CHALLENGES"]
tab1, tab2 = st.tabs(tabs)

with tab1:
    
    # If "drinks" is not in session state, initialize it
    if "drinks" not in st.session_state:
        st.session_state["drinks"] = os.listdir("drinks")
        # Remove .DS_Store
        if ".DS_Store" in st.session_state["drinks"]:
            st.session_state["drinks"].remove(".DS_Store")

    if st.button("Click me to generate your drink"):
        if len(st.session_state["drinks"]) > 0:
            choice = np.random.randint(0, len(st.session_state["drinks"]))  # Index should start from 0
            drink_choice = st.session_state["drinks"].pop(choice)
            with st.spinner("⌛ Wait for it..."):
                time.sleep(1.5)
            with st.spinner("🥱 The suspense..."):
                time.sleep(1.5)
            st.header(f"Here you go, your drink is...")
            st.image(f"drinks/{drink_choice}", width=300)
            st.header(f"{drink_choice.split('.')[0]}!!!")
        else:
            st.write("No more drinks available, restarting...")
            st.balloons()
            # Resetting the drinks list
            st.session_state["drinks"] = os.listdir("drinks")
            if ".DS_Store" in st.session_state["drinks"]:
                st.session_state["drinks"].remove(".DS_Store")

with tab2:

    challenges_dict = {"arm_wrestle.jpeg": "challenge someone to an arm wrestle",
                           "beer_bong.jpeg": "down a beer",
                           "cigarette.jpeg": "ask someone for a cigarette",
                           "girls.jpeg": "get a photo with two girls",
                           "corporate.jpeg": "ask someone to connect with you on linkedin",
                           "lads.jpeg": "do a shot of tequila",
                           }
        
    # If "challenges" is not in session state, initialize it
    if "challenges" not in st.session_state:
        st.session_state["challenges"] = os.listdir("challenges")

        # Remove .DS_Store
        if ".DS_Store" in st.session_state["challenges"]:
            st.session_state["challenges"].remove(".DS_Store")

    if st.button("Click me to generate your challenge"):
        if len(st.session_state["challenges"]) > 0:
            choice = np.random.randint(0, len(st.session_state["challenges"]))  # Index should start from 0
            challenge_choice = st.session_state["challenges"].pop(choice)
            with st.spinner("⌛ Wait for it..."):
                time.sleep(1.5)
            with st.spinner("🥱 The suspense..."):
                time.sleep(1.5)
            with st.spinner("🥁 Drumroll..."):
                time.sleep(1.5)
            st.header(f"Your challenge is...")
            st.image(f"challenges/{challenge_choice}", width=300)
            st.header(f"{challenges_dict[challenge_choice]}!!!")
        else:
            st.write("No more challenges available, restarting...")
            st.balloons()
            # Resetting the challenges list
            st.session_state["challenges"] = os.listdir("challenges")
            if ".DS_Store" in st.session_state["challenges"]:
                st.session_state["challenges"].remove(".DS_Store")