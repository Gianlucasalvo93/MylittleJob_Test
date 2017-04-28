
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, _app_ctx_stack,make_response

app = Flask(__name__)
import requests,json,urllib2



global types #global variable to store the item type of the search


@app.route('/get_api', methods=['GET', 'POST'])
def get_api():

    global types
    name = str(request.form['search'])
    root="https://api.spotify.com/v1/search?q="

    url = build_link(root,name,types)

    raw_content = urllib2.urlopen(url).read()#raw API response

    json_content=json.loads(raw_content)#json conversion

    artist = json_content[types+"s"]["items"] #access to the relevant items..
    
    return render_template('index.html', content=artist, counter=len(artist))


def build_link(root,name,types):

    name=name.replace(" ","%20") #correct spaces for the request..

    return "https://api.spotify.com/v1/search?q="+name+"&type="+types


#these four methods are useful to set the item type, in order to make the right API call
@app.route('/set_type_artist')
def set_type_artist():
    global types
    types="artist"
    return render_template('index_w_b.html', types=types)


@app.route('/set_type_album')
def set_type_album():
    global types
    types="album"
    return render_template('index_w_b.html', types=types)


@app.route('/set_type_playlist')
def set_type_playlist():
    global types
    types="playlist"
    return render_template('index_w_b.html', types=types)


@app.route('/set_type_track')
def set_type_track():
    global types
    types="track"
    return render_template('index_w_b.html',types=types)
    

@app.route("/")
def main():
    return render_template('index.html',counter=0)


if __name__ == "__main__":
    app.run()
