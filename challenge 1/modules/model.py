from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

#defining the database schema in the Bids class
class Bids(db.Model):
    bidid= db.Column(db.Integer, primary_key=True)
    petid = db.Column(db.Integer,nullable=False)
    userid = db.Column(db.Integer, nullable=False)
    value = db.Column(db.Integer)
 
#query all database entries and prepare them to be outputed into json
def get_bids():
    bids = Bids.query.all()
    output = []
    for bid in bids:
        biddingdata = {'bidid':bid.bidid,'petid': bid.petid, 'value': bid.value, 'userid':bid.userid}
        output.append(biddingdata)
    return {"bids": output}

#fetch input bid from serialized json and push to object model that will be placed into the database
def add_bid(petid,value,userid):
    bid = Bids(petid=petid,value=value,userid=userid)
    db.session.add(bid)
    db.session.commit()