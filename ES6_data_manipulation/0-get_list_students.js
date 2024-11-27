function getListStudents() {
  const students = [];

  const guillaume = {
    id: 1,
    firstName: 'Guillaume',
    location: 'San Francisco',
  };
  students.push(guillaume);

  const james = {
    id: 2,
    firstName: 'James',
    location: 'Columbia',
  };
  students.push(james);

  const serena = {
    id: 5,
    firstName: 'Serena',
    location: 'San Francisco',
  };
  students.push(serena);

  return students;
}

const students = getListStudents();
console.log(students);
