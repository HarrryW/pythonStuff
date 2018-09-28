class personalInfo():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def callFeatures(self):
        print 'You are %s' %self.name + ' you are %s years old' %self.age

r1 = personalInfo("Tony", 23, 23)
r1.callFeatures()

#control shift K to delete entire lines
