import requests

result = requests.get("https://api.vk.com/method/wall.get?v=5.53&owner_id=-45491419")
count = result.json()['response']['count']
print(count)
baneks = []
for i in range(0, count, 100):
    print(i)
    result = requests.get("https://api.vk.com/method/wall.get?v=5.53&count=100&owner_id=-45491419&offset="+str(i))
    for anek in result.json()['response']['items']:
        if anek['text'] != '':
            baneks.append(anek['text'])
print(len(baneks))

file = open('AnekdotsClassB.txt', 'w')

for i in range(len(baneks)):

    file.write(baneks[i])

file.close()
