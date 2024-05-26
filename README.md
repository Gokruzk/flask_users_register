# Flask User Register

Flask api for register users in mongodb.

## Installation

Go to mongodb page to download [mongodb community server](https://www.mongodb.com/try/download/community) and [mongosh](https://www.mongodb.com/try/download/atlascli).

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the followings modules.

```
pip install flask pymongo flask_pymongo
```
## Database
Use the shell to run mongodb
```
mongod
```
Use mongosh to create database
```
mongosh
use ochestra
db.createCollection("users")
```
