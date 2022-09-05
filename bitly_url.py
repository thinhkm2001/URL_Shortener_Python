import bitly_api
 
BITLY_ACCESS_TOKEN ="#################################"
 
x = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN)

url_input = input("Enter the url: ") 
response = x.shorten(url_input)
print(response)
