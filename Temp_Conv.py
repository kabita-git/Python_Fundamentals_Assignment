#temperature converterd: Celsius to ferhenheit,ferhenheit to Celsius
#Ask user for temperature value and also for unit
class Converter:
  def __init__(self,temp,unit):
    self.temp=temp
    self.unit=unit
  def f_to_c(self):
    return (self.temp - 32) * 5 / 9
  def c_to_f(self):
    return (self.temp * 9 / 5) + 32
  def conv(self):
    if self.unit == "c":
     return f"{self.temp}°C is {self.c_to_f()}°F"
    elif self.unit == "f":
     return f"{self.temp}°F is {self.f_to_c()}°C"
    else:
        return "The unit is invalid."


temp=float(input("Enter the temperature value: "))
unit=input("Enter the unit:")
obj=Converter(temp,unit)
print(obj.conv())