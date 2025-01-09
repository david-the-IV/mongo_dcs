db = connect("mongodb://root:rootpassword@localhost:27017/admin");

// Create user 'edy'
db.getSiblingDB('admin').createUser({
  user: "edy",
  pwd: "20edy25",
  roles: [
    { role: "readWrite", db: "admin" }
  ]
});

// Create user 'ridho'
db.getSiblingDB('admin').createUser({
  user: "ridho",
  pwd: "20ridho25",
  roles: [
    { role: "readWrite", db: "admin" }
  ]
});

// Database and collection for DHT22 logs
db = db.getSiblingDB('dht22_logs');
db.createCollection('log_dht');

// Database and collection for Biometrics logs
db = db.getSiblingDB('biometrics_logs');
db.createCollection('biometrics');

// Database and collection for Tuya App logs
db = db.getSiblingDB('tuya_app_logs');
db.createCollection('tuya_app');

// Database and collection for RTSP App logs
db = db.getSiblingDB('rtsp_app_logs');
db.createCollection('rtsp_app');
