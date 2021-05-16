import http.cookiejar
import urllib.request
import requests
import bs4

# Store the cookies and create an opener that will hold them
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

# Add our headers
opener.addheaders = [('User-agent', 'dfdf')]

# Install our opener (note that this changes the global opener to the one
# we just made, but you can also just call opener.open() if you want)
urllib.request.install_opener(opener)

# The action/ target from the form
authentication_url = 'https://m.facebook.com/login.php'

# Input parameters we are going to send
payload = {
  'email': 'tharanitharanmr123@gmail.com',
  'pass': 'tharani2000'
  }

# Use urllib to encode the payload
data = urllib.parse.urlencode(payload).encode("utf-8")

# Build our Request object (supplying 'data' makes it a POST)
req = urllib.request.Request(authentication_url, data)

# Make the request and read the response
resp = urllib.request.urlopen(req)
contents = resp.read()

url = "https://www.facebook.com/tharani.tharan.3363/friends"
data = requests.get(url, cookies=cj)
soup = bs4.BeautifulSoup(data.text, 'html.parser')

z = 0
for i in soup.find_all('a'):
    if z>16:
        if i.text.lower()=="see more friends":
            break
        elif i.text != "Add Friend":
            print(i.text)
    z = z+1
