
from google.appengine.ext import ndb
from servicelib import models as slmodels

class User(slmodels.ModelBase):
    fullname = ndb.StringProperty()
    phone = ndb.StringProperty(default="")
    email = ndb.StringProperty(default="")
    is_active = ndb.BooleanProperty(default=True)
    last_update_at = ndb.DateTimeProperty(auto_now_add=True)

    def to_json(self):
        return {
            'id': self.getid(),
            'fullname': self.fullname,
            'email': self.email,
            'is_active': self.is_active,
            'phone': self.phone,
            'last_updated': self.last_update_at.ctime()
        }
