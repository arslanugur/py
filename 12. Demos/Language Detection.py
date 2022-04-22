# Kütüphaneyi kurmak için   pip install detect
from langdetect import detect

print(detect("one two three")) # en
print(detect("ein zwei drei")) # ge
