from flask import Flask,url_for,redirect,request
from flask import render_template

import requests

app = Flask(__name__) 

app.config["DEBUG"] = True

@app.route("/")
def render_search():
    return render_template("landing-page.html")

@app.route("/search", methods=['POST'])
def form_submit():
    
    user_query= request.form['search_query'] #matches name attribute of query string input (HTML)
    redirect_url=url_for(".render_search_page",query_string=user_query) #match search_imdb function name
    return redirect(redirect_url)


@app.route("/search/<query_string>", methods=['GET'])
def render_search_page(query_string):
    url = "https://imdb8.p.rapidapi.com/title/auto-complete"

    querystring = {"q":query_string}

    headers = {
        'x-rapidapi-key': "754bf32cb9msh1da68a05c8eff47p14144bjsnd886ba44cc4f",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }
    
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)

        data=response.json()
        return render_template("search-result.html",data=data)

    except:
        return render_template("error404.html")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

