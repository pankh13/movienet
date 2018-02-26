# all the imports
import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
import psycopg2


if 'RDS_HOSTNAME' in os.environ:
    POSTGRES_USER = os.environ['RDS_USERNAME']

    POSTGRES_PW = os.environ['RDS_PASSWORD']

    POSTGRES_URL ="aa17r6yquq9zgm3.cidcmcwt0iep.us-west-2.rds.amazonaws.com:5432"

    POSTGRES_DB = os.environ['RDS_DB_NAME']


application = Flask(__name__) # create the application instance :)
application.config.from_object(__name__) # load config from this file , flaskr.py

# Load default config and override config from an environment variable





#DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)

#application.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

def out_similar(movieid):
    '''get similar movie and related infos of the searched object; return none for exception'''
    try:
        result = data.loc[data['0'] == movieid]
        for i in result.iterrows():
            index, output = i
            output = output.tolist()
            output[14] = output[14][1:-1].replace("'","").split(",")
            with open('movielist','r') as f:
                x = f.read().split('\n')
            output.append(x)
            return  output
    except:
        return 0

@application.route('/', methods=['GET', 'POST'])
def searchMovie():
    '''searchMovie main page function'''
    error = None
    if request.method == 'POST':
        movieid = request.form['search']
        result = out_similar(movieid)
       # print(result)
        if result == None:
            
            return render_template('404.html')
        return render_template('mainpage.html', movieList=result)
    return render_template('mainpage.html', movieList=out_similar("The Dark Knight Rises"))

@application.route('/contact')
def contact():
    '''contact page function'''
    return render_template('contact.html')

@application.route('/resume')
def resume():
    '''resume page function'''
    return render_template('resume.html')

if __name__ == "__main__":
    data = pd.read_csv("result.csv")
  #  from sqlalchemy import create_engine
   # engine = create_engine(DB_URL)
    #data.to_sql(name='result', con = engine, if_exists = 'append', index=False)
    #data2 = pd.read_sql_query('select * from result',con=engine)
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()