# Nama    : Salma Aulia Nazhira
# NIM     : 210511132
# Kelas   : R3/TI21C


def name_message():
    try:
        name = "SalmaAulia"
        # return SalmaAulia
    except NameError:
        return "NameError occurred. Some variable isn't defined."

print(name_message())