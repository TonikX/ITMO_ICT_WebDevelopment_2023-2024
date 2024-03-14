import React, {useState, useEffect, useCallback} from "react";
import { useParams } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import useUser from "../../hooks/useUser";
import { Form, Button, Row, Col } from "react-bootstrap";

const GradeUpdateForm = () => {
  const { gradeId } = useParams();
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    lesson: null,
    student: null,
    grade: null,
  });

  const [availableLessons, setAvailableLessons] = useState([]);
  const [availableStudents, setAvailableStudents] = useState([]);

  const getGrades = useCallback(() => {
    fetch(`http://127.0.0.1:8000/grade/${gradeId}` , {
      method: "GET",
      headers: {
        Authorization: `Token ${localStorage.getItem("token")}`,
      }
    })
        .then((response) => response.json())
        .then((data) => {
          setFormData(data);
        })
        .catch((error) => console.error("Error fetching grade data:", error));
  }, [gradeId])

  const getLessons = useCallback(() => {
    fetch("http://127.0.0.1:8000/lesson/all", {
      method: "GET",
      headers: {
        Authorization: `Token ${localStorage.getItem("token")}`,
      },
    })
        .then((response) => response.json())
        .then((data) => {
          setAvailableLessons(data);
        })
        .catch((error) => console.error("Error fetching data:", error));
  }, [gradeId])

  const getStudents = useCallback(() => {
    fetch("http://127.0.0.1:8000/student/all", {
      method: "GET",
      headers: {
        Authorization: `Token ${localStorage.getItem("token")}`,
      },
    })
        .then((response) => response.json())
        .then((result) => {
          setAvailableStudents(result);
        })
        .catch((error) => console.error("Error fetching data:", error));
  }, [gradeId])


  useEffect(() => getGrades(), [getGrades]);
  useEffect(() => getLessons(), [getLessons]);
  useEffect(() => getStudents(), [getStudents]);
  const handleChange = (event) => {
    const { name, value } = event.target;
      setFormData({
        ...formData,
        [name]: value,
      });
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    fetch(`http://127.0.0.1:8000/grade/update/${gradeId}/`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${localStorage.getItem("token")}`,
      },
      body: JSON.stringify(formData),
    })
      .then((response) => response.json())
      .then((updatedFlight) => {
        console.log("Grade updated successfully:", updatedFlight);
        navigate("/");
      })
      .catch((error) => console.error("Error updating grade:", error));
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
                {student.first_name} {student.last_name}
              </option>
            ))}
          </Form.Select>
        </Form.Group>

        <Form.Group controlId="lesson">
          <Form.Label>Расписание:</Form.Label>
          <Form.Select
            name="lesson"
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
          Обновить
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
};

export default GradeUpdateForm;