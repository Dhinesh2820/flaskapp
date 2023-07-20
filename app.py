from flask import Flask,request,redirect,url_for,render_template
from user_model import user_model
from flask_cors import CORS, cross_origin
from flask_jwt_extended import jwt_required
obj = user_model()
app = Flask(__name__)


from flask_jwt_extended import JWTManager
from datetime import timedelta
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=2)

jwt = JWTManager(app)


@app.route("/user/getall")
@jwt_required()
def user_getall_controller():
    return obj.user_getall_model()

@app.route("/login", methods=["POST"])
@cross_origin()
def user_login():
    # return 'rgtest'
    try:
        obj = user_model()
        return obj.user_login_model(request.data)
    except Exception as e:
        return {"message":str(e)}
    finally:
        del obj


@app.route("/user/getbyid/<id>")
@jwt_required()
def user_getone_controller(id):
    return obj.user_getbyid_model(id)

@app.route("/user/addone",methods=['POST'])
def user_addone_controller():
     return obj.user_add(request.data)


@app.route("/user/update",methods=['POST'])
def user_update_controller():
     return obj.user_update(request.data)


@app.route("/user/delete/<id>",methods=['Delete'])
def user_delete_controller(id):
     return obj.user_delete(id)

@app.route('/hello')
def welcome():
     return {"message":'hello world'}

@app.route('/guest/<guest>')
def guest_controller(guest):
     return {"message":"hello %s as Guest" % guest}

@app.route('/admin')
def hello_admin():
     return "hello admin"

@app.route('/user/<name>')
def hello_user(name):
     if name =="admin":
          return redirect(url_for("hello_admin"))
     else:
          return redirect(url_for("guest_controller",guest =name))
     

@app.route('/department/get')
@jwt_required()
def department_getcontroller():
     return obj.user_get()
     

@app.route('/udcombine/get')
@jwt_required()
def user_departmentcontroller():
     return obj.user_right_combine()

@app.route('/udcombineleft/get')
def user_departmentleftcontroller():
     return obj.user_left_combine()

@app.route("/udcombineinner/get")
def user_departmentinnercontroller():
     return obj.user_inner_combine()

@app.route("/appliedleave/get")
def user_subcombinecontroller():
     return obj.appliedleave()

@app.route("/holiday/get")
def user_holiday_get():  
     return obj.holidaycombine()

@app.route("/birthday/get")
def user_birthday_get():
     return obj.birthday()

@app.route("/user/status")
def user_status():
     return obj.status()

@app.route("/users/age")
def user_age():
     return obj.age()

@app.route("/users/last")
def user_last():
     return obj.last()
     




# @app.route("/index")
# def index():
#    return render_template('index.html')


# @app.route('/')
# @app.route('/home')
# def homepage():
#     return render_template('register.html')


if __name__ == "__main__":
      app.run(debug=True)