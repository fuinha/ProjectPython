import requests

response = requests.get('http://208.117.87.29:3333/api/v0/games')

data = response.json()

#for user in data['machineName']
#    print(user['name']['first'])

def greet(greeting, name):
    """[summary]
    
    Arguments:
        greeting {string} -- a greet world
        name {string} -- a person name
    
    Returns:
        string -- greeting with name
    """
    return f'{greeting} {name}'

print(greet('hello','world'))

