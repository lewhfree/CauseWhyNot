import sys
import re

pattern = r'^\d+\.\d{2}$'

numArgs = len(sys.argv)

if numArgs < 3:
    print("Expected 2 filename arguments - one input, one output")
    sys.exit()

if numArgs >= 4:
    #Dump rest of the bin after the stub
    print("Dumping binary after stub to", sys.argv[3])

fileName = sys.argv[1]

print("Opening:", fileName)

with open(fileName, "rb") as file:
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
    
    file.seek(0)
    data = file.read()
    repeatableString = "83e00f03f8e9eafec300000000000000"
    offset = data.find(bytes.fromhex(repeatableString))

    if offset == -1:
        print("CauseWay magic bytes not found.")
        sys.exit()
    else:
        print("CauseWay magic bytes at:", offset)
                    #This is here because the length is 32 when its 16 bytes, you could also do bytes.fromhex
    eos = offset + int(len(repeatableString) / 2)
    
    outputFile = sys.argv[2]
    with open(outputFile, "wb") as out:
        print("Opening", outputFile,"to write.")
        dataToEos = data[:eos]
        out.write(dataToEos)
        print("Wrote", len(dataToEos), "bytes to file")
    print("Closed", outputFile)
    
    if numArgs >= 4:
        outputFile = sys.argv[3]
        with open(outputFile, "wb") as out:
            print("Opening", outputFile, "to write.")
            dataFromEos = data[eos:]
            out.write(dataFromEos)
            print("Wrote",len(dataFromEos), "bytes to file")
        print("Closed", outputFile)

print("Closed", sys.argv[1])


