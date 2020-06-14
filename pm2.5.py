import urllib.request


link = "https://www.aismagellan.io/api/things/pull/3654fa50-5c96-11ea-b7bc-61455edf93af"
f = urllib.request.urlopen(link)
myfile = f.read()
print(myfile)
