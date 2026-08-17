# 1-qator: soat (int)
# 2-qator: daqiqa (int)
# Jami soniya: soat*3600 + daqiqa*60
# "Seconds: <natija>" ko'rinishida chiqaring.
soat = int(input())
daqiqa = int(input())
jami_soniya = soat * 3600 + daqiqa * 60
print(f"Seconds: {jami_soniya}")