export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    console.log(task, task2);
    return [task, task2];
  }

  return [task, task2];
}
