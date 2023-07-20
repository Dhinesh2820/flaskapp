from flask import Flask,request,make_response
import mysql.connector
import json
# from werkzeug.security import generate_password_hash, check_password
from flask_jwt_extended import create_access_token,get_jwt_identity


# from datetime import datetime
# class user_model():
#     def database(self):
#         self.conn=mysql.connector.connect(host="127.0.0.1",user="root",passwd="",database="sample",port=3307)

#         self.conn.autocommit=True
#         return self.conn.cursor(dictionary=True)
    
#     def user_getall_model(self):
#         cur=self.database()

#         cur.execute("SELECT *FROM users")
#         result=cur.fetchall()
#         if len(result)>0:
#             return result
#         else:
#             return {"message":"not data found"}
        
    

#     def user_getbyid_model(self,id):
#         cur =self.database()

#         sql_select_query="SELECT *FROM users where id =%s"
#         cur.execute(sql_select_query,(id,))
#         result =cur.fetchall()
#         if len(result)>0:
#             return result
#         else:
#             return {"message":"not data found"}
        
    
# class user_model():
#     def database(self):
#         self.conn=mysql.connector.connect(host="127.0.0.1",username="root",database="sample",port=3307,password="")

#         self.conn.autocommit=True
#         return self.conn.cursor(dictionary=True)
    

#     def user_getall_model(self):
#         cur=self.database()
#         cur.execute("SELECT *FROM USERS")
#         result =cur.fetchall()

#         if len(result)>0:
#             return result
        

#     def user_getbyid_model(self,id):
#         cur=self.database()

#         sql_select_query="SELECT * FROM USERS where id =%s"
#         cur.execute(sql_select_query,(id,))

#         result=cur.fetchall()
        
#         if len(result)>0:
#             return result
        
#     def user_add(self,data1):
#         cur=self.database()
#         data=json.loads(data1)
#         cur.execute(f"Insert into users(age,name,phone)VALUES('{data['age']}','{data['name']}','{data['phone']}')")
#         return {"message":"added successfully"}

#     def user_update(self,data1):
#         cur=self.database()
#         data=json.loads(data1)
#         sql_select_query ="update users set age =%s ,name =%s, phone = %s where id =%s"
#         input =(data['age'],data['name'],data['phone'],data['id'])

#         cur.execute(sql_select_query,input)
#         return {"message":"updated successfully"}
    
#     def user_delete(self,id):

#         try:
#             cur=self.database()
#             data=json.loads(id)
#             cur.execute(f"DELETE FROM  users where id ={id}")
#             return {"message":"deleted successfully"}
        
#         except Exception as e:
#             return {"message":str(e)}
#         finally :
#             del cur



# class user_model():
#     def database(self):
#         self.conn =mysql.connector.connect(host="127.0.0.1",username="root",database="sample",port=3307)

#         self.conn.autocommit=True
#         return self.conn.cursor(dictionary= True)
    
#     def user_getall_model(self):
#         cur=self.database()
#         cur.execute("SELECT * From users")
#         result=cur.fetchall()

#         if len(result)>0:
#             return result
        

#     def user_getbyid_model(self,id):
#         cur=self.database()
#         sql_select_query=("SELECT * FROM USERS WHERE id =%s")
#         cur.execute(sql_select_query,(id,))
#         result=cur.fetchall()

#         if len(result)>0:
#             return result
        

#     def user_add(self,data1):
#         cur=self.database()
#         data =json.loads(data1)
#         sql_select_query="INSERT INTO users(age,phone,name)VALUES(%s,%s,%s)"
#         input=(data['age'],data['phone'],data['name'])
#         cur.execute(sql_select_query,input)
#         return {'message':"added successfully"}
    
#     def user_update(self,data1):
#         cur=self.database()
#         data=json.loads(data1)
#         sql_select_query= "UPDATE users set age =%s,phone =%s,name=%s where id =%s"
#         input=(data['age'],data['phone'],data['name'],data['id'])
#         cur.execute(sql_select_query,input)
#         return {"message":"update successfully"}
        

#     def user_delete(self,id):
#         try:    

#             cur =self.database()
#             data =json.loads(id)
#             cur.execute="DELETE from users where id =%s"
#             if cur.rowcount>0:

#                 return {"message":"delete successfully"}
#             else:
#                 return {"message": "Nothing to delete"}
        
        
#         except Exception as e:
#             return {"message":e}
#         finally:
#             del cur


# class user_model():
#     def database(self):
#         self.conn =mysql.connector.connect(host="127.0.0.1",username="root",database ="sample",port=3307)

#         self.conn.autocommit =True
#         return self.conn.cursor(dictionary=True)
    
#     def user_getall_model(self):
#         cur =self.database()
#         cur.execute("SELECT * FROM users ")
#         result =cur.fetchall()
#         return result
    

#     def user_getbyid_model(self,id):
#         cur =self.database()
#         sql_select_query=("SELECT * FROM users where id = %s")
#         cur.execute(sql_select_query,(id,))
#         result =cur.fetchall()
#         return result

#     def user_add(self,data1):
#         cur=self.database()
#         data=json.loads(data1)
#         sql_select_query="INSERT INTO USERS(age,name,phone)VALUES(%s,%s,%s)"
#         input=(data['age'],data['name'],data['phone'])
#         cur.execute(sql_select_query,input)
#         # result =cur.fetchall()
        # if cur.rowcount>0:
        #     return {"message":"added successfully"}
        # else:
        #     return {"message":"Nothing to update"}

#     def user_update(self,data1):
#         cur=self.database()
#         data=json.loads(data1)
#         sql_select_query="UPDATE USERS SET age =%s ,name=%s, phone =%s where id=%s"
#         input=(data['age'],data['name'],data['phone'],data['id'])
#         cur.execute(sql_select_query,input)
#         if cur.rowcount>0:
#             return {"message":"updated successfully"}
#         else:
#             return {"message":"Nothing to update"}
    

#     def user_delete(self,id):
            
#         try:
#             cur=self.database()
#             data=json.loads(id)
#             cur.execute="DELETE * FROM USERS WHERE  id =%s"

#             if cur.rowcount>0:
#                 return {"message":"delete successfully"}
#             else:
#                 return {"message":"Nothing to update"}
        
#         except Exception as e:
#             return {"message" : e}
#         finally:
#             del cur


# class user_model():
#     def database(self):
#         self.conn =mysql.connector.connect(host="127.0.0.1",database="sample",username="root",port=3307)

#         self.conn.autocommit=True
#         return self.conn.cursor(dictionary=True)
    
#     def user_getall_model(self):
#         cur =self.database()
#         cur.execute("SELECT * FROM users")
#         result=cur.fetchall()
#         return result
    
#     def user_getbyid_model(self,id):
#         cur =self.database()
#         sql_select_query=("SELECT *FROM USERS WHERE id = %s")
#         cur.execute(sql_select_query,(id,))
#         result =cur.fetchall()
#         return result
    
#     def user_add(self,data1):
#         cur=self.database()
#         data=json.loads(data1)
#         sql_select_query="INSERT INTO users (age,name,phone)Values(%s,%s,%s)"
#         input =(data['age'],data['name'],data['phone'])
#         cur.execute(sql_select_query,input)
#         if cur.rowcount>0:
#             return {"message":"added successfully"}
#         else:
#             return {"message":"Nothing to update"}
        


#     def user_update(self,data1):
#         cur=self.database()
#         data =json.loads(data1)
#         sql_select_query="UPDATE USERS SET age =%s,name =%s,phone =%s where id=%s"
#         input=(data['age'],data['name'],data['phone'],data['id'])
#         cur.execute(sql_select_query,input)
#         if cur.rowcount>0:
#             return{"message":"updated successfully"}
#         else:
#             return {"message":"Nothing to update"}
        

#     def user_delete(self,id):
#         cur =self.database()
#         data=json.loads(id)
#         cur.execute = "DELETE * FROM users WHERE id =%s"
#         if cur.rowcount>0:
#             return{"message":"Deleted successfully"}
#         else:
#             return {"message":"Nothing to Delete"}
        

    # def database(self):
    #     self.conn=mysql.connector.connect(host="127.0.0.1",database="sample",username="root",port=3307)
    #     self.conn.autocommit=True
    #     return self.conn.cursor(dictionary=True)


    # def user_getall_model(self):
    #     cur= self.database()
    #     cur.execute("select * from users")
    #     result=cur.fetchall()
    #     return result

    # def user_getbyid_model(self,id):
    #     cur =self.database()
    #     sql_select_query=("select * from users where id=%s") 
    #     cur.execute(sql_select_query,(id,))
    #     result=cur.fetchall()
    #     return result
    
    # def user_add(self,data1):
    #     cur=self.database()
    #     data=json.loads(data1)
    #     sql_select_query="Insert into users(name,age,phone)values(%s,%s,%s)"
    #     input=(data['name'],data['age'],data['phone'])
    #     cur.execute(sql_select_query,input)
    #     if cur.rowcount>0:
    #         return{"message":"added successfully"}
    #     else:
    #         return{"message":"Nothing to update"}

    # def user_update(self,data1):
    #     cur=self.database()
    #     data=json.loads(data1)
    #     sql_select_query="update users set age=%s,name=%s,phone=%s where id=%s"
    #     input=(data['name'],data['age'],data['phone'])
    #     cur.execute(sql_select_query,input)
    #     if cur.rowcount >0:
    #         return{"message":"updated successfully"}
    #     else:
    #         return{"message":"Nothing to update"}

    # def user_delete(self,id):
    #     cur=self.database()
    #     # data= json.loads(id)
    #     cur.execute="Delete * from users where id=%s"
        
    #     if cur.rowcount >0:
    #         return{"message":"Delete successfully"}
    #     else:
    #         return{"message":"Nothing to Delete"}
    

        
class user_model():
    
    def ErrorJson(self, data):
        return {"status":'false',"response": data}, 200
    
    def SuccessJson(self, data):
            return {"status":'true',"response": data}, 200
    
    def user_login_model(self, data):


        try:
       
            dataa = json.loads(data)

        
                
            cursor = self.database()
            
            sql_select_query = "SELECT * from users WHERE email=%s"
            cursor.execute(sql_select_query, (dataa['email'],))
            result = cursor.fetchall()


            if len(result)==0:
                return self.ErrorJson({"message":"No user found"})

            if result[0]['password']!=dataa['password']:
                return self.ErrorJson({"message":"Wrong password"})
            
        
            access_token = create_access_token(identity=result[0]['id'])
            result[0]["token"] = access_token
            return self.SuccessJson(result[0])
        
        except Exception as e:
            return self.ErrorJson({"message":str(e)})
        finally:
            cursor.close()
            del cursor
            self.conn.close()
    
    

    def database(self):
        self.conn=mysql.connector.connect(host="127.0.0.1",database="sample",port= 3306,username="root")
        self.conn.autocommit= True
        return self.conn.cursor(dictionary=True)  
    
    def user_getall_model(self):
        cur =self.database()
        cur.execute("select * from users")
        result=cur.fetchall()
        return result
    
    def user_getbyid_model(self,id):
        cur= self.database()
        sql_select_query=("select * from users where id =%s")
        cur.execute(sql_select_query,(id,))
        result =cur.fetchall()
        return result
    
    def user_add(self,data1):
        cur =self.database()
        data =json.loads(data1)
        sql_select_query="Insert into users(name,age,phone,first_name,middle_name,last_name,dept,date_of_birth,status) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        input=(data['name'],data['age'],data['phone'],data['first_name'],data['middle_name'],data['last_name'],data['dept'],data['date_of_birth'],data['status'])
        cur.execute(sql_select_query,input)
        # result=cur.fetchall()
        # return result
        if cur.rowcount>0:
            return{"message":"added successfully"}

        else:
            return{"message":"NO update"}
    
    def user_update(self,data1):
        cur=self.database()
        data=json.loads(data1)
        sql_select_query="Update  users set name=%s,age=%s,phone=%s,first_name=%s,last_name=%s,middle_name=%s,dept=%s,date_of_birth=%s,status =%s where id = %s"
        input =(data['name'],data['age'],data['phone'],data['first_name'],data['last_name'],data['middle_name'],data['dept'],data['date_of_birth'],data['status'],data['id'])
        cur.execute(sql_select_query,input)
        # result =cur.fetchall()
        # return result
        if cur.rowcount>0:
            return{"message":"Updated successfully"}

        else:
            return{"message":"NO update"}   
    
    def user_delete(self,id):
        cur=self.database()
        cur.execute="Delete * from users where id = %s" 
        if cur.rowcount>0:
            return{"message":"deleted successfully"}
        else:
            return{"message":"Nothing to Delete"}
            
    def user_get(self):
        cur=self.database()
        cur.execute("select * from department")
        result=cur.fetchall()
        return result
    

    def user_right_combine(self):
        cur=self.database()
        cur.execute("select users.name,department.dept from users right join department on users.id = department.users_id")
        result=cur.fetchall()
        return result
    

    def user_left_combine(self):
        cur=self.database()
        cur.execute("select users.name,department.dept from users left join department on users.id =department.users_id")
        result=cur.fetchall()
        return result
    
    def user_union(self):
        cur=self.database()
        cur.execute("select * from users union select * from department")
        result=cur.fetchall()
        return result
    
    def user_inner_combine(self):
        cur=self.database()
        cur.execute("select users.name,department.dept from users inner join department on users.id = department.users_id")
        result =cur.fetchall()
        return result
    

    def appliedleave(self):
        cur=self.database()
        cur.execute("select *,(select concat(first_name,' ',middle_name,' ',last_name) from users where id = user_id) as user_name from applied_leaves where status = 1")
        result =cur.fetchall()
        return result
    
    def holidaycombine(self):
        cur=self.database()
        cur.execute("select * from holiday where DATE_FORMAT(year, '%m-%d') BETWEEN DATE_FORMAT(CURDATE(), '%m-%d') AND DATE_FORMAT(DATE_ADD(CURDATE(), INTERVAL 30 DAY), '%m-%d') ORDER BY DATE_FORMAT(year, '%m-%d')")
        result =cur.fetchall()
        return result
    
    def birthday(self):
        cur=self.database()
        cur.execute("select * from users where DATE_FORMAT(date_of_birth, '%m-%d') BETWEEN DATE_FORMAT(CURDATE(), '%m-%d') AND DATE_FORMAT(DATE_ADD(CURDATE(), INTERVAL 30 DAY), '%m-%d') ORDER BY DATE_FORMAT(date_of_birth, '%m-%d')")
        result = cur.fetchall()
        return result
    
    def status(self):
        cur=self.database()
        cur.execute("select * from users where status = 1")
        result =cur.fetchall()
        return result
    
    def age(self):
        cur=self.database()
        cur.execute("select * from users where age>40")
        result =cur.fetchall()
        return result
    
    def last(self):
        cur=self.database()
        cur.execute("select * from users  where not last_name=' '")
        result =cur.fetchall()
        return result     