def ground_shipping_cost(weight):
  if weight <= 2:
  	return (1.50 * weight) + 20
  elif (weight > 2) and (weight <= 6):
  	return (3.00 * weight) + 20
  elif (weight > 6) and (weight <= 10):
  	return (4 * weight) + 20
  else:
    return (4.75 * weight) + 20
  
print(ground_shipping_cost(8.4))

prem_ground_shipping = 125.00

def drone_shipping_cost(weight):
  if weight <= 2:
  	return (4.50 * weight) 
  elif (weight > 2) and (weight <= 6):
  	return (9.00 * weight) 
  elif (weight > 6) and (weight <= 10):
  	return (12 * weight) 
  else:
    return (14.75 * weight) 

print(drone_shipping_cost(1.5))

def cheapest_method(weight):
  pr = prem_ground_shipping(weight)
  ds = drone_shipping_cost(weight)
  gs = ground_shipping_cost(weight)
  
