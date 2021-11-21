from .extensions import db
#  mối quan hệ nhiều nhiều
# bảng nhật kí thực phẩm
log_food = db.Table('log_food',
         db.Column('log_id', db.Integer, db.ForeignKey('log.id'), primary_key=True),
         db.Column('food_id', db.ForeignKey('food.id'), primary_key=True)

)
#  thực phẩm
class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    proteins = db.Column(db.Integer, nullable=False)
    carbs = db.Column(db.Integer, nullable=False)
    fats = db.Column(db.Integer, nullable=False)

    # hàm tính lượng calo ăn trong ngày
    @property
    def calo(self):
        return self.proteins * 4 + self.carbs * 4 + self.fats * 9

#  nhật ký
class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False)
    foods = db.relationship('Food', secondary=log_food, lazy='dynamic')
