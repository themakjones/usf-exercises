const fs = require("fs");
const axios = require("axios");

function cat(path) {
  fs.readFile(path, "utf8", (err, data) => {
    if (err) {
      console.log(err);
      process.exit(1);
    }
    console.log(data);
  });
}

function webCat(path) {
  let webPromise = axios.get(path);

  webPromise
    .then((res) => {
      console.log(res.data);
    })
    .catch(() => {
      console.log("An error occured");
    });
}
webCat(process.argv[2]);
