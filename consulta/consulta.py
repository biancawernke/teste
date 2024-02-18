import requests
import json
import csv

url = "https://obras.betha.cloud/obras/api/obras?limit=1000"

headers = {
  'User-Access': '3HGZDbySGFqZzUcNYVn15g==',
  'Authorization': 'Bearer 244d852e-59b5-4221-9537-b179a00a6174',
  'Content-Type': 'application/json'
}

with open('verifica_get_obras.csv', 'w', newline='') as file:
  writer = csv.writer(file)

  response = requests.request("GET", url, headers=headers)
  response_json = json.loads(response.text)

  for obra in response_json['content']:
    print( obra['id'])
    writer.writerow([obra['id']])
