latitudes = [1, 2, 3, 4, 5]
longitudes = [2, 3, 90, 100, 900]

output = []
for i in range(0, len(latitudes)):
    output.append([latitudes[i], longitudes[i]])

print(output)