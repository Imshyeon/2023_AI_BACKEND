import xml.etree.ElementTree as ET

#1. 파일을 로드하자.
tree = ET.parse('weather.xml')
root = tree.getroot()   #<weather>
print(root)

#2. 하위 요소 추출
for city in root.findall('city'):
    name=city.get('name')
    temperature= city.findtext('temperature')
    weather_condition=city.findtext('weather_condition')
    humidity=city.findtext('humidity')
    wind_speed=city.findtext('wind_speed')
    print(f"{name}'s temperature : {temperature},")
    print(f"{name}'s weather_condition : {weather_condition},")
    print(f"{name}'s humidity : {humidity},")
    print(f"{name}'s wind_speed : {wind_speed},")
    print()