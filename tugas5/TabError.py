# Nama    : Salma Aulia Nazhira
# NIM     : 210511132
# Kelas   : R3/TI21C

try:
    
    if True:
        print("Indented code block")
        
        print("This line has incorrect indentation")
except TabError as e:
    print("TabError:", e)
    
    print("There was an error with the indentation. Please review your code.")
