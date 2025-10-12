#self arguments
class Art:
    traditional = 2000

    def describe(self):
        return f"{self.traditional} for tranditional art"
    

artwork = Art()
print(artwork.describe())
#print(Art.describe()) throws an error
print(Art.describe(artwork)) # gives the output

new_artwork = Art()
new_artwork.price = 5000
print(Art.describe(new_artwork))

#easiest way is to creat an object and then call the methods