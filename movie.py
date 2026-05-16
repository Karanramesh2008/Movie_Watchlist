
class Movie:
    def __init__(self,title,genre,rating):
        self.title=title
        self.genre=genre
        self.rating=rating
        self.watched=0

    def show(self):
        status="Watched" if self.watched==1 else "Not Watched"
        print(f"{self.title}| {self.genre}| {self.rating}| {status} ")
    
    def to_dict(self):
        return {
            "Title":self.title,
            "Genre":self.genre,
            "Rating":self.rating,
            "Watched":"Yes" if self.watched==1 else "No"

        }
    