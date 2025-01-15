import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred , {
    'databaseURL' : ""
})

ref = db.reference('Students')

data = {
    "23232":
        {
            "name": "Pushkar Kashyap",
            "course": "BCA",
            "starting_year": 2022,
            "total_attendance": 18,
            "standing": "A",
            "year": 2,
            "last_attendance_time": "2024-12-11 08:00:00"
        },
    "13232":
        {
            "name": "Ken Roy",
            "course": "BCA",
            "starting_year": 2022,
            "total_attendance": 11,
            "standing": "B",
            "year": 2,
            "last_attendance_time": "2024-12-11 08:00:00"
        },
    "145177":
        {
            "name": "Rahul Sharma",
            "course": "BBA",
            "starting_year": 2022,
            "total_attendance": 9,
            "standing": "C",
            "year": 3,
            "last_attendance_time": "2024-12-11 08:00:00"
        }
}

for key,value in data.items():
    ref.child(key).set(value)

