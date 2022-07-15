import re

auto = "А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666"

pattern_private = r"[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}"
pattern_taxi = r"[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}"

result1 = re.findall(pattern_private, auto)
print("Список номеров частных автомобилей:", result1)
result2 = re.findall(pattern_taxi, auto)
print("Список номеров такси:", result2)
