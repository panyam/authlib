
from google.appengine.ext import ndb
from google.appengine.ext.ndb import msgprop
from servicelib import models as slmodels


class User(slmodels.ModelBase):
    AUTHY_STATUSES = (
        'unverified',
        'onetouch',
        'sms',
        'token',
        'approved',
        'denied'
    )

    fullname = ndb.StringProperty()
    password_hash = ndb.StringProperty(default="")
    phone = ndb.StringProperty(default="")
    email = ndb.StringProperty(default="")
    is_active = ndb.BooleanProperty(default=True)
    last_update_at = ndb.DateTimeProperty(auto_now_add=True)
    authy_id = ndb.IntegerProperty()
    authy_status = msgprop.EnumProperty(AUTHY_STATUSES, required=True, indexed=True)

    def to_json(self):
        return {
            'id': self.getid(),
            'fullname': self.fullname,
            'email': self.email,
            'is_active': self.is_active,
            'phone': self.phone,
            'last_updated': self.last_update_at.ctime(),
            'authy_status': self.authy_status
        }
