#!/usr/bin/node

// create request instance
const request = require('request');

// function to compute number of tasks completed by user ID
function completedTasks (apiUrl) {
  request.get(apiUrl, (err, response, body) => {
    if (err) {
      console.log(err);
    } if (response.statusCode !== 200) {
      console.log('code:', response.statusCode);
    } else {
      const tasks = JSON.parse(body);
      // declare empty object to store counts of completed tasks
      const completedTasksById = {};

      for (const task of tasks) {
        if (task.completed === true) {
          const userId = task.userId;
          completedTasksById[userId] = (completedTasksById[userId] || 0) + 1;
        }
      }
      console.log(completedTasksById);
    }
  });
}

// store url in variable
const apiUrl = process.argv[2];

// call function
completedTasks(apiUrl);
