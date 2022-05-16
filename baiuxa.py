import requests

img = '='

response_img = requests.get(img)

with open('you.jpg', 'wb') as f:
    f.write(response_img.content)


