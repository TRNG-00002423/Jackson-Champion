from flask import Flask, jsonify, request

app = Flask(__name__)

students = {
    1: {"id": 1, "name": "Alice", "course": "Computer Science"},
    2: {"id": 2, "name": "Bob", "course": "Data Science"},
    3: {"id": 3, "name": "Kaitlyn", "course": "Computer Science"},
    4: {"id": 4, "name": "John", "course": "Environmental Science"},
    5: {"id": 5, "name": "Trevor", "course": "Data Science"},
    6: {"id": 6, "name": "Benjamin", "course": "Computer Science"},
    7: {"id": 7, "name": "Madison", "course": "Electrical Engineering"},
    8: {"id": 8, "name": "Jeremy", "course": "Physics"}
}

next_id = 9

@app.get("/students")
def get_students():
    return jsonify(list(students.values()))


@app.get("/students/<int:student_id>")
def get_student(student_id):
    student = students.get(student_id)

    if not student:
        return jsonify({"error": "Student not found"}), 404
    return jsonify(student)


@app.post("/students")
def create_student():
    global next_id
    
    data = request.get_json(silent=True)
    
    if not data:
        return jsonify({"error": "JSON body required"}), 400
    
    new_student = { "id": next_id,"name": data["name"], "course": data["course"]}
    
    students[next_id] = new_student
    next_id += 1
    
    return jsonify(new_student)

@app.put("/students/<int:student_id>")
def update_student(student_id):
    student = students.get(student_id)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    data = request.get_json()

    student["name"] = data.get("name", student["name"])
    student["course"] = data.get("course", student["course"])

    return jsonify(student)

@app.delete("/students/<int:student_id>")
def delete_student(student_id):
    if student_id not in students:
        return jsonify({"error": "Student not found"}), 404

    del students[student_id]

    return jsonify({"message": "Student deleted successfully"})


if __name__ == "__main__":
    app.run(debug=True)
    