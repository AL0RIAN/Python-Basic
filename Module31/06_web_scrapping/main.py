import requests
import re

base = requests.get("http://www.columbia.edu/~fdc/sample.html").text
pattern = r'<h3\s{0,}\d{0,}\D{0,}>\s{0,}\d{0,}\D{0,}</h3>'

headers = re.findall(pattern, base)
temp = '<h3 id="contents">CONTENTS</h3>'

result = [head[head.find(">") + 1:head.rfind("<")] for head in headers]
print(f"Результат:\n\t{result}")
