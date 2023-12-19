#Keyboard Input for Weather Modeling
def temperature_modeling(a, b, c, time):
    temperature = a * time**2 + b * time + c
    return temperature
print("Keyboard Input for Weather Modeling")
a_keyboard = float(input("Enter coefficient a: "))
b_keyboard = float(input("Enter coefficient b: "))
c_keyboard = float(input("Enter coefficient c: "))
time_keyboard = float(input("Enter time in hours: "))
print("Temperature for keyboard input coefficients at time", time_keyboard, "hours:", 
      temperature_modeling(a_keyboard, b_keyboard, c_keyboard, time_keyboard))
print("\n")