print("Home Thermostat")
def heating_cooling (actual_temp, desired_temp):
    if desired_temp > actual_temp:
        print("Run heat")
    elif desired_temp < actual_temp:
        print("Run A/C")
    else:
        print("Stand by")



heating_cooling (70, 65)
heating_cooling (50, 75)
heating_cooling (70, 70)