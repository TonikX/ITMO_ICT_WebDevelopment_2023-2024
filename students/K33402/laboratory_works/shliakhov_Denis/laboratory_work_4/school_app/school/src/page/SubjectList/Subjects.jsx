import React, {useCallback, useEffect, useState} from "react";
import useUser from "../../hooks/useUser";
import {Table} from "react-bootstrap";
import Button from "react-bootstrap/Button";

function Subjects({subject, getSubjects}) {
    const {token} = useUser();
    const [routeData, setRouteData] = useState("");
    const [teachers, setTeachers] = useState("");

    const onDelete = (subject) => {
        fetch(`http://127.0.0.1:8000/subject/delete/${subject.id}/`, {
            method: "DELETE",
            headers: {
                Authorization: `Token ${localStorage.getItem("token")}`,
            },
        }).then(() => getSubjects());
    };

    const getTeachers = useCallback(() => {
        subject.teachers.forEach(teacher =>
            fetch(`http://localhost:8000/teacher/${teacher}/`, {
                method: "GET",
                headers: {
                    Authorization: `Token ${localStorage.getItem("token")}`,
                },
            })
                .then((response) => response.json())
                .then((result) => {
                    setTeachers(prevState => prevState + `\n ${result.first_name} ${result.last_name}, Номер кабинета: ${result.room_number}`);
                })
                .catch((error) => console.error("Error fetching data:", error))
        )

    }, [subject, token]);
    useEffect(() => getTeachers(), [getTeachers]);

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
                            <td>Название</td>
                            <td>{subject.name}</td>
                        </tr>
                        <tr>
                            <td>Учителя</td>
                            <td>{teachers}</td>
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
                    onClick={() => onDelete(subject)}
                    variant="outline-primary"
                >
                    Удалить
                </Button>
            </div>
        </div>
    );
}

export default Subjects