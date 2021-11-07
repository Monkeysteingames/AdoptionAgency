from app import db
from models import Pet

db.drop_all()
db.create_all()

buster = Pet(name='Buster', species="cat",
             photo_url="https://pbs.twimg.com/media/EpUFKvIXEAoMemB?format=jpg&name=large", age=1, notes="He's crazy!", available=False)
corn = Pet(name='Corn', species="chipmunk", photo_url="https://npr.brightspotcdn.com/dims4/default/0d5e58e/2147483647/strip/true/crop/1920x1280+0+0/resize/880x587!/quality/90/?url=http%3A%2F%2Fnpr-brightspot.s3.amazonaws.com%2Flegacy%2Fsites%2Fwxpr%2Ffiles%2F202007%2Fchipmunk-5401165_1920.jpg", age=1, notes="loves peanut butter!")

db.session.add_all([buster, corn])
db.session.commit()
