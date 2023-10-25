#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

if (process.argv.length <= 2) {
  console.error('Provide API url...');
  process.exit(1);
}

request.get(apiUrl, (error, response, body) => {
  const todos = JSON.parse(body);
  const completedTasks = {};
  if (error) {
    console.error(error);
  }

  todos.forEach(task => {
    if (task.completed) {
      completedTasks[task.userId] = (completedTasks[task.userId] || 0) + 1;
    }
  });

  console.log(completedTasks);
});
