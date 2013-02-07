names = ['Justin', 'caterpillar', 'openhome']
for i in range(len(names)):
    print '{0}, {1}'.format(i, names[i])
    
for i, name in zip(range(len(names)), names):
    print '{0}, {1}'.format(i, name)
    
for i, name in enumerate(names):
    print '{0}, {1}'.format(i, name)