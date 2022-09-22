from models import Pet, db
from app import app

db.drop_all()
db.create_all()

Pet.query.delete()

fred = Pet(name='Fred', species='cat', age='1 year')
kirby = Pet(name='Kirby', species='dog', age='9 months')
bean = Pet(name='String Bean', species='dog', age='2 years', breed='Pitbull/Husky')

db.session.add(fred)
db.session.add(kirby)
db.session.add(bean)

db.session.commit()