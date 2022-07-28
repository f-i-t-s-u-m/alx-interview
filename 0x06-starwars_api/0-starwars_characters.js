#!/usr/bin/node

const id = process.argv[2];

const req = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + id;
req(url, async function (err, resp, body) {
  if (!err && resp.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    for (const a of characters) {
      await new Promise(function (resolve, reject) {
        req(a, function (er, res, body) {
          console.log(JSON.parse(body).name);
        });
        resolve();
      });
    }
  }
});
