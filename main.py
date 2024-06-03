from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///test.db"
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__= "users"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(50),nullable=True)
    age = db.Column(db.Integer, nullable=True) 

    def __repr__(self) -> str:
        return f'<User: {self.name}>'

class Address(db.Model):
    __tablename__ = "address"
    id = db.Column(db.Integer,primary_key=True)
    area = db.Column(db.String(50),nullable=False)
    city = db.Column(db.String(50),nullable=False)
    state = db.Column(db.String(50),nullable=False)
    pincode = db.Column(db.Integer,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id',ondelete='CASCADE'))

    def __repr__(self) -> str:
        return f'<User: {self.area}>'

@app.route('/')
def index():
    return "Hello World"

@app.route('/add_user',methods=['POST'])
def add_user():
    data = request.json
    if not data:
        return jsonify({"Message":"Please provide Data"})
    name = data['name']
    email = data['email']
    age = data.get('age')
    if not (name or email):
        return jsonify({"Message":"Please fill both the name and Email field"})
    user = User(name=name,email=email,age=age)
    db.session.add(user)
    db.session.commit()
    return jsonify({"Message":"User Added Successfully..!!!"})


@app.route('/add_address',methods=['POST'])
def add_address():
    data = request.json
    if not data:
        return jsonify({"Message":"Please provide Data"})
    area = data['area']
    city = data['city']
    state = data['state']
    pincode = data['pincode']
    user_id = data['user_id']
    if not (area or city or state or pincode):
        return jsonify({"Message":"please provide all the required details"})
    addrss = Address(area=area,city=city,state=state,pincode=pincode,user_id=user_id)
    db.session.add(addrss)
    db.session.commit()
    return jsonify({"Message":"Address added successfully."})

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)