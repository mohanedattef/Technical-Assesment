# Bidding Api:
This is the requested bidding api with two endpoints, one to bid a new bid and one to list all bids.  

## requirements:

```
pip3 install requirements.txt
```

## Running the App:
Make sure you first install Flask and the rest of the requiremnts   

**bids.py:** is the main Flask application server so to make sure everything is in order
```
set FLASK_APP=hello.py
```
then you can 
```
Flask run
```

To test the api end points you can run 
```
nosetests --verbose
```
when the server is running or use Postman on the local server http://127.0.0.1:5000


