from db import *
from models import *
from Flask import redirect, url_for


class StoreFunctions:
  def createStore(username,name,longitude,latitude,address):
    user = db.session.execute(db.select(User).where(User.username == username)).scalar()
    new_store = Store(
      name = name,
      longitude = longitude,
      latitude = latitude,
      address = address,
      admin = user
    )
    db.session.add(new_store)
    db.session.commit()
    return redirect(url_for("stores",username=user.username))
