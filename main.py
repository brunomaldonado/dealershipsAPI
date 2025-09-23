import random
from utils import server
from utils.config import car_object, motor_object, indentation_title4, textwrap_title
from utils.inheritance_dealership import Car, Motorcycle, Trucks, Customer, Dealership
from rapid.trucks import trucks_data
from datetime import datetime
from db.db_luxury_motorcycle import motorcycle_data_lst
from db.db_luxury_cars import luxury_car_lst


def print_options():
  print()
  options = [
    " [1] Add inventory      ",
    " [2] Show Inventory",
    " [3] Register Customer  ",
    " [4] Customer Data  ",
    " [5] Exit"
  ]

  layout = [2, 3]
  index = 0
  for col in layout:
    row = options[index:index+col]
    print("".join("{:<15}".format(opt) for opt in row))
    index += col

def print_service_line():
  print()
  options = [
    " [1] Luxury Cars  ",
    " [2] Luxury Motorcycles  ",
    " [3] Exit",
  ]

  print("".join("{:<15}".format(opt) for opt in options))

def main():
  dealership = Dealership()

  def date_time():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%B %d, %Y")
    return formatted_date

  def register_customer1():
    name = input("\n Enter your name: ")
    customer = Customer(name)
    dealership.register_customers(customer)

  customer = Customer("Katharine Bennet")
  dealership.register_customers(customer)

  # cars request .........................................................................
  features_car = []
  def luxury_car():
    data = server.car_engines()
    car_price = []

    lower_bound = 23950
    upper_bound = 80790
    random_numbers = [random.uniform(lower_bound, upper_bound) for _ in range(100)]

    for price in random_numbers:
      on_sale = int(price)
      prices = "{:,.2f}".format(on_sale)
      car_price.append(prices)

    # print(car_price)
    list_car_models = list(dict.fromkeys(luxury_car_lst))

    # print(f"luxury_car_lst {len(luxury_car_lst)}\n unique data {len(unique_data)}")

    for idx, car in enumerate(list_car_models, start=1):
      print(f" [{idx:2}] {car}")

    def select_index(selection):
      if 1 <= selection <= len(list_car_models) or 1 <= selection <= len(prices):
        return selection - 1
      else:
        return None

    while True:
      try:
        selection = int(input("\n Selected car [#]: "))
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
              features_car.append(model_name)
              # print(f"CAR... OBJECT {model_name}")
              name = model_name['make_model_trim']['make_model']['make']['name']
              brand = model_name['make_model_trim']['make_model']['name']
              model = model_name['make_model_trim']['name']
              # price = car_price[selected_number]
              # print(name, brand, model, price)
              car = Car(name, brand, model)

              dealership.car_number.append(selected_number + 1)

              count_numbers = dealership.car_number.count(selection)
              if dealership.car_number.count(selection) > 1:
                print(" This item has been added recently.....\n")

              if count_numbers < 2:
                dealership.add_vehicles1(car)
                # features_car.append(model_name)

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
        option = int(input(" [1] Selected car [#]  [2] Exit.\n Option: "))
        if option == 2:
          print("\n")
          break

      except ValueError:
        print(" Invalid input, please enter a number.")
        continue


  # motorcycle request.......................................................................
  features_motorcycle = []
  def luxury_motorcycle():
    motorcycle_names = ['BMW', 'DUCATI', 'HONDA', 'HARLEY-DAVIDSON', 'KAWASAKI', 'SUZUKI']
    # motorcycle_names = ['DUCATI', 'BMW', 'KAWASAKI', 'SUZUKI']
    # motorcycle_data_lst = []
    data = []
    list_motorcycle_brands = []
    list_motorcycle_models = []
    motorcycle_price = []

    spinner = ['-', '\\', '|', '/']
    # spinner = ['..', '../', '.-', '...', '.\\', '..|', '..']

    # 3.254,00
    lower_bound = 263805
    upper_bound = 594713

    random_numbers = [random.uniform(lower_bound, upper_bound) for _ in range(176)]
    # print(random_numbers)

    for value in random_numbers:
      on_sale = value
      formatted_price = "{:,.2f}".format(on_sale / 176)
      price = formatted_price.replace(',', 'X').replace('.', ',').replace('X', '.')
      motorcycle_price.append(price)

    # print(f"DATA {motorcycle_data_lst} \n\nLEN {len(motorcycle_data_lst)}")

    for sublist in motorcycle_data_lst:
      for obj_lst in sublist:
        data.append(obj_lst)

    for item in data:
      list_motorcycle_brands.append(f"{item['make']} {item['model']} {item['type']}")

    # print(data)
    elements = ['Honda CB125F                                            Allround',
                'Honda CB125R                                           Naked bike',
                'Honda CB125e                                           Naked bike',
                'Honda CB150F                                            Allround']

    def filter_new_brands(elements, items):
      elements_clean = [" ".join(e.split()) for e in elements]
      new_brands = []
      for d in items:
        d_clean = " ".join(d.split())
        if d_clean not in elements_clean:
          new_brands.append(d)

      return new_brands

    new_data = filter_new_brands(elements, list_motorcycle_brands)
    # print(new_data)

    counter = 1
    for brand_name in list_motorcycle_brands:
      if "Honda CB125F " <= brand_name <= "Honda CB150F Allround":
        continue
      if brand_name == "Honda CB200X Sport":
        counter = 73
      wrapped_lines = textwrap_title(brand_name)
      print(f" [{counter:3}] {wrapped_lines[0].lstrip()}")
      for line in wrapped_lines[1:]:
        print(line)
      list_motorcycle_models.append(brand_name)
      counter += 1

    # print(f"list_motorcycle_brands:\n{len(new_data)}\n\nlist_motorcycle_models:\n{len(list_motorcycle_models)}")

    def select_index(selection):
      if 1 <= selection <= len(new_data):
        return selection - 1
      else:
        return None

    while True:
      try:
        selection = int(input("\n Selected motorcycle [#]: "))
        selected_number = select_index(selection)
        if selected_number is None:
          print(" Invalid selection, please try again.")
          continue
        if isinstance(selected_number, int):
          motorcycle_brand = list_motorcycle_models[selected_number]
          for model_name in data:
            motorcycle_model = f"{model_name['make']} {model_name['model']} {model_name['type']}"

            if motorcycle_brand == motorcycle_model:
              model_name['price'] = motorcycle_price[selected_number]
              # print(" model name", model_name) # return object data
              # features_motorcycle.append(model_name)
              name = model_name['make']
              brand = model_name['model']
              model = model_name['type']
              # print(name, brand, model)
              motor = Motorcycle(name, brand, model)

              dealership.motor_number.append(selected_number + 1)

              count_numbers = dealership.motor_number.count(selection)
              if dealership.motor_number.count(selection) > 1:
                print(" This item has been added recently...\n")
                # dealership.motor_number.pop()

              if count_numbers < 2:
                dealership.add_vehicles2(motor)
                features_motorcycle.append(model_name)

              count = 0
              new_list = []
              for number in dealership.motor_number:
                if number == selection:
                  if count == 0:
                    new_list.append(number)
                    count += 1
                else:
                  new_list.append(number)
              dealership.motor_number = new_list
              break
        else:
          print("invalid selection")

        option = int(input(" [1] Selected motorcycle [#]  [2] Exit.\n Option: "))
        if option == 2:
          print("\n")
          break
      except ValueError:
        print(" Invalid input, please enter a number.")
        continue

  # Trucks data ..........................................
  def luxury_truck():
    random_numbers = random.sample(range(123, 187), 6)
    sorted_numbers = sorted(random_numbers)
    name_trucks = []

    for idx, truck in enumerate(trucks_data, start=1):
      name_trucks.append(f"{truck['make']} {truck['model']} {truck['type']}")
      name = truck['make']
      brand = truck['model']
      model = truck['type']
      # price = item['price']
      # print(name, brand, model, price)
      truck = Trucks(name, brand, model)
      dealership.add_vehicles3(truck)
      for number in sorted_numbers:
        dealership.truck_number.append(number)

  luxury_truck()

  while True:
    try:
      print_options()
      option = int(input(" Enter option: "))
      if option == 1:
        print_service_line()
        selected_option = int(input(" Option: "))
        if isinstance(selected_option, int):
          if selected_option == 1:
            print(f"\n{' ' * 1}{'-' * 54}")
            print(f"{' ' * 1}LUXURY CARS\n {'-' * 54}\n")
            #print(" LUXURY CARS")
            #print("" * 1, "-" * 53)
            #print("\n")
            luxury_car()
          elif selected_option == 2:
            print(f"\n{' ' * 1}{'-' * 54}")
            print(f"{' ' * 1}LUXURY MOTORCYCLES\n {'-' * 54}\n")
            luxury_motorcycle()
        else:
          print(" Invalid selection")

      elif option == 2:
        if len(dealership.customers) == 0:
          customer_name = 'Katharine Bennet'
        else:
          customer_name = dealership.customers[0].name
        spacing = " " * 15
        initial_spacing = " " * 34
        print()
        print(f" {initial_spacing}{date_time()}")
        print("" * 1, "-" * 54)
        print(f" INVENTORY {spacing}\n Customer: {customer_name}")
        # print("" * 1, " " * 15, "-" * 20, )
        print("" * 1, "-" * 54, )

        # print(f"Dealership motor number: {dealership.motor_number}")

        car_id_count = {}
        car_details = []
        for item in features_car:
          item_id = item.get('id')
          if item_id:
            car_id_count[item_id] = car_id_count.get(item_id, 0) + 1
            if car_id_count[item_id] != 2:
              car_details.append(item)
          else:
            car_details.append(item)
        features_car = car_details

        while True:
          dealership.show_available_vehicles()
          question = input("\n Do you like to inquire the details? (y/n) : ").strip().lower()
          if question == 'y':
            try:
              selection = int(input(" Selected vehicle #: "))

              def inquire_car_buy():
                index = dealership.car_number.index(selection)
                car = features_car[index]
                car_object.append(car)
                car_index = dealership.cars_inventory[index]
                customer.inquire_vehicle1(car_index) # customer inquire a car_index
                ask = input(" Do you want to buy this vehicle? (y/n) : ").strip().lower()
                while True:
                  try:
                    if ask == 'y':
                      customer.buy_vehicle(car_index)
                      customer.purchased_vehicles.append(car_index)
                      car_object.clear()
                      break
                    elif ask == 'n':
                      car_object.clear()
                      print("\n")
                      break
                    else:
                      print(" Please enter y or n")
                      break
                  except ValueError:
                    break

              def inquire_motor_buy():
                index = dealership.motor_number.index(selection)
                motor = features_motorcycle[index]
                motor_object.append(motor)
                motor_index = dealership.motorcycles_inventory[index]
                customer.inquire_vehicle2(motor_index) # customer inquire a motor_index
                ask = input(" Do you want to buy this vehicle? (y/n) : ").strip().lower()
                while True:
                  try:
                    if ask == 'y':
                      customer.buy_vehicle(motor_index)
                      customer.purchased_vehicles.append(motor_index)
                      motor_object.clear()
                      break
                    elif ask == 'n':
                      motor_object.clear()
                      print("\n")
                      break
                    else:
                      print(" Please enter y or n\n")
                      break
                  except ValueError:
                    break
              def inquire_truck_buy():
                index = dealership.truck_number.index(selection)
                truck_index = dealership.trucks_inventory[index]
                customer.inquire_vehicle3(truck_index) # customer inquire a car_index
                ask = input(" Do you want to buy this vehicle? (y/n) : ").strip().lower()
                while True:
                  try:
                    if ask == 'y':
                      customer.buy_vehicle(truck_index)
                      customer.purchased_vehicles.append(truck_index)
                      # dealership.show_available_vehicles()
                      # truck_object.clear()
                      break
                    elif ask == 'n':
                      # truck_object.clear()
                      print("\n")
                      break
                    else:
                      print(" Please enter y or n")
                      break
                  except ValueError:
                    break

              if selection in dealership.car_number and selection in dealership.motor_number:
                option = int(input("\n [1] Car [2] Motorcycle [3] Exit\n Option: "))
                if option == 1:
                  inquire_car_buy()
                if option == 2:
                  inquire_motor_buy()
                if option == 3:
                  break
              elif selection in dealership.car_number:
                inquire_car_buy()
              elif selection in dealership.motor_number:
                inquire_motor_buy()
              elif selection in dealership.truck_number:
                inquire_truck_buy()
              else:
                print(" Invalid selection, try again!\n")

            except ValueError:
              print(" Invalid input, please enter a number.")
              break
            except KeyboardInterrupt:
              break

          elif question == 'n':
            print("\n")
            break
          else:
            print(" Please enter y or n\n\n")

      elif option == 3:
        register_customer1()
      elif option == 4:
        if len(dealership.customers) == 0:
          customer_name = 'Katharine Bennet'
        else:
          customer_name = dealership.customers[0].name
        spacing = " " * 11
        initial_spacing = " " * 34
        print()
        print(f" {initial_spacing}{date_time()}")
        print("" * 1, "-" * 53)
        print(f" CUSTOMER DATA {spacing}\n Customer:  {customer_name}")
        print("" * 1, "-" * 53)

        purchased_vehicles = list(dict.fromkeys(customer.purchased_vehicles))

        print("\n List of purchased vehicles\n")

        if len(purchased_vehicles) == 0:
          print("           |Has no purchased vehicles...!|\n")
        else:
          for idx, vehicles in enumerate(purchased_vehicles, start=1):
            print(f" {idx:2} {vehicles.name} {vehicles.brand} {vehicles.model}")

          print("\n")
      elif option == 5:
        break
    except ValueError:
      print(" Invalid input. Please enter a number")

if __name__ == '__main__':
 main()
