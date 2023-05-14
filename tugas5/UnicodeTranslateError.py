# Nama    : Salma Aulia Nazhira
# NIM     : 210511132
# Kelas   : R3/TI21C

text = "Café"  # Unicode string containing a non-ASCII character

try:
    # Attempt to translate the string using ASCII encoding
    translated_text = text.encode('ascii').decode('ascii')
    print("Translated text:", translated_text)
except UnicodeTranslateError as e:
    print("UnicodeTranslateError:", e)
    # Handle the error by specifying an alternative translation method or error handling logic
    translated_text = text.encode('ascii', errors='ignore').decode('ascii')
    print("Translated text with ignoring errors:", translated_text)
