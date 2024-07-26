#!/usr/bin/node

const request = require('request');

if (process.argv.length === 2) {
  console.error('please provide at least one argument');
  process.exit(1);
}

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
    process.exit(1);
  }
  const taskCompletion = {};
  if (response.statusCode === 200) {
    const todos = JSON.parse(body);
    for (const todo of todos) {
      if (todo.completed === false) {
        continue;
      }
      if (todo.userId in taskCompletion) {
        taskCompletion[todo.userId]++;
      } else {
        taskCompletion[todo.userId] = 1;
      }
    }
  }

  console.log(taskCompletion);
});
