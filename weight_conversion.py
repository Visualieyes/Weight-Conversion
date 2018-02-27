#Write a function that takes a weight as input and outputs a conversion value

def weight_conversion():
  unit = input("""'Kg' Or 'Pounds':""")
  weight = float(input("Enter weight:"))
  output = 0
  if unit == "kg" or "Kg":
    output = weight * 2.20462                               #constant
    return output
  elif unit == "lbs" or "Lbs" or "pounds" or "Pounds":  
    output = weight * 0.453592                              #constant
    return output
  else:
    return False
    print("Error")
  return output  
  
print(weight_conversion())  
