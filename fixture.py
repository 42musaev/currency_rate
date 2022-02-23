from app import db
from app.models import Currency

currency = Currency(name="USD", code="R01235")
db.session.add(currency)
db.session.commit()
