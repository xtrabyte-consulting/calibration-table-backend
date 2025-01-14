from . import db

class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    equipment_name  = db.Column(db.String(100), index=True, nullable=False)
    last_calibrated = db.Column(db.Date, nullable=False)
    next_due = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '<Equipment {}>'.format(self.equipment_name)