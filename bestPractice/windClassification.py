print(" *** Wind classification ***")
speed = float(input("Enter wind speed (km/h) : "))

if speed <= 0:
    print("!!!Wrong value can't classify.")
    quit()

if speed > 0 and speed < 52.00:
    print("Wind classification is Breeze.")
elif  speed >= 52.00 and speed < 56:
    print("Wind classification is Depression.")

elif  speed >= 56.00 and speed < 102:
    print("Wind classification is Tropical Storm.")
elif  speed >= 102.00 and speed < 209:
    print("Wind classification is Typhoon.")
elif  speed >= 209:
    print("Wind classification is Super Typhoon.")