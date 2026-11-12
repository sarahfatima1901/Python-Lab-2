from flask import Flask, request

app=Flask(__name__)

@app.get("/")
def home_page():
    return "Hello user"

@app.get("/user")
def users_page():
    return {"response": ["John", "Mark", "Steve"]}

@app.post("/users/register")
def users_reguster():
    data=request.get_json()
    surname=data.get("Surname", "The key is not found")
    print(data)
    return{"response":surname, "status":201},201

if __name__=="__main__":
    app.run(debug=True)