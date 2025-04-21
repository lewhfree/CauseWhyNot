import sys

numOfArgs = len(sys.argv)

if numOfArgs < 4:
    print("At least 3 arguments needed: see readme")
    sys.exit()

executableInput = sys.argv[1]
stubInput = sys.argv[2]
output = sys.argv[3]

with open(output, "wb") as out:
    with open(executableInput, "rb") as exe:
        with open(stubInput, "rb") as stub:
            add = 0
            if len(sys.argv) == 5:
                add = int(sys.argv[4])
            out.write(stub.read())
            
            if add != 0:
                print("need bytes", add-len(stub.read()))
                for i in range(add - len(stub.read())):
                    out.write(b'\x90')
            out.write(exe.read())
            print("done")