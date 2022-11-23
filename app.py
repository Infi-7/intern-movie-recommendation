import pandas as pd
import os
import pickle
from flask import *

os.chdir('C:\\Users\\infip\\OneDrive\\Documents\\PY Projects\\not ready\\')
with open('model_similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)

with open('dummy.pkl', 'rb') as f:
    movies_data = pickle.load(f)

headings = ("Title","Populararity")
list1 = []
list2 = []
rows = []

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/recommend',methods=['GET','POST'])
def recommend():
    movie_user_likes = request.form.get("movie")
    results_title = pd.DataFrame(similarity, index=movies_data.title, columns=movies_data.title)

    data = results_title[movie_user_likes].sort_values(ascending=False)[:20]
    titles = data.index
    list1 = (titles.tolist())

    popularity = data.values
    list2 = popularity.astype(str)
    list2 = list(map(str, list2))

    rows.extend([list(a) for a in zip(list1, list2)])

    return render_template('recommend.html',headings=headings,rows = rows)

 
if __name__=='__main__':
    app.run(port = 5000, debug = True)