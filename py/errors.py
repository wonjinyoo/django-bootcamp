try:
    f = open("sample.txt", "r")
    f.write("Test writing")
except:
    print("ERROR: COULD NOT FIND or READ")
finally:
    print("I work no matter what")
