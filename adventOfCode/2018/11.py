# Calculate the End Frequency Changes from the Freq changes list
# * Start from 0
import requests
# Sent the cookie set through the environment variable to get this
input = requests.get("https://adventofcode.com/2018/day/1/input")
# Hard Coded inputs
input = open("11.input","r").read()
input = input.split("\n")
print input
print eval("0"+"".join(input))
