import requests


url = 'http://127.0.0.1:5000/'  # Replace with the URL of your server-side script
filename = 'C:\Users\zaina\Desktop\DESIGN website\loginandsignup\Uploads'  # Replace with the path to your JPEG file

files = {'image': open(filename, 'rb')}

response = requests.post(url, files=files)




