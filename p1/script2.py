import os

files = os.walk(r"C:\Users\rajan\OneDrive\Desktop\Personal")

for r,s,f in files:
    print(s)