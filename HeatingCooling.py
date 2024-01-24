"""Psuedo notes
psuedo code
look up fourmulas for temp to code.

heating_cooling = 0

while loop looking for specfic conditionals greater equal and lessthan equal

if the actual_temp is too high
print run a/c

if the actual_temp is too cold
print run heat

if it's the desired_temp
print stand bay

**exteneded challenge**
convert_temp = 0

temp_celsius is a number

target_unit is a string for ("C", "F", "K")

if temp_celsius is this pull temp to be converted into target_unit"""

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