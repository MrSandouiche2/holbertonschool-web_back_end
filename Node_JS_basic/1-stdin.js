const readline = require('readline');

console.log('Welcome to Holberton School, what is your name?');

if (process.stdin.isTTY) {
  // Interactive mode: use readline to read a line
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  rl.question('', (name) => {
    console.log(`Your name is: ${name}`);
    rl.close();
  });
} else {
  // Non-interactive (piped input): read all data until end
  let input = '';

  process.stdin.on('data', (chunk) => {
    input += chunk;
  });

  process.stdin.on('end', () => {
    const name = input.trim();
    console.log(`Your name is: ${name}`);
    console.log('This important software is now closing');
  });
}
