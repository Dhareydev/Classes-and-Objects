class Student:
    #Specifically for Bob as the first instance
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.scores = float(score)
        print("My name is", self.name, "\n" "I am", self.age, "\n" "I am undergoing", self.tracks, "\n" "My score is", self.scores)
        print()
        
        print("STUDENT 2 DETAILS ARE: ")
        
    #should accept any new details and change the variables but add to the track
    def change_name(self, change_name):
        self.change_name = str(change_name)
        print("My name is", change_name)
        
    def change_age(self, change_age):
        self.change_age = int(change_age)
        print("My age is", change_age)
    
    def add_tracks(self, add_tracks):
        self.add_tracks = list(add_tracks)
        print("I am also undergoing", add_tracks)
        
    def get_score(self, get_score):
        self.get_score = float(get_score)
        print("My score is", get_score)
        
        
Bob = Student(name = "Bob", age = "26", tracks = ["FE", "BE"], score = 20.90)

      
        
#Expected methods
print(Bob.change_name("Peter"))
print(Bob.change_age(34))
print(Bob.add_tracks("UI/UX"))
Bob.get_score(30)
