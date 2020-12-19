import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('helloworldfirebase-24-firebase-adminsdk-88h6d-61c4cc8207.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://helloworldfirebase-24-default-rtdb.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('')

# add more data
hopper_ref = ref.child('text')
hopper_ref.delete()

# show data from path
print(ref.get())
