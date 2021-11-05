#Fahrenheit (°F) = (Celsius x 1.8) + 32
print("Welcome to Celsius to Fahrenheit Converter")
Celsius_Temp = int(input("Please enter the temperature in °C.\n"))
def Fahrenheit_Temp(Temp):
  Fahrenheit_Temp = round((Celsius_Temp * 1.8) + 32)
  return str(Fahrenheit_Temp) + "°F"
print(f"{Celsius_Temp}°C = " + (Fahrenheit_Temp(Celsius_Temp)))