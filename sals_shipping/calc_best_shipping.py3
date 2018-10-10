# cost by normal ground shipping
def ground_shipping_cost(weight):
  cost = 0
  if weight <= 2:
    cost = weight * 1.50
  elif weight > 2 and weight <= 6:
    cost = weight * 3
  elif weight > 6 and weight <= 10:
    cost = weight * 4
  elif weight > 10:
    cost = weight * 4.75
  return cost + 20

PREMIUM_GROUND_SHIPPING = 125.00

# cost by normal ground shipping
def drone_shipping_cost(weight):
  cost = 0
  if weight <= 2:
    cost = weight * 4.50
  elif weight > 2 and weight <= 6:
    cost = weight * 9
  elif weight > 6 and weight <= 10:
    cost = weight * 12
  elif weight > 10:
    cost = weight * 14.25
  return cost

# calc and return cheapest shippping method
def get_best_shipping_method(weight):
  drone = drone_shipping_cost(weight)
  ground = ground_shipping_cost(weight)
  shipping_method = ""
  if ground < drone and ground < PREMIUM_GROUND_SHIPPING:
    shipping_method = "Ground shipping for: $%.2f" % (ground)
  elif drone < ground and drone < PREMIUM_GROUND_SHIPPING:
    shipping_method = "Drone shipping for: $%.2f" % (drone)
  else:
    shipping_method = "Premium ground shipping for: $%.2f" % (PREMIUM_GROUND_SHIPPING)
  return shipping_method

# test that shipping a 8.4lb package via ground costs 53.6
print(ground_shipping_cost(8.40))

# test that shipping a 1.5lb package via drone costs 6.75
print(drone_shipping_cost(1.50))

# test cheapest method of shipping for 4.8lb package
print(get_best_shipping_method(4.80))

# test cheapest method of shipping for 41.5lb package
print(get_best_shipping_method(41.50))