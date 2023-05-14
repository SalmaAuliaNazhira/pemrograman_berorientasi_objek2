# Nama    : Salma Aulia Nazhira
# NIM     : 210511132
# Kelas   : R3/TI21C

a = u'café'
b = a.encode('utf8')
r = str(b)
print("The unicode string after fixing the UnicodeEncodeError is as follows:")
print(r)

text = "Café"  # Unicode string containing a non-ASCII character

try:
    # Attempt to encode the string using UTF-8 encoding
    encoded_text = text.encode('utf-8')
    print("Encoded text:", encoded_text)
except UnicodeEncodeError as e:
    print("UnicodeEncodeError:", e)
    # Handle the error by specifying an alternative encoding or error handling method
    encoded_text = text.encode('ascii', errors='replace')
    print("Encoded text with replacement:", encoded_text)

