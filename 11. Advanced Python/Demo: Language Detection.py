# Kütüphaneyi kurmak için   pip install detect
from langdetect import detect

print(detect("one two three"))  # tr
print(detect("ein zwein drei")) # en
