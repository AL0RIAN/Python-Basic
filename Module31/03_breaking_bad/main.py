import requests
import json

episodes = json.loads(requests.get("https://www.breakingbadapi.com/api/death").text)
death_maximum = max(episodes, key=lambda episode: episode["number_of_deaths"])
death_maximum_episode = json.loads(
    requests.get(f"https://www.breakingbadapi.com/api/episodes/{death_maximum['episode']}").text)[0]

print("ID эпизода:", death_maximum_episode["episode_id"])
print("Номер сезона:", death_maximum['season'])
print("Номер эпизода:", death_maximum["episode"])
print("Общее количество смертей:", death_maximum["number_of_deaths"])
print("Список погибших:", death_maximum["death"])
