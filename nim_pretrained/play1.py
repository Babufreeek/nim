"""
Version of nim where AI is pre-trained already for faster gameplay
"""
from nim1 import train, play

ai = train(0)
play(ai)
