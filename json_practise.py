import json
bemor = {
  "ism": "Alijon Valiyev",
  "yosh": 30,
  "oila": True,
  "farzandlar": ("Ahmad","Bonu"),
  "allergiya": None,
  "dorilar": [
    {"nomi": "Analgin", "miqdori": 0.5},
    {"nomi": "Panadol", "miqdori": 1.2}
  ]
}

# with open('bemor.json','w') as f:
#     json.dump(bemor,f)

filename = 'bemor.json'
with open(filename) as f:
    kasal = json.load(f)
    
print(kasal)