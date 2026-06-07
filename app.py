from flask import Flask,request, jsonify,render_template
import json
import os
import requests

app=Flask(__name__)
file='watchlist.json'
api='f968a55a'

def load_watchlist():
    if os.path.exists(file):
        with open(file,'r') as f:
            return json.load(f)
    return []

def save_watchlist(data):
    with open(file,'w') as f:
        json.dump(data,f,indent=4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    title=request.args.get('title')
    url=f'https://www.omdbapi.com/?t={title}&apikey={api}'
    res=requests.get(url)
    data=res.json()
    if data.get('Response')=='False':
        return jsonify({'error': 'Movie not found'})
    return jsonify(data)

@app.route('/add',methods=['POST'])
def add():
    movie=request.json
    watchlist=load_watchlist()
    for m in watchlist:
        if movie['imdbID']==m['imdbID']:
            return jsonify({'message':movie['Title']+' added to watchlist!'})
    movie['watched']=False
    watchlist.append(movie)
    save_watchlist(watchlist)
    return jsonify({'message':movie['Title']+' added to watchlist!'})

@app.route('/watchlist')
def get_watchlist():
    return jsonify(load_watchlist())

@app.route("/watched",methods=['POST'])
def mark_watched():
    imdb_id=request.json.get('imdbID')
    watchlist=load_watchlist()
    for movie in watchlist:
        if movie['imdbID']==imdb_id:
            movie['watched']=True
    save_watchlist(watchlist)
    return jsonify({"message":'Marked as watched!'})

@app.route('/unwatch',methods=['POST'])
def unwatch():
    imdb_id=request.json.get('imdbID')
    watchlist=load_watchlist()
    for movie in watchlist:
        if movie['imdbID']==imdb_id:
            movie['watched']=False
    save_watchlist(watchlist)
    return jsonify({'message':'Marked as unwatched!'})
if __name__=='__main__':
    app.run(debug=True)