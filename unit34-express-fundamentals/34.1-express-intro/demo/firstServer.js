const express = require("express");
const ExpressError = require("./expressError");

const app = express();

app.use(express.json());
app.use(express.urlencoded({extended: true}));

app.use((req, res, next) => {
  console.log("The server got a request");
  next();
});

app.get("/dogs", (req, res) => {
  console.log("You asked for /dogs");
  res.send("Dogs are coolz");
});

app.get("/chickens", (res, req) => {
  console.log("You requested /chickens");
  res.send("chikenz");
});

app.post("/chickens", (req, res) => {
  res.send("You sent a post request to /chickens");
});

const greetings = {
  en: "hello",
  fr: "bonjour",
  ic: "hallo",
  js: "konnichiwa",
};

app.get("/greet/:language", (req, res) => {
  const lang = req.params.language;
  const greeting = greetings[lang];

  !greeting ? res.send("Invalid Language") : res.send(greeting);
});

app.get("/search", (req, res) => {
  const {term = "birds", sort = "top"} = req.query;
  return res.send(`Term is: ${term}, sort is: ${sort}`);
});

app.get("/show-me-headers", (req, res) => {
  return res.send(req.headers);
});

app.post("/register", (res, req) => {
  res.send(res.body);
});

const CANDIES = [
  {name: "twix", qty: 24, price: 1.99},
  {name: "snickers", qty: 15, price: 1.89},
  {name: "resees", qty: 38, price: 1.49},
];

app.get("/candies", (res, req) => {
  res.json(CANDIES);
});

app.post("/candies", (res, req) => {
  CANDIES.push(req.body);
  res.statusCode(201).json(CANDIES);
});

// example route below, there is no USERS defined

app.get("/users/:username", function (req, res) {
  const user = USERS.find((u) => u.username === req.params.username);

  if (!user) throw new ExpressError("Not found!", 404);

  return res.send({user});
});

app.listen(3000, function () {
  console.log("App on port 3000 started");
});
