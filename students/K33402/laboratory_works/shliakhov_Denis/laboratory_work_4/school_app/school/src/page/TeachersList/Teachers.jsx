import useUser from "../../hooks/useUser";
import React, {useCallback, useEffect, useState} from "react";
import {Table} from "react-bootstrap";
import Button from "react-bootstrap/Button";
import {useNavigate} from "react-router-dom";

function Teachers({teacher, getTeachers}) {
    const navigate = useNavigate();
    const {token} = useUser();
    const [routeData, setRouteData] = useState("");
    const [subjects, setSubjects] = useState("");

    const onDelete = (teacher) => {
        fetch(`http://127.0.0.1:8000/teacher/delete/${teacher.id}/`, {
            method: "DELETE",
            headers: {
                Authorization: `Token ${localStorage.getItem("token")}`,
            },
        }).then(() => getTeachers());
    };

    const getSubjects = useCallback(() => {
        teacher.subjects.forEach( subject =>
            fetch(`http://localhost:8000/subject/${subject}/`, {
                method: "GET",
                headers: {
                    Authorization: `Token ${localStorage.getItem("token")}`,
                },
            })
                .then((response) => response.json())
                .then((result) => {
                    setSubjects(prevState => prevState + " " + result.name);
                })
                .catch((error) => console.error("Error fetching data:", error))
        )

    }, [teacher, token]);
    useEffect(() => getSubjects(), [getSubjects]);

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
                            <td>Учитель</td>
                            <td>{teacher.first_name} {teacher.last_name}</td>
                        </tr>
                        <tr>
                            <td>Номер кабинета</td>
                            <td>{teacher.room_number}</td>
                        </tr>
                        <tr>
                            <td>Предметы</td>
                            <td>{subjects}</td>
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
                    onClick={() => navigate(`teacher/update/${teacher.id}`)}
                    variant="outline-primary"
                >
                    Редактировать
                </Button>

                <Button
                    onClick={() => onDelete(teacher)}
                    variant="outline-primary"
                >
                    Удалить
                </Button>
            </div>
        </div>
    );
}

export default Teachers