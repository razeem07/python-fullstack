# Movie
# title,rating,run_time,director,genre

# ARM
# KGF

class Movie:

    id:int

    title:str

    rating:int

    run_time:int

    director:str

    genre:str

    def set_movie(self,id,title,rating,director,run_time,genre):

        self.title=title

        self.id=id

        self.rating=rating

        self.director=director

        self.run_time=run_time

        self.genre=genre

    def display(self):

        print(self.id,self.title,self.genre)

filim_instance1=Movie()

filim_instance1.set_movie(100,"arm",4.5,"jithin lal","2:30","action")

filim_instance1.display()






