import pandas as pd 
data = {'name': ['John', 'Anna', 'Mike'], 'age': [28, 22, 32], 'salary': [50000, 60000, 70000]}
# x = pd.read_csv('CC_data.csv') << any excel data >>
x=pd.DataFrame(data)
print(x)

# print(x.to_string())

dict_data = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
print(pd.DataFrame(dict_data))
print(f'version {pd.__version__}')

