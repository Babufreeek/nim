"""
Generate AI by training it 10000 times and play a game with the human user
"""
from nim import train, play

ai = train(10000)
play(ai)
