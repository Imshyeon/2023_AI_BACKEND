function myCommands() {
  db.Score.find({ kor: { $gt: 90 } }).forEach((doc) => {
    printjson(doc);
  });
}

// mongosh mydb my_commands.js
myCommands()