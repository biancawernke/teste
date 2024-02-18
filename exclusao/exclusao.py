import csv

import requests

with open('verifica_get_obras.csv') as file:
  reader=csv.reader(file, delimiter=',')

  for linha in reader:
    

   
    headers = {
      'User-Access': '3HGZDbySGFqZzUcNYVn15g==',
      'Authorization': 'Bearer 244d852e-59b5-4221-9537-b179a00a6174',
      'Content-Type': 'application/json'
    } 

    url = "https://obras.betha.cloud/obras/api/obras/"+linha[0]

    response = requests.request("DELETE", url, headers=headers)
    print(linha[0],':',response.text)
    break