// GET
        async function getStudents() {

            const response = await fetch("/students");

            const students = await response.json();

            const table = document.getElementById("studentTable");

            table.innerHTML = "";


            students.forEach(function(student) {

                table.innerHTML += `

                    <tr>

                        <td>${student.id}</td>

                        <td>${student.name}</td>

                        <td>${student.age}</td>

                        <td>${student.course}</td>

                    </tr>

                `;

            });

        }


        // POST
        async function addStudent() {

            const name =
                document.getElementById("addName").value;

            const age =
                document.getElementById("addAge").value;

            const course =
                document.getElementById("addCourse").value;


            const response = await fetch("/students", {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({

                    name: name,
                    age: age,
                    course: course

                })

            });


            const result = await response.json();

            alert(result.message);


            getStudents();

        }


        // PUT
        async function updateStudent() {

            const id =
                document.getElementById("updateId").value;

            const name =
                document.getElementById("updateName").value;

            const age =
                document.getElementById("updateAge").value;

            const course =
                document.getElementById("updateCourse").value;


            const response = await fetch(
                `/students/${id}`,
                {

                    method: "PUT",

                    headers: {
                        "Content-Type": "application/json"
                    },

                    body: JSON.stringify({

                        name: name,
                        age: age,
                        course: course

                    })

                }
            );


            const result = await response.json();

            alert(result.message);


            getStudents();

        }


        // DELETE
        async function deleteStudent() {

            const id =
                document.getElementById("deleteId").value;


            const response = await fetch(
                `/students/${id}`,
                {

                    method: "DELETE"

                }
            );


            const result = await response.json();

            alert(result.message);


            getStudents();

        }


        // Load students when page opens
        getStudents();
