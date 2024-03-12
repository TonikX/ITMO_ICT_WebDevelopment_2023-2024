import React, { useCallback, useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import Button from "react-bootstrap/Button";
import useUser from "../../hooks/useUser";
import {Table} from "react-bootstrap";


function Grades({ grade, getGrades }) {
  const navigate = useNavigate();
  const { token } = useUser();
  const [routeData, setRouteData] = useState("");
  const [student, setStudent] = useState("");
  const [lesson, setLesson] = useState("");

    const onDelete = (grade) => {
    fetch(`http://127.0.0.1:8000/grade/delete/${grade.id}/`, {
      method: "DELETE",
      headers: {
        Authorization: `Token ${token}`,
      },
    }).then(() => getGrades());
    };

    const getStudent = useCallback(() => {
        fetch(`http://localhost:8000/student/${grade.student}/`, {
            method: "GET",
            headers: {
                Authorization: `Token ${token}`,
            },
        })
            .then((response) => response.json())
            .then((result) => {
                setStudent(result);
            })
            .catch((error) => console.error("Error fetching data:", error));
    }, [grade,token]);
    useEffect(() => getStudent(), [getStudent]);

    const getlesson = useCallback(() => {
        fetch(`http://localhost:8000/lesson/${grade.lesson}/`, {
            method: "GET",
            headers: {
                Authorization: `Token ${token}`,
            },
        })
            .then((response) => response.json())
            .then((result) => {
                setLesson(result);
            })
            .catch((error) => console.error("Error fetching data:", error));
    }, [grade,token]);
    useEffect(() => getlesson(), [getlesson]);

    return (
    <div className="cell-container">
      <div>
        <div>
            <Table striped bordered hover>
                <thead>
                <tr>
                    <th>Параметр</th>
                    <th>Значение</th>
                </tr>
                </thead>
                <tbody>
                <tr>
                    <td>Ученик</td>
                    <td>{student.first_name} {student.last_name}</td>
                </tr>
                <tr>
                    <td>Оценка</td>
                    <td>{grade.grade}</td>
                </tr>
                <tr>
                    <td>Дата получения оценки</td>
                    <td>{lesson.date}</td>
                </tr>
                </tbody>
            </Table>
        </div>
      </div>
      <div className="cell-route">

        <div>{routeData.destination_point}</div>
      </div>
      <div className="cell-button-group">

        <Button
            onClick={() => navigate(`grade/update/${grade.id}`)}
            variant="outline-primary"
          >
            Редактировать
        </Button>

        <Button
            onClick={() => onDelete(grade)}
            variant="outline-primary"
          >
            Удалить
        </Button>
      </div>
    </div>
    );
    }

export default Grades;