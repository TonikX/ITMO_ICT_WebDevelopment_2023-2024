import React, { useEffect, useState } from "react";
import useUser from "../../hooks/useUser";
import { useNavigate } from "react-router-dom";
import { Form, Button, Row, Col } from "react-bootstrap";


function GradesForm() {
  const { setToken, token } = useUser();
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    lesson: null,
    student: null,
    grade: null,
  });

  const [availableSchedules, setAvailableSchedules] = useState([]);
  const [availableStudents, setAvailableStudents] = useState([]);


  useEffect(() => {
    fetch("http://127.0.0.1:8000/lesson/all", {
      method: "GET",
      headers: {
        Authorization: `Token ${token}`,
      },
    })
      .then((response) => response.json())
      .then((result) => {
        setAvailableSchedules(result);
      })
      .catch((error) => console.error("Error fetching data:", error));

    fetch("http://127.0.0.1:8000/student/all", {
        method: "GET",
        headers: {
          Authorization: `Token ${token}`,
        },
      })
        .then((response) => response.json())
        .then((result) => {
          setAvailableStudents(result);
        })
        .catch((error) => console.error("Error fetching data:", error));

  }, [token]);

  const handleChange = (event) => {
    const { name, value } = event.target;
      setFormData({
        ...formData,
        [name]: value,
      });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log("Form submitted:", formData);
    fetch("http://127.0.0.1:8000/grade/create/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${localStorage.getItem("token")}`,
      },
      body: JSON.stringify(formData),
    })
      .then((response) => response.json())
      .then((result) => {
        console.log("Success:", result);
        navigate("/");
      })
      .catch((error) => console.error("Error:", error));
  };

  return (
    <div className="container mt-4">
      <h2>Оценка</h2>
      <Form onSubmit={handleSubmit}>
        <Row className="mb-3">
            <Form.Group controlId="student">
                <Form.Label>Оценка:</Form.Label>
                        <Form.Control
                    type="text"
                    name="grade"
                    value={formData.grade}
                    onChange={handleChange}
                />
            </Form.Group>
        </Row>

        <Form.Group controlId="student">
          <Form.Label>Ученик:</Form.Label>
          <Form.Select
            name="student"
            value={formData.student}
            onChange={handleChange}
          >
            <option value="">Выбор ученика</option>
            {availableStudents.map((student) => (
              <option key={student.id} value={student.id}>
                {student.id} {student.first_name} {student.last_name}
              </option>
            ))}
          </Form.Select>
        </Form.Group>

        <Form.Group controlId="schedule">
          <Form.Label>Расписание:</Form.Label>
          <Form.Select
            name="schedule"
            value={formData.lesson}
            onChange={handleChange}
          >
            <option value="">Выбор расписания</option>
            {availableStudents.map((lesson) => (
              <option key={lesson.id} value={lesson.id}>
                {lesson.id} {lesson.date}
              </option>
            ))}
          </Form.Select>
        </Form.Group>


        <Button variant="primary" type="submit">
          Создать
        </Button>
        <Button
          variant="primary"
          onClick={() => {
            navigate("/");
          }}
          className="m-3"
        >
          На главную
        </Button>
      </Form>
    </div>
  );
}

export default GradesForm;