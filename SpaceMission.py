WIDTH = 800
HEIGHT = 600
roommap = []
temprow = []
for i in range(10):
    temprow.append(1)
roommap.append(temprow)
for i in range(6):
    temprow = []
    temprow.append(1)
    for j in range(8):
        temprow.append(0)
    temprow.append(1)
    roommap.append(temprow)
temprow = []
for i in range(10):
    temprow.append(1)
roommap.append(temprow)
print(roommap)