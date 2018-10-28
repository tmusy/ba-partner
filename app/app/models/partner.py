from ..extensions import db


class Partner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    stars = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(16), nullable=False)
    hp = db.Column(db.Integer, nullable=False)
    atk = db.Column(db.Integer, nullable=False)
    df = db.Column(db.Integer, nullable=False)
    spd = db.Column(db.Integer, nullable=False)
    cr = db.Column(db.Integer, nullable=False)
    crd = db.Column(db.Integer, nullable=False)
    res = db.Column(db.Integer, nullable=False)
    hit = db.Column(db.Integer, nullable=False)
    skill_1 = db.Column(db.String(1080))
    skill_2 = db.Column(db.String(1080))
    skill_3 = db.Column(db.String(1080))
    leader_skill = db.Column(db.String(1080))
    type = db.Column(db.String(8))
    tier = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Partner {0} {1}>'.format(self.color, self.name)
