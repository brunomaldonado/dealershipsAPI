import random
import sys
import time
from utils import server
from utils.config import car_object, motor_object, indentation_title4
from utils.inheritance_dealership import Car, Motorcycle, Trucks, Customer, Dealership
from rapid.trucks import trucks_data
from datetime import datetime

def print_options():
  print()
  options = [
    " [1] Add inventory",
    " [2] Show Inventory",
    " [3] Register Customer",
    " [4] Customer Data",
    " [5] Exit"
  ] 
  
  for i in range(0, len(options), 3):
    print("{:<15} {:<15} {:<15}".format(
      *options[i:i+3], *[''] * (3 - len(options[i:i+3]))
    ))

def print_service_line():
  print()
  options = [
    " [1] Luxury Cars"
    " [2] Luxury Motorcycles",
    " [3] Exit",
  ]

  for i in range(0, len(options), 3):
    print("{:<15} {:<15} {:<15}".format(
      *options[i:i+3], *[''] * (3 - len(options[i:i+3]))
    ))

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
    list_car_brands = []
    car_price = []
    lower_bound = 23950
    upper_bound = 80790
    random_numbers = [random.uniform(lower_bound, upper_bound) for _ in range(100)]

    for price in random_numbers:
      on_sale = int(price)
      prices = "{:,.2f}".format(on_sale)
      car_price.append(prices)

    # print(car_price)
    for idx, item in enumerate(data, start=1):
      list_car_brands.append(f"{item['make_model_trim']['make_model']['make']['name']} {item['make_model_trim']['make_model']['name']} {item['make_model_trim']['name']}")

    seen = set()
    unique_data = []
    for car in list_car_brands:
      if car not in seen:
        seen.add(car)
        unique_data.append(car)
      else:
        if unique_data.count(car) < 1:
          unique_data.append(car)

    for idx, car in enumerate(unique_data, start=1):
      print(f" [{idx:2}] {car}")
      
    def select_index(selection):
      if 1 <= selection <= len(list_car_brands) or 1 <= selection <= len(prices):
        return selection - 1
      else:
        return None
     
    while True:
      selection = int(input("\n Select car #: "))
      selected_number = select_index(selection)
      car_number = selected_number + 1
      if isinstance(selected_number, int):
        car_brands = unique_data[selected_number]
        for model_name in data:
          car_models = f"{model_name['make_model_trim']['make_model']['make']['name']} {model_name['make_model_trim']['make_model']['name']} {model_name['make_model_trim']['name']}"
          if car_brands == car_models:
            model_name['price'] = car_price[selected_number]
            features_car.append(model_name)
            # print(f"CAR... OBJECT {model_name}")
            name = model_name['make_model_trim']['make_model']['make']['name']
            brand = model_name['make_model_trim']['make_model']['name']
            model = model_name['make_model_trim']['name']
            #price = car_price[selected_number]
            # print(name, brand, model, price)
            model_name = Car(name, brand, model)
            dealership.car_number.append(car_number) 
            count_numbers = dealership.car_number.count(selection)
            if count_numbers < 2:
              dealership.add_vehicles1(model_name)
              
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
      option = int(input(" [1] Select car #    [2] Exit.\n Option: "))
      if option == 2:
        break

  # motorcycle request.......................................................................
  features_motorcycle = []
  def luxury_motorcycle():
    motorcycle_names = ['BMW', 'DUCATI', 'HONDA', 'HARLEY-DAVIDSON', 'KAWASAKI', 'SUZUKI']
    motorcycle_data_lst = []
    data = []
    list_motorcycle_brands = []
    list_motorcycle_models = []
    motorcycle_price = []

    spinner = ['-', '\\', '|', '/']
    # spinner = ['..', '../', '.-', '...', '.\\', '..|', '..']
    lower_bound = 24150
    upper_bound = 32900
    initial_spacing = "" * 2
    random_numbers = [random.uniform(lower_bound, upper_bound) for _ in range(122)]
    for value in random_numbers:
      on_sale = int(value)
      formatted_price = "{:,.2f}".format(on_sale)
      price = formatted_price.replace(',', 'X').replace('.', ',').replace('X', '.')
      motorcycle_price.append(price)
        
    for make_name in motorcycle_names:
      motorcycle_data = server.motorcycles(make_name)
      motorcycle_data_lst.append(motorcycle_data)
      for frame in spinner:
        print(initial_spacing, end=" ", flush=True)
        sys.stdout.write('\r' + frame)
        sys.stdout.flush()
        time.sleep(0.1)
    print()
    for sublist in motorcycle_data_lst:
      for obj_lst in sublist:
        data.append(obj_lst)
    for item in data:
      list_motorcycle_brands.append(f"{item['make']} {item['model']} {item['type']}")

    character = '/'
    count = 1
    for brand_name in list_motorcycle_brands:
      if character not in brand_name:
        brand_model_type = f" [{count:3}] {brand_name}"
        print(indentation_title4(brand_model_type))
        list_motorcycle_models.append(brand_name)
        count += 1 

    def select_index(selection):
      if 1 <= selection <= len(list_motorcycle_brands):
        return selection - 1
      else:
        return None

    while True:
      selection = int(input("\n Select motorcycle #: "))
      selected_number = select_index(selection)
      motorcycle_number = selected_number + 1
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
            dealership.motor_number.append(motorcycle_number)
            #........
            count_numbers = dealership.motor_number.count(selection)
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
      
      option = int(input(" [1] Select motorcycle #     [2] Exit.\n Option: "))
      if option == 2:
        break
  
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
      option = int(input("\n Enter option: "))
      if option == 1:
        # add inventory [] line services
        print_service_line()
        selected_option = int(input("\n Option: "))
        if isinstance(selected_option, int):
          if selected_option == 1:
            print("\n LUXURY CARS \n")
            luxury_car()
          elif selected_option == 2:
            print("\n LUXURY MOTORCYCLES")
            luxury_motorcycle()
        else:
          print(" Invalid selection")

      elif option == 2:
        if len(dealership.customers) == 0:
          customer_name = 'Katharine Bennet'
        else:
          customer_name = dealership.customers[0].name
        spacing = " " * 15 
        initial_spacing = " " * 38
        print()
        print(f" {initial_spacing}{date_time()}")
        print("" * 1, "-" * 53)
        print(f" INVENTORY {spacing}Customer: 🧑🏼‍⚖️ {customer_name}")
        # print("" * 1, " " * 15, "-" * 20, )
        # print("" * 1, "-" * 53, )
        

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
              selection = int(input(" Vehicle # selector: "))

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
                      break
                    else:
                      print(" Please enter y or n")
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
                print(" Invalid selection, try again!")
            
            except ValueError:
              print(" Invalid input, please enter a number.")
              break
            except KeyboardInterrupt:
              break
            
          elif question == 'n':
            break
          else:
            print(" Please enter y or n")

      elif option == 3:
        register_customer1()
      elif option == 4:
        if len(dealership.customers) == 0:
          customer_name = 'Katharine Bennet'
        else:
          customer_name = dealership.customers[0].name
        spacing = " " * 11
        initial_spacing = " " * 38
        print()
        print(f" {initial_spacing}{date_time()}")
        print("" * 1, "-" * 53)
        print(f" CUSTOMER DATA {spacing}Customer: 🧑🏼‍⚖️ {customer_name}")
        print("" * 1, "-" * 53)
        # print(f" {initial_spacing}Date: August 24, 2024")
        # print(f" {initial_spacing}{date_time()}")
        # print()
        
        seen = set()
        result = []
        for car in customer.purchased_vehicles:
          if car not in seen:
            seen.add(car)
            result.append(car)
          else:
            if result.count(car) < 1:
              result.append(car)
              
        print("\n List of purchased vehicles\n")

        if len(result) == 0:
          print("           |Has no purchased vehicles...!|\n")
        else:
          for idx, car in enumerate(result, start=1):
            print(f" {idx:2}.- {car.name} {car.brand} {car.model}")   

          print("\n")  
      elif option == 5:
        break
    except ValueError:
      print(" Invalid input. Please enter a number")
 
if __name__ == '__main__':
 main()