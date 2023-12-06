Seeds = []
Map = []
SeedToSoil = []
SoilToFertilizer = []
FertiliserToWater = []
WaterToLight = []
LightToTemperature = []
TemperatureToHumidity = []
HumidityToLocation = []
Manual = []

with open("Hrdy\Day5\Test.txt","r") as f:
    Seeds = [int(x) for x in f.readline().split(": ")[1].strip().split(" ")]
    for line in f:
        if line.strip() == "":
            if len(Map) > 0 :
                Manual.append(Map)
                Map = []
        else: Map.append(line.strip())
    Manual.append(Map)

for i in range(1,len(Manual[0])):
    SeedToSoil.append([int(x) for x in Manual[0][i].split(" ")])
for i in range(1,len(Manual[1])-1):
    SoilToFertilizer.append([int(x) for x in Manual[1][i].split(" ")])
for i in range(1,len(Manual[2])):
    FertiliserToWater.append([int(x) for x in Manual[2][i].split(" ")])
for i in range(1,len(Manual[3])):
    WaterToLight.append([int(x) for x in Manual[3][i].split(" ")])
for i in range(1,len(Manual[4])):
    LightToTemperature.append([int(x) for x in Manual[4][i].split(" ")])
for i in range(1,len(Manual[5])):
    TemperatureToHumidity.append([int(x) for x in Manual[5][i].split(" ")])
for i in range(1,len(Manual[6])):
    HumidityToLocation.append([int(x) for x in Manual[6][i].split(" ")])
print(Seeds)
print(SeedToSoil,SoilToFertilizer,FertiliserToWater,WaterToLight,LightToTemperature,TemperatureToHumidity,HumidityToLocation)
