function getListStudents() {
  let students = [];

  let guillaume = {
    id: 1,
    firstName: "Guillaume",
    location: "San Francisco"
  };
  students.push(guillaume);

  let james = {
    id: 2,
    firstName: "James",
    location: "Columbia"
  };
  students.push(james);

  let serena = {
    id: 5,
    firstName: "Serena",
    location: "San Francisco"
  };
  students.push(serena);

  return students;
}
