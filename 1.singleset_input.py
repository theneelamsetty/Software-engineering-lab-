#Single set User Input for Weather Modeling
import matplotlib.pyplot as plt
def temperature_modeling(a, b, c, time):
    temperature = a * time**2 + b * time + c
    return temperature
print("User Input for Weather Modeling\n")
coefficients = input("Enter coefficients (a, b, c) separated by spaces: ").split()
a_user, b_user, c_user = map(float, coefficients)
time_user = float(input("Enter time in hours:"))
temperature_result = temperature_modeling(a_user, b_user, c_user, time_user)
print("Temperature for user-input coefficients at time", time_user, "hours:", temperature_result)
time_values = range(int(time_user) + 1) 
temperature_values = [temperature_modeling(a_user, b_user, c_user, t) for t in time_values]

plt.plot(time_values, temperature_values, label='Temperature Curve')
plt.xlabel('Time (hours)')
plt.ylabel('Temperature')
plt.title('Temperature Modeling for User Input Coefficients')
plt.legend()
plt.grid(True)
plt.show()