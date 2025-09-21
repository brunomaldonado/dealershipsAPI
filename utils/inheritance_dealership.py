import random

from utils.config import indentation_title2, indentation_title4, indentation_title5, car_object, motor_object, indentation_title01, indentation_title02, indentation_title03, indentation_title04, indentation_title05, indentation_title06, indentation_title07, textwrap_name, textwrap_message

class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'

class Vehicle:
  def __init__(self, name, brand, model):
    self.name = name
    self.brand = brand
    self.model = model
    self.is_available = True

  def sell(self):
    if self.is_available:
      self.is_available = False
      #print(f" The {self.name} {self.brand} {self.model} has been sold ")
      message = f"{bcolors.OKGREEN}The vehicle {self.name} {self.brand} {self.model} has been sold.{bcolors.ENDC}"
      print(f"\n{textwrap_message(message)}\n")
    else:
      #print(f" The {self.name} {self.brand} {self.model} is not available")
      message = f"The vehicle {self.name} {self.brand} {self.model} is not available{bcolors.ENDC}"
      print(f"\n{textwrap_message(message)}\n")


  def check_available(name):
    return name.is_available

  def get_price(self):
    return self.price

  def message(self):
    return " All the vehicles have been sold"

  def start_engine(self):
    raise NotImplementedError("This methods should be implement for sub-class")

  def stop_engine(self):
    raise NotImplementedError("This methods should be implement for sub-class")


class Car(Vehicle):
  def start_engine(self):
    if not self.is_available:
      return f"{self.name} {self.brand} {self.model} car is running"
    else:
      return f"The {self.name} {self.brand} {self.model} car is not running"

  def stop_engine(self):
    if not self.is_available:
      return f"{self.name} {self.brand} {self.model} car is stopped"
    else:
      return f"The {self.name} {self.brand} {self.model} car is not available"

class Motorcycle(Vehicle):
  def start_engine(self):
    if not self.is_available:
      return f"{self.name} {self.brand} {self.model} motorcycle is running"
    else:
      return f"The {self.name} {self.brand} {self.model} motorcycle is not running"

  def stop_engine(self):
    if not self.is_available:
      return f"{self.name} {self.brand} {self.model} motorcycle is stopped"
    else:
      return f"The {self.name} {self.brand} {self.model}motorcycle is not available"

class Trucks(Vehicle):
  def start_engine(self):
    if not self.is_available:
      return f"{self.name} {self.brand} {self.model} trucks is running"
    else:
      return f"The {self.name} {self.brand} {self.model} trucks is not running"

  def stop_engine(self):
    if not self.is_available:
      return f"{self.name} {self.brand} {self.model} trucks is stopped"
    else:
      return f"The {self.name} {self.brand} {self.model} trucks is not available"

class Customer:
  def __init__(self, name):
    self.name = name
    self.purchased_vehicles = []

  def buy_vehicle(self, vehicle: Vehicle):
      if vehicle.check_available():
        vehicle.sell()
        self.purchased_vehicles.append(vehicle)
      else:
        #print(f"\n Sorry this {vehicle.name} {vehicle.brand} {vehicle.model} is not available")
        message = f"{bcolors.FAIL}Sorry, the {vehicle.name} {vehicle.brand} {vehicle.model} vehicle is not available.{bcolors.ENDC}"
        print(f"\n{textwrap_message(message)}\n")


  def inquire_vehicle1(self, vehicle: Vehicle):
    availability = f"{bcolors.HEADER}is Available{bcolors.ENDC}" if vehicle.check_available() else f"{bcolors.FAIL}is Not Available{bcolors.ENDC}"
    message = f"{bcolors.OKCYAN}The {vehicle.name} {vehicle.brand} {vehicle.model} vehicle {availability}.{bcolors.ENDC}"
    print(f"\n{textwrap_message(message)}\n")

    # print("car_object...", car_object)
    if vehicle.check_available():
      random_year = random.randint(2022, 2024)
      spacing_line = " " * 15
      print("" * 1, "-" * 53)
      # print(f" Year: {car_object[0]['make_model_trim']['year']}         Create: {car_object[0]['make_model_trim']['created']}")
      print(f" Year: {random_year}         Create: {car_object[0]['make_model_trim']['created']}")
      print(f" Name: {car_object[0]['make_model_trim']['make_model']['make']['name']}")
      print(f" Design: {car_object[0]['make_model_trim']['name']}")
      print(f" Performance: {car_object[0]['make_model_trim']['make_model']['name']}")
      print("\n Key Specifications.")
      print(f" Engine: {car_object[0]['engine_type'].capitalize()}")
      print(f" Power: {car_object[0]['horsepower_rpm']} horsepower")
      print(f" Torque: {car_object[0]['torque_ft_lbs']} lb-ft")
      print(f" Transmission: {car_object[0]['transmission']}")
      print(f" Fuel Type: {car_object[0]['fuel_type'].capitalize()}")
      print(f" Drive Type: {car_object[0]['drive_type'].capitalize()}")
      print(f" Cam Type: {car_object[0]['cam_type']}")
      message = f" Description: {car_object[0]['make_model_trim']['description']}"
      print(indentation_title2(message))
      print(f"\n {spacing_line}Price: ${car_object[0]['price']} (US starting price)\n")

  def inquire_vehicle2(self, vehicle: Vehicle):
    availability = f"{bcolors.HEADER}is Available{bcolors.ENDC}" if vehicle.check_available() else f"{bcolors.FAIL}is Not Available{bcolors.ENDC}"
    message = f"{bcolors.OKCYAN}The {vehicle.name} {vehicle.brand} {vehicle.model} vehicle {availability}.{bcolors.ENDC}"
    print(f"\n{textwrap_message(message)}\n")

    # print(motor_object)
    if 'power' in motor_object[0]:
      power = motor_object[0]['power']
    else:
      power = f"no data"
    if 'torque' in motor_object[0]:
      torque = motor_object[0]['torque']
    else:
      torque = f"no data"
    if 'bore_stroke' in motor_object[0]:
      bore_stroke = motor_object[0]['bore_stroke']
    else:
      bore_stroke = f"no data"
    if 'compression' in motor_object[0]:
      compression = motor_object[0]['compression']
    else:
      compression = f"no data"
    if 'valves_per_cylinder' in motor_object[0]:
      valves_per_cylinder = motor_object[0]['valves_per_cylinder']
    else:
      valves_per_cylinder = f"no data"
    if 'fuel_system' in motor_object[0]:
      fuel_system = motor_object[0]['fuel_system']
    else:
      fuel_system = f"no data"
    if 'fuel_control' in motor_object[0]:
      fuel_control = motor_object[0]['fuel_control']
    else:
      fuel_control = f"no data"
    if 'ignition' in motor_object[0]:
      ignition = motor_object[0]['ignition']
    else:
      ignition = f"no data"
    if 'cooling' in motor_object[0]:
      cooling = motor_object[0]['cooling']
    else:
      cooling = f"no data"
    if 'lubrication' in motor_object[0]:
      lubrication = motor_object[0]['lubrication']
    else:
      lubrication = f"no data"
    if 'fuel_consumption' in motor_object[0]:
      fuel_consumption = motor_object[0]['fuel_consumption']
    else:
      fuel_consumption = f"no data"
    if 'emission' in motor_object[0]:
      emission = motor_object[0]['emission']
    else:
      emission = f"no data"
    if 'rear_suspension' in motor_object[0]:
      rear_suspension = motor_object[0]['rear_suspension']
    else:
      rear_suspension = f"no data"
    if 'fuel_capacity' in motor_object[0]:
      fuel_capacity =motor_object[0]['fuel_capacity']
    else:
      fuel_capacity = f"no data"

    if vehicle.check_available():
      initial_line = " " * 42
      spacing_line = " " * 17
      print("" * 1, "-" * 53)
      print(f" {initial_line}Year: {motor_object[0]['year']}")
      print(f" Name: {motor_object[0]['make']}")
      print(f" Design: {motor_object[0]['model']}")
      print(f" Performance: {motor_object[0]['type']}")
      print("\n Key Specifications.")
      print(f" Engine: {motor_object[0]['engine']}")
      print(f" Power: {power} horsepower")
      print(indentation_title01(f" Torque: {torque} lb-ft"))
      print(indentation_title02(f" Bore Stroke: {bore_stroke}"))
      print(f" Valves per Cylinder: {valves_per_cylinder} Compression: {compression}")
      print(indentation_title02(f" Fuel System: {fuel_system}"))
      print(f" Fuel Control: {fuel_control}")
      print(f" Ignition: {ignition}")
      print(indentation_title02(f" Lubrication: {lubrication}  Cooling: {cooling}  Gearbox: {motor_object[0]['gearbox']}"))
      print(f" Transmission: {motor_object[0]['transmission']}")
      print(indentation_title03(f" Fuel Consumption: {fuel_consumption}"))
      print(indentation_title04(f" Emission: {emission}"))
      print(indentation_title03(f" Front Suspension: {motor_object[0]['front_suspension']}"))
      print(indentation_title05(f" Rear Suspension: {rear_suspension}"))
      print(indentation_title06(f" Front Brakes: {motor_object[0]['front_brakes']}"))
      print(indentation_title07(f" Rear Brakes: {motor_object[0]['rear_brakes']}"))
      print(f" Fuel Capacity: {fuel_capacity}")
      print(f" Starter: {motor_object[0]['starter']}")
      print(f"\n {spacing_line}Price: ${motor_object[0]['price']} (US starting price)\n")

  def inquire_vehicle3(self, vehicle: Vehicle):
    availability = f"{bcolors.HEADER}is Available{bcolors.ENDC}" if vehicle.check_available() else f"{bcolors.FAIL}is Not Available{bcolors.ENDC}"
    message = f"{bcolors.OKCYAN}The {vehicle.name} {vehicle.brand} {vehicle.model} vehicle {availability}.{bcolors.ENDC}"
    print(f"\n{textwrap_message(message)}\n")

class Dealership:
  def __init__(self):
    self.cars_inventory = []
    self.motorcycles_inventory = []
    self.trucks_inventory = []
    self.customers = []
    self.car_number = []
    self.motor_number = []
    self.truck_number = []
    self.selected_number = []

  def add_vehicles1(self, vehicle: Vehicle):
    self.cars_inventory.append(vehicle)
    message = f"{bcolors.OKCYAN}The Car {vehicle.name} {vehicle.brand} {vehicle.model} has been added to the inventory.{bcolors.ENDC}"
    print(f"\n{textwrap_message(message)}\n")


  def add_vehicles2(self, vehicle: Vehicle):
    self.motorcycles_inventory.append(vehicle)
    message = f"{bcolors.OKCYAN}The Motorcycle {vehicle.name} {vehicle.brand} {vehicle.model} has been added to the inventory.{bcolors.ENDC}"
    print(f"\n{textwrap_message(message)}\n")

  def add_vehicles3(self, vehicle: Vehicle):
    self.trucks_inventory.append(vehicle)

  def register_customers(self, customer: Customer):
    self.customers.append(customer)
    message = f"{bcolors.OKBLUE}{customer.name} customer has been registered at the dealership{bcolors.ENDC}"
    print(f"\n{textwrap_message(message)}\n")

  def show_available_vehicles(self):
    print("" * 1, "-" * 54)
    print(f"        Vehicles Available on the Dealership.".upper())
    print("" * 1, "-" * 54)

    formatted_titles1 = []
    formatted_titles2 = []
    formatted_titles3 = []

    if len(self.cars_inventory) == 0:
      print("\n\n You don't have any luxury cars added yet.\n")
    else:
      print("\n Cars available.\n")

      for idx, (number, car) in enumerate(zip(self.car_number, self.cars_inventory), start=1):
        if car.check_available():
          formatted_titles1.append(f"[{number:2}] {car.name} {car.brand} {car.model}")

      for idx, formatted_title in enumerate(formatted_titles1, start=1):
        wrapped_lines = textwrap_name(formatted_title)
        print(f" {bcolors.OKCYAN}{idx:2}{bcolors.ENDC} {wrapped_lines[0].lstrip()}")

        for line in wrapped_lines[1:]:
          print(line)

    if len(self.motorcycles_inventory) == 0:
      # print("\n Motorcycles available.")
      print("\n\n You don't have any Motorcycles added yet.\n")
      # pass
    else:
      print("\n Motorcycles available.\n")

      for idx, (number, motorcycle) in enumerate(zip(self.motor_number, self.motorcycles_inventory), start=1):
        if motorcycle.check_available():
          # print(f"{bcolors.OKCYAN}{idx:2}{bcolors.ENDC} [{number:3}]  {motorcycle.name} {motorcycle.brand} {motorcycle.model}")
          formatted_titles2.append(f"[{number:3}] {motorcycle.name} {motorcycle.brand} {motorcycle.model}")

      for idx, formatted_title in enumerate(formatted_titles2, start=1):
        wrapped_lines = textwrap_name(formatted_title)
        print(f" {bcolors.OKCYAN}{idx:2}{bcolors.ENDC} {wrapped_lines[0].lstrip()}")

        for line in wrapped_lines[1:]:
          print(line)

    if len(self.trucks_inventory) == 0:
      pass
    else:
      print("\n Trucks available.\n")

      for idx, (num, truck) in enumerate(zip(self.truck_number, self.trucks_inventory), start=1):
        if truck.check_available():
          formatted_titles3.append(f" [{num:3}] {truck.name} {truck.brand} {truck.model}")

      for idx, formatted_title in enumerate(formatted_titles3, start=1):
        wrapped_lines = textwrap_name(formatted_title)
        print(f" {bcolors.OKCYAN}{idx:2}{bcolors.ENDC} {wrapped_lines[0].lstrip()}")
        for line in wrapped_lines[1:]:
          print(line)





