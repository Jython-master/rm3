a = [0, 0]
try:
    a[0] = raw_input("Type the name of the file ")
except:
    a[0] = input("Type the name of the file ")
a[1] = open(a[0]+".html", "w")
a[1].write('<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<meta charset="utf-8"/>\n\t\t<title>'+str(a[0])+'</title>\n\t</head>\n\t<body>\n\t</body>\n</html>')
a[1].close()
print ("Done")
try:
    raw_input("Press any key to close the application")
except:
    input("Press any key to close the application")
a = [0, 0]
try:
    a[0] = raw_input("Type the name of the file ")
except:
    a[0] = input("Type the name of the file ")
a[1] = open(a[0]+".html", "w")
a[1].write('<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<meta charset="utf-8"/>\n\t\t<title>'+str(a[0])+'</title>\n\t</head>\n\t<body>\n\t</body>\n</html>')
a[1].close()
print ("Done")
try:
    raw_input("Press any key to close the application")
except:
    input("Press any key to close the application")
