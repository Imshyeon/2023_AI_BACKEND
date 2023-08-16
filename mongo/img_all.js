const fs = require('fs');
const path = require('path');

const directoryPath = 'c:/pywork/img';
const databaseName = 'images';

const conn = new Mongo();
const db = conn.getDB(databaseName);

const files = fs.readdirSync(directoryPath);

files.forEach((file) => {
  const filePath = path.join(directoryPath, file);
  const fileContent = fs.readFileSync(filePath);

  const fileInfo = {
    filename: file,
    contentType: 'image/jpeg', 
  };

  const fileObjectId = db.gridfs.files.insertOne(fileInfo);
  db.gridfs.chunks.insertOne({ files_id: fileObjectId, data: fileContent });
  print(`Uploaded ${file} to MongoDB.`);
});
