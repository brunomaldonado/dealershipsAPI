# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import random
from utils import server
from utils.inheritance_dealership import Car, Dealership, Customer
from db.db_luxury_cars import luxury_car_lst

def luxury_car():
  dealership = Dealership()
  # data = server.car_trims()
  data = server.car_engines()
  car_price = []

  lower_bound = 263549.99
  upper_bound = 895300.49
 
  random_numbers = [random.uniform(lower_bound, upper_bound) for _ in range(100)]
  # print(random_numbers)

  for price in random_numbers:
    on_sale = price
    prices = "{:,.2f}".format(on_sale)
    car_price.append(prices)

  # for idx, item in enumerate(data, start=1):
  #   # print(f"[{idx:2}] {item['make_model']['make']['name']} {item['make_model']['name']} {item['name']}")
  #   # new_data.append(f"{item['make_model']['make']['name']} {item['make_model']['name']} {item['name']}")
  #   new_data.append(f"{item['make_model_trim']['make_model']['make']['name']} {item['make_model_trim']['make_model']['name']} {item['make_model_trim']['name']}")

  # print(new_data)

  list_car_models = list(dict.fromkeys(luxury_car_lst))

  # print(f"luxury_car_lst {len(luxury_car_lst)}\n unique data {len(unique_data)}")

  for idx, car in enumerate(list_car_models, start=1):
    print(f" [{idx:2}] {car}")

  features_car = []
  def select_index(selection):
    if 1 <= selection <= len(list_car_models) or 1 <= selection <= len(prices):
      return selection - 1
    else:
      return None

  while True:
    try:
      selection = int(input("\n Selected car #: "))
      selected_number = select_index(selection)
      # car_number = selected_number + 1
      if selected_number is None:
        print(" Invalid selection, please try again.")
        continue
      if isinstance(selected_number, int):
        car_brand = list_car_models[selected_number]
        for model_name in data:
          car_model = f"{model_name['make_model_trim']['make_model']['make']['name']} {model_name['make_model_trim']['make_model']['name']} {model_name['make_model_trim']['name']}"
          if car_brand == car_model:
            model_name['price'] = car_price[selected_number]
            # features_car.append(model_name)
            # print(f"CAR... OBJECT {model_name}")
            name = model_name['make_model_trim']['make_model']['make']['name']
            brand = model_name['make_model_trim']['make_model']['name']
            model = model_name['make_model_trim']['name']
            # price = car_price[selected_number]
            # print(name, brand, model, price)
            car = Car(name, brand, model)

            dealership.car_number.append(selected_number+1)

            count_numbers = dealership.car_number.count(selection)
            if dealership.car_number.count(selection) > 1:
              print(" This item has been added recently.....")

            if count_numbers < 2:
              dealership.add_vehicles1(car)
              features_car.append(model_name)

            count = 0
            new_list = []
            for number in dealership.car_number:
              if number == selection:
                if count == 0:
                  new_list.append(number)
                  count += 1
              else:
                new_list.append(number)
            dealership.car_number = new_list
            break
      else:
        print("Invalid selection")
      option = int(input(" [1] Selected car #    [2] Exit.\n Option: "))
      if option == 2:
        break

    except ValueError:
      print(" Invalid input, please enter a number.")
      continue

if __name__ == '__main__':
  luxury_car()
  # pass