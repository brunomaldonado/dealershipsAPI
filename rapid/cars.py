import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import server
import random

from utils.oop_dealership import Car, Dealership, Customer
# from utils.config import car_object

def luxury_car():
  dealership = Dealership()
  # data = server.car_trims()
  data = server.car_engines()
  # print(data)
  new_data = []
  car_price = []
  # print(f"\ndata {data}\nlen {len(data)}\n")

  lower_bound = 263549.99
  upper_bound = 895300.49
 
  random_numbers = [random.uniform(lower_bound, upper_bound) for _ in range(100)]
  # print(random_numbers)

  for price in random_numbers:
    on_sale = price
    prices = "{:,.2f}".format(on_sale)
    car_price.append(prices)

  for idx, item in enumerate(data, start=1):
    # print(f"[{idx:2}] {item['make_model']['make']['name']} {item['make_model']['name']} {item['name']}")
    # new_data.append(f"{item['make_model']['make']['name']} {item['make_model']['name']} {item['name']}")
    new_data.append(f"{item['make_model_trim']['make_model']['make']['name']} {item['make_model_trim']['make_model']['name']} {item['make_model_trim']['name']}")

  seen = set()
  unique_data = []
  for car in new_data:
    if car not in seen:
      seen.add(car)
      unique_data.append(car)
    else:
      if unique_data.count(car) < 1:
        unique_data.append(car)

  for idx, car in enumerate(unique_data, start=1):
    print(f" [{idx:2}] {car}")

  # for idx, item in enumerate(data, start=1):
  #   # print(f"{list_data[i]['name']}")
  #   print(f"[{idx:2}] {item['make']['name']} {item['name']}")
  #   new_data.append(f"{item['make']['name']} {item['name']}")
    
  features_car = []
  def select_index(selection):
    if 1 <= selection <= len(new_data) or 1 <= selection <= len(prices):
      return selection - 1
    else:
      return None
    
  while True:
    selection = int(input("\n Select car #: "))
    option_car = select_index(selection)
    # print(option_car)
    car_num = option_car + 1
    # if len(dealership.customers) == 0:
    #   print(f"\n      You need to register...\n")
    # else:
    if isinstance(option_car, int):
      # print("isinstance")
      get_value = unique_data[option_car]
      # print("get value", get_value)
      count = 0
      for idx, car in enumerate(data, start=1):
        # content = f"{car['make_model']['make']['name']} {car['make_model']['name']} {car['name']}"
        content = f"{car['make_model_trim']['make_model']['make']['name']} {car['make_model_trim']['make_model']['name']} {car['make_model_trim']['name']}"
        count += 1

        if get_value == content:
          # print(f"{count} {car}")
          car['price'] = car_price[option_car]
          features_car.append(car)

          name = car['make_model_trim']['make_model']['make']['name']
          brand = car['make_model_trim']['make_model']['name']
          model = car['make_model_trim']['name']
          price = car_price[option_car]
          # print(name, brand, model)
          car = Car(name, brand, model)
          dealership.add_car(car)
          dealership.car_number.append(car_num)          
          break

    else:
      print("Invalid selection")
    option = int(input(" [1] Select car #    [2] Exit.\n Option: "))
    if option == 2:
      # dealership.show_available_cars()
      break

if __name__ == '__main__':
  # luxury_car()
  pass