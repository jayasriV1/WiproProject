class Base:
    def _init_(self):
        self.__age =45  # private access modifier   

    def __m1(self):       # two underscores for private
    
        print("This is a private method.")

class Derived(Base):
      pass

obj = Derived()

#print(obj.__age)     
obj.__m1()