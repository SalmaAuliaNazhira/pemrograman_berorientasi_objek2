# Nama    : Salma Aulia Nazhira
# NIM     : 210511132
# Kelas   : R3/TI21C

def calculate_sum(a, b):
    try:
        
        result = a + b
        return result
    except UnboundLocalError as e:
        print("UnboundLocalError:", e)
        return None

x = 5
y = 10

sum_result = calculate_sum(x, y)
if sum_result is not None:
    print("Sum result:", sum_result)
else:
    print("Error occurred during calculation.")
