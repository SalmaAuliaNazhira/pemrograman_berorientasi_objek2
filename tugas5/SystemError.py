# Nama    : Salma Aulia Nazhira
# NIM     : 210511132
# Kelas   : R3/TI21C

try:
    # Some code that may raise SystemError
    raise SystemError("An internal error occurred")
except SystemError as e:
    print("SystemError:", e)
    # Handle the exception or perform any necessary actions
    print("Handling SystemError...")
    # Additional logic if needed
    # ...
