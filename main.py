import sys
import re

pattern = r'^\d+\.\d{2}$'

numArgs = len(sys.argv)

if numArgs == 1:
    print("Expected a filename argument")
    sys.exit()

fileName = sys.argv[1]

print("Opening:", fileName)

with open(fileName, "rb") as file:
    #file.seek(1241)
    #byte = file.read(4)
    #byte = byte.decode('ascii')
    #print(str(byte))
    

    for i in range(5):
        knownVOffsets = [1241, 1273, 1257, 1225, 1289]
        file.seek(knownVOffsets[i])
        byte = file.read(4)
        byte = byte.decode('ascii', errors='ignore')
        if re.match(pattern, str(byte)):
            print("CauseWay version", str(byte))
            break
        else:
            if i == 4:
                print("CauseWay not found or unsupported version")
                sys.exit()
    
    #Valid CauseWay executable, I think it is just the first 0xb680 but 

    repeatableString = "d138d1e8d1e88cc303c38ec05b582bf8"
    offset = file.read().find(bytes.fromhex(repeatableString))

    if offset == -1:
        print("string not found")
        sys.exit()
    else:
        print("OFFSET FOUND AT", offset)
