nemo = ['charles','nemo','charles']

if 'nemo' in nemo:
    print('encontrado')
else:
    print('no encontrado')
    
nemo.append('wa')
nemo.pop(1)
inde = nemo.count('charles')

for n in nemo:
    print(n)

print(inde)