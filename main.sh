#!/bin/sh

source venv/bin/activate

echo -e "\n Testing all unit tests. \n"

pytest

echo -e "\n Executing all commands. \n"
python3 src/Day1/main.py
