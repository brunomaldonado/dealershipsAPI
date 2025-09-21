# import sys
# import os
# import sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import server
import random
from db.db_luxury_motorcycle import motorcycle_data_lst
from utils.config import textwrap_title
from utils.inheritance_dealership import Motorcycle, Dealership


def luxury_motorcycle():
  dealership = Dealership()
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

  features_motorcycle = []

  while True:
    try:
      selection = int(input("\n Selected motorcycle #: "))
      selected_number = select_index(selection)
      # motorcycle_number = selected_number + 1
      #print(f"\n You selected option {selection}\n selected_number {selected_number}\n")
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

      option = int(input(" [1] Selected motorcycle #     [2] Exit.\n Option: "))
      if option == 2:
        print(dealership.motor_number)
        break

    except ValueError:
      print(" Invalid input, please enter a number.")
      continue

# if __name__ == '__main__':
#   luxury_motorcycle()


