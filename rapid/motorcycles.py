import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import server
import random
import time
import sys

def luxury_motorcycle():
  motorcycle_names = ['BMW', 'DUCATI', 'HONDA', 'HARLEY-DAVIDSON', 'KAWASAKI', 'SUZUKI']
  # motorcycle_names = ['DUCATI', 'BMW', 'KAWASAKI', 'SUZUKI']
  motorcycle_data_lst = []
  data = []
  list_motorcycle_brands = []
  list_motorcycle_models = []
  motorcycle_price = []

  spinner = ['-', '\\', '|', '/']
  # spinner = ['..', '../', '.-', '...', '.\\', '..|', '..']

  # 3.254,00
  lower_bound = 263805
  upper_bound = 594713
  initial_spacing = "" * 2

  random_numbers = [random.uniform(lower_bound, upper_bound) for _ in range(122)]
  # print(random_numbers)

  for value in random_numbers:
    on_sale = value
    formatted_price = "{:,.2f}".format(on_sale/100)
    price = formatted_price.replace(',', 'X').replace('.', ',').replace('X', '.')
    motorcycle_price.append(price)
      
  for make_name in motorcycle_names:
    motorcycle_data = server.motorcycles(make_name)
    motorcycle_data_lst.append(motorcycle_data)
    # print(f"DATA {motorcycle_name}\nlen: {len(motorcycle_name)}")
    for frame in spinner:
      print(initial_spacing, end=" ", flush=True)
      sys.stdout.write('\r' + frame)
      sys.stdout.flush()
      time.sleep(0.2)
  print()
    
  # print(f"DATA {motorcycle_data_lst} \n\nLEN {len(motorcycle_data_lst)}")

  for sublist in motorcycle_data_lst:
    for obj_lst in sublist:
      data.append(obj_lst)

  # print(data)
  for item in data:
    list_motorcycle_brands.append(f"{item['make']} {item['model']} {item['type']}")

  # for _ in range(10):
  #   for frame in spinner:
  #     sys.stdout.write('\r' + frame)
  #     sys.stdout.flush()
  #     time.sleep(0.1)

  # for name in list_motorcycle_brands:
  #   print(name)
    
  character = '/'
  count = 1
  for brand_name in list_motorcycle_brands:
    if character not in brand_name:
      print(f" [{count:3}] {brand_name}")
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
    # motorcycle_number = selected_number + 1
    if isinstance(selected_number, int):
      motorcycle_brand = list_motorcycle_models[selected_number]
      print(f"\n {motorcycle_brand}\n")
      for model_name in data:
        motorcycle_model = f"{model_name['make']} {model_name['model']} {model_name['type']}"

        if motorcycle_brand == motorcycle_model:
          model_name['price'] = motorcycle_price[selected_number]
          print(" model name", model_name)
    else:
      print("invalid selection")
    
    option = int(input("\n [1] Select motorcycle #     [2] Exit.\n Option: "))
    if option == 2:
      break

if __name__ == '__main__':
  luxury_motorcycle()