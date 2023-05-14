# Nama    : Salma Aulia Nazhira
# NIM     : 210511132
# Kelas   : R3/TI21C

binary_data = b'\xc3\x89cole'  # Binary data containing UTF-8 encoded string

try:
    # Attempt to decode the binary data using UTF-8 encoding
    decoded_text = binary_data.decode('utf-8')
    print("Decoded text:", decoded_text)
except UnicodeDecodeError as e:
    print("UnicodeDecodeError:", e)
    # Handle the error by specifying an alternative encoding or error handling method
    decoded_text = binary_data.decode('latin-1', errors='replace')
    print("Decoded text with replacement:", decoded_text)
