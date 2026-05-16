import sqlite3
import json

class Watchlist:
    def __init__(self):
        self.conn=sqlite3.connect("movies.db")
        self.cursor=self.conn.cursor()
        self._create_table()
    
    def _create_table(self):
        self.cursor.execute(" CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY  AUTOINCREMENT,title TEXT NOT NULL,genre TEXT NOT NULL,rating REAL, watched INTEGER DEFAULT 0)")
        self.conn.commit()
    
    def add_movie(self,movie):
        self.cursor.execute("INSERT INTO movies (title,genre,rating) VALUES (?,?,?) ",(movie.title,movie.genre,movie.rating))
        self.conn.commit()
        print(f"{movie.title} is successfully added")

    def view_movies(self):
        self.cursor.execute("SELECT * FROM movies")
        movies=self.cursor.fetchall()
        if not movies:
            print("No movies added")
            return

        print("\n -----Your Watchlist-------\n")
        for movie in movies:
            ws="Watched" if movie[4]==1 else "Not Watched"
            print(f"{movie[0]}. {movie[1]} | {movie[2]} | Rating: {movie[3]} | {ws}")
            print("\t---------------\n")

    def update_m(self):
        self.view_movies()
        mo=int(input("Enter the movie id to update: "))
        self.cursor.execute("UPDATE movies SET watched=1 WHERE id=?",(mo,))
        self.conn.commit()
        print("Movie watchlist updated.!")

    def delete(self):
        self.view_movies()
        mo=int(input("Enter the movie id to delete: "))
        self.cursor.execute("DELETE FROM movies WHERE id=?",(mo,))
        self.conn.commit()
        print("Movie successfully deleted!\n")
        return

    def se_b_gen(self):
        gen=input("Enter the genre you like to search: ")
        self.cursor.execute("SELECT * FROM movies WHERE genre LIKE ?",(f"%{gen}%",))
        movies=self.cursor.fetchall()
        if not movies:
            print("No Movies available")
            return
        
        print(f"\n -------Results for {gen}------- \n")
        for movie in movies:
            ws="Watched" if movie[4]==1 else "Not Watched"
            print(f"{movie[0]}. {movie[1]} | {movie[2]} | Rating: {movie[3]} | {ws}")
            print("\t---------------\n")

    def export(self):
        self.cursor.execute("SELECT * FROM movies")
        movies=self.cursor.fetchall()
        mo_l=[]
        for m in movies:
            status='Yes' if m[4]==1 else "Not Watched"
            mo_l.append({'id': m[0],'Title': m[1],'Genre': m[2],'Rating': m[3],'Watched': status})
        
        with open("movies.json","w") as f:
            json.dump(mo_l,f,indent=4)
        print(f"\nExported {len(mo_l)} movies to movies.json!\n")

        