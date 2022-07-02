#!/usr/bin/python3

# Author: Kaio Amaral.
# Script to generate colors.

# Function color has two inputs.
def color(cor, text):
    colors = {
    "blue": "\033[1;34m",
    "red": "\033[31m",
    "green": "\033[1;32m",
    "yellow": "\033[1;33m",
    "fundo": "\033[0;0m"}
    return colors[cor]+f"{text}"+colors["fundo"]

