from fastapi import FastAPI, HTTPException

from MD_User import User, Gender, Role, UpdateUser,Scanneduser
from typing import List
from uuid import uuid4, UUID
import datetime

app = FastAPI()
scannerUserDB: List[Scanneduser] = []

db: List[User] = [
    User(
        # id=UUID("59b56781-c76a-453f-afb3-336f1d761893"),
        name="Praveen",
        empid="CL885",
        emailid="praveen@colive.com",
        mobile="919994611550",
        gender=Gender.male,
        dob='03-03-2000',
        role=[Role.user]
    ),
    User(
        # id=UUID("cab90523-f48c-4bc6-a312-1c29ada7daf9"),
        name="Udayakumar",
        empid="CL098",
        emailid="User1@email.com",
        mobile="919994411550",
        gender=Gender.male,
        dob='23-04-1990',
        role=[Role.admin]
    ),
    User(
        # id=UUID("93e122c3-9cd7-4e57-8759-3ecdadab04cb"),
        name="Manojkumar",
        empid="CL198",
        emailid="manoj@colive.com",
        mobile="919994811550",
        gender=Gender.female,
        dob='03-03-2000',
        role=[Role.user]
    ),
    User(
        # id=UUID("93e122c3-9cd7-4e57-8759-3ecdadab04cv"),
        name="Suriya",
        empid="CL962",
        emailid="suriya@colive.com",
        mobile="918489605424",
        gender=Gender.male,
        dob='21-07-1993',
        role=[Role.user]
    ),
    User(
        # id=UUID("93e122c3-9cd7-4e57-2759-3ecdadab04cv"),
        name="Yogesh",
        empid="CL1076",
        emailid="yogesh@colive.com",
        mobile="918681099866",
        gender=Gender.male,
        dob='03-03-2000',
        role=[Role.user]
    ),
    User(
        # id=UUID("93e122c3-9cd7-4e57-8709-3ecdadab04cv"),
        name="Sajja venu",
        empid="CL1039",
        emailid="sajja@colive.com",
        mobile="919573932851",
        gender=Gender.male,
        dob='27-06-1997',
        role=[Role.user]
    ),
    User(
        # id=UUID("93e122c3-9cd7-4e57-8709-3ecdadab04cv"),
        name="Karthik kumar",
        empid="CL1100",
        emailid="karthikkumar@colive.com",
        mobile="919741064329",
        gender=Gender.male,
        dob='31-01-1998',
        role=[Role.user]
    ),
    User(
        # id=UUID("93e122c3-9cd7-4e57-8709-3ecdadab04cv"),
        name="Ganesh S",
        empid="CL685",
        emailid="ganesh@colive.com",
        mobile="919741064329",
        gender=Gender.male,
        dob='31-01-1998',
        role=[Role.user]
    ),
    User(
        # id=UUID("93e122c3-9cd7-4e57-8709-3ecdadab04cv"),
        name="Vijay Sivasankaran",
        empid="CL914",
        emailid="vijays@colive.com",
        mobile="919741064329",
        gender=Gender.male,
        dob='31-01-1998',
        role=[Role.user]
    )
]


@app.get("/")
async def root():
    return {"Hello": "World"}


@app.get("/api/v1/users")
async def fetch_users():
    return {"UserData":db}

@app.get("/api/v1/users/{emp_id}")
async def fetch_users(emp_id: str):
    for user in db:
        #print("User ID", user.emailid)
        if user.empid == emp_id:
            return user
    return {"Failure":"Not user found!"}


@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
        raise HTTPException(
            status_code=404,
            detail=f"user with id: {user_id} does not exists"
        )


@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UpdateUser, user_id: UUID):
    for user in db:
        print("User ID",user.id)
        if user.id == user_id:
            if user_update.name is not None:
                user.name = user_update.name
            if user_update.emailid is not None:
                user.emailid = user_update.emailid
            if user_update.mobile is not None:
                user.mobile = user_update.mobile
            if user_update.role is not None:
                user.role = user_update.role
            return
    raise HTTPException(
            status_code=404,
            detail=f"user with id: {user_id} does not exists"
        )


@app.post("/api/v1/scan/addDetails")
async def addScannedUsers(user: Scanneduser):
    inserted = False
    filtered_arr = [p for p in scannerUserDB if p.empid == user.empid]
    if len(filtered_arr) == 0:
        x = datetime.datetime.now()
        x = x.strftime("%b-%d-%Y %H:%M:%S")
        user.date = x
        scannerUserDB.append(user)
       # return scannerUserDB
    else:
        print(f'Alread logged in {user.name}')

@app.get("/api/v1/scan/details")
async def getScannedUsers():
    return scannerUserDB