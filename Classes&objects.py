#def keyword
#Working on class
class Student:
    def __init__(self,name,age,tracks,score):
        self.name=name
        self.age=age
        self.tracks=tracks
        self.score=score
    
    def __str__(self):
        return f"{self.name} , {self.age} ,  {self.tracks} , {self.score}"
    
    def change_name(self, newName):
        self.name= newName

    def Change_age(self, newAge):
        self.age= newAge
    
    def Add_track(self, newTrack):
        self.tracks.append(newTrack)

    def get_score(self):
        return self.score
        
    

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
Bob.change_name("Peter")
Bob.Change_age(34)
Bob.Add_track("UI/UX")
Bob.get_score()
print(Bob)