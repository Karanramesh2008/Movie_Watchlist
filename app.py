from watchlist import Watchlist as wa
from movie import Movie
def main():
    print("Welcome to Movie Watchlish & Tracker")
    w=wa()
    while True:
        
        print("============================================")
        print("1.Add Movies\n2.View Movies\n3.Delete Movies\n4.Mark as Watched\n5.Search By Gerne\n6.Export To Json\n7.Quit")
        print("============================================")
        try:
            c=int(input("Enter your choice: "))
            if c==1:
                title=input("Enter the Movie Title: ")  
                gerne=input("Enter the Movie gerne: ")
                rate=float(input("Enter the movie rating: "))
                m=Movie(title,gerne,rate)
                w.add_movie(m)
            elif c==2:
                w.view_movies()
            elif c==3:
                w.delete()
            elif c==4:
                w.update_m()
            elif c==5:
                w.se_b_gen()
            elif c==6:
                w.export()
            elif c==7:
                print("Thank you for using our app")
                w.conn.close()
                break
            else:
                print("Invalid Choice.")
        except ValueError:
            print("Invalid input choice.")

if __name__=='__main__':
    main()
