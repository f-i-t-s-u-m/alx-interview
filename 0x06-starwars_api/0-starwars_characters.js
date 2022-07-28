#!/usr/bin/node

const id = process.argv[2];

const req = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + id + '/?format=json';
req(url, function (err, resp, body) {
  if (!err && resp.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    characters.forEach(function (a) {
      req(a, function (er, res, body) {
        console.log(JSON.parse(body).name);
      });
    });
  }
});
