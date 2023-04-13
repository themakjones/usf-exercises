const express = require("express");
const {
  findMean,
  findMedian,
  findMode,
  validateAndConfigNums,
} = require("./operations");
const ExpressError = require("./expressError");

const app = express();

app.get("/mean", (req, res) => {
  const nums = req.query.nums;
  let numsArr = validateAndConfigNums(nums);
  let mean = findMean(numsArr);
  return res.status(200).json({
    operation: "mean",
    value: mean,
  });
});

app.get("/median", (req, res) => {
  const nums = req.query.nums;
  let numsArr = validateAndConfigNums(nums);
  let median = findMedian(numsArr);
  return res.status(200).json({
    operation: "median",
    value: median,
  });
});

app.get("/mode", (req, res) => {
  const nums = req.query.nums;
  let numsArr = validateAndConfigNums(nums);
  let mode = findMode(numsArr);
  return res.status(200).json({
    operation: "mode",
    value: mode,
  });
});

app.use((err, req, res, next) => {
  let status = err.status || 500;
  let message = err.message;

  return res.status(status).json({
    error: {message, status},
  });
});

app.listen(3000, function () {
  console.log("App on port 3000 started");
});
