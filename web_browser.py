import webbrowser, sys, requests, bs4

string = "https://automatetheboringstuff.com"
badString = "https://automatetheboringstuff.com/files/rj.text"

# webbrowser.open(string)
#
# if len(sys.argv) > 1:
#     address = ' '.join(sys.argv[1:])
# else:
#     address = py

res = requests.get(string)
print("Status code of request: {}".format(res.status_code))

# res = requests.get(badString)
# print(res.status_code)

res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
elems = soup.select('body > div.main > div:nth-child(1) > div:nth-child(4) > center > a:nth-child(3)')

print(elems[0].text.strip())