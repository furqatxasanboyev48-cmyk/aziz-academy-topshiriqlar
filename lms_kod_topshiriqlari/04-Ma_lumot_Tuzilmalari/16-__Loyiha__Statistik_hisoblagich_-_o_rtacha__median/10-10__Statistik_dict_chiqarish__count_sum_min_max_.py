sonlar = list(map(int, input().split()))
stats = {'count': len(sonlar),'sum': sum(sonlar), 'min': min(sonlar), 'max': max(sonlar)}
print(stats)