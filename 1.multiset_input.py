#Hard-coded Variables for Weather Modeling
def temperature_modeling(a, b, c, time):
    temperature = a * time**2 + b * time + c
    return temperature
a_hardcoded, b_hardcoded, c_hardcoded = 4, 7, 3
print("Hard-coded Variables for Weather Modeling\n")
time_hardcoded = 5 
print("Temperature for hardcoded coefficients at time", time_hardcoded, "hours:", 
      temperature_modeling(a_hardcoded, b_hardcoded, c_hardcoded, time_hardcoded))
print("\n")