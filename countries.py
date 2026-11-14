class India():
    
    def capital(self):
        print("Capital of India is New Delhi.")
    def language(self):
        print("Hindi is the most widely spoken language in India.")
    def continent(self):
        print("India is located in Asia.")

class USA():
    def capital(self):
        print("Washington D.C. is the capital of the USA.")
    def language(self):
        print("English is the most widely spoken language in the USA.")
    def continent(self):
        print("USA is located in North America.")

class Russia():
    def capital(self):
        print("Moscow is the capital of Russia.")
    def language(self):
        print("Russian is the most widely spoken language in Russia.")
    def continent(self):
        print("A part of Russia is located in Europe and the rest in Asia.")

Rus = Russia()
Ind = India()
Us = USA()

for country in (Rus,Ind,Us):
    print("================")

    country.language()
    country.capital()
    country.continent()
    print("================")
