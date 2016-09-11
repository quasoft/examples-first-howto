Title: Start MongoDB as Win32 process
Date: 2016-05-13 20:09
Category: MongoDB
Tags: mongodb, windows, start, win32

First, add MongoDB's bin folder to path and relogin/restart.

Then, start the following command, where `C:\MongoData` is the path to your database storage location. 

```batch
mongod --dbpath C:\MongoData --port 27017
```

