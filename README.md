# Flask_Apps

#Without Docker
- Open Terminal 
- source <location of app.py>   
- export FLASK_APP=app.py
- flask run

#With Docker
- Open Terminal
- git build -t flask_app .
- git run -p 5000:5000

Befor you run ensure yo have mongoDB installed
