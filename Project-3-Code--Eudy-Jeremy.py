from Crypto.Hash import SHA256

#Create SHA256 object
h = SHA256.new()
#Open file and hash
f = open('Anarchism.txt', 'r')
data = f.read()
h.update(data.encode('utf8'))
print(h.hexdigest())
