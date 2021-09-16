#wapp to read temp in faranite and convert into celcius

fah = float(input("temp in fah "))
cel = (fah-32)*(5/9)

print("temp in fah", fah)
print("temp in cel", cel)
print("temp in cel", round(cel,2), "\u00B0")
print("temp in cel", round(cel,1))
# \u00B0 is the unicode for symbol of cel which we got from google
