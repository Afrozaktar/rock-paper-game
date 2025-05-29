import streamlit as st
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Streamlit title
st.title("Afroza's Rock Paper Scissors Game")

# Map choices to ASCII art
ascii_art = {
    "rock": rock,
    "paper": paper,
    "scissors": scissors
}

# User selection
my_turn = st.selectbox("What do you want to choose?", ["rock", "paper", "scissors"])
if my_turn in ascii_art:
    st.text("My turn is " + my_turn + ":")
    st.text(ascii_art[my_turn])

# Computer's turn
com_turn = random.choice(list(ascii_art))
st.text("Computer turn is " + com_turn + ":")
st.text(ascii_art[com_turn])

# Win-lose logic
if my_turn == "rock" and com_turn == "scissors":
    st.success("You win!")
elif my_turn == "rock" and com_turn == "paper":
    st.error("Computer wins! You lose")
elif my_turn == "paper" and com_turn == "rock":
    st.success("You win!")
elif my_turn == "paper" and com_turn == "scissors":
    st.error("Computer wins! You lose!")
elif my_turn == "scissors" and com_turn == "paper":
    st.success("You win!")
elif my_turn == "scissors" and com_turn == "rock":
    st.error("Computer wins! You lose!")
elif my_turn == com_turn:
    st.info("It's a tie!")
else:
    st.warning("You chose an invalid option.")
