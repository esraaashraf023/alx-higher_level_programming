#!/usr/bin/node

const args = process.argv.slice(2); // Exclude the first two elements of process.argv (path to node and script)

if (args[0]) {
  console.log(args[0]);
} else {
  console.log('No argument');
}
