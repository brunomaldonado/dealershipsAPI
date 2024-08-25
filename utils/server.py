from requests import get, post
import json

#  Cars requests
querystring = {"sort":"id","direction":"asc","year":"2020","verbose":"yes"}

headers = {
	"x-rapidapi-key": "627629bd6dmsha98c129e3532846p13d202jsna9dfd8219a65",
	"x-rapidapi-host": "car-api2.p.rapidapi.com"
}

def search_models():
  url = "https://car-api2.p.rapidapi.com/api/models"
  result = get(url, headers=headers, params=querystring)
  print(result)
  json_result = json.loads(result.content)
  # print(json_result)
  # print(json_result.keys())
  json_result = json_result['data']
  # json_result = json_result['data']['make']

  return json_result

def car_trims():
  url = "https://car-api2.p.rapidapi.com/api/trims"
  result = get(url, headers=headers, params=querystring)
  # print(result)
  json_result = json.loads(result.content)
  # print(json_result)
  json_result = json_result['data']

  return json_result

def car_engines():
  url = "https://car-api2.p.rapidapi.com/api/engines"
  result = get(url, headers=headers, params=querystring)
  json_result = json.loads(result.content)
  # print(json_result)
  # print(json_result.keys())
  json_result = json_result['data']

  return json_result


# Motorcycle requests

# headers1 = {
#   "x-rapidapi-key": "627629bd6dmsha98c129e3532846p13d202jsna9dfd8219a65",
#   "x-rapidapi-host": "cars-motorcycles-trucks-models-and-prices.p.rapidapi.com"
# }

# # querystring = {"id":"131","model":"4360","year":"2009-1"}

# def motocycle_brands():
#   url = "https://cars-motorcycles-trucks-models-and-prices.p.rapidapi.com/motos"
#   result = get(url, headers=headers1)
#   json_result = json.loads(result.content)
#   #print(json_result)
#   # print(json_result.keys())
#   json_result = json_result['motos']

#   return json_result


# #querystring = {"make":"Kawasaki","model":"Ninja"}

headers2 = {
  "x-rapidapi-key": "627629bd6dmsha98c129e3532846p13d202jsna9dfd8219a65",
  "x-rapidapi-host": "motorcycles-by-api-ninjas.p.rapidapi.com"
}

# def motorcycles():
def motorcycles(make):
  url = f"https://motorcycles-by-api-ninjas.p.rapidapi.com/v1/motorcycles?make={make}"
  # result = get(url, headers=headers, params=querystring)
  result = get(url, headers=headers2)
  json_result = json.loads(result.content)

  return json_result

# data = car_engines()
# print(f"\ndata {data}\nlen {len(data)}\n")

# motor = motorcycles('HONDA')
# print(motor)