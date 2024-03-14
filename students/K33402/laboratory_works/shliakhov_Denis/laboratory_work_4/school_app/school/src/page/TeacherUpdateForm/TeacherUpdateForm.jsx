import {useNavigate, useParams} from "react-router-dom";
import useUser from "../../hooks/useUser";
import React, {useCallback, useEffect, useState} from "react";
import {Button, Form, Row} from "react-bootstrap";

const TeacherUpdateForm = () => {
    const teacherId = useParams()
    const { setToken, token } = useUser();
    const navigate = useNavigate();
    const [formData, setFormData] = useState({
        first_name: null,
        last_name: null,
        room_number: null
    });

    const getTeacher = useCallback(() => {
        fetch(`http://127.0.0.1:8000/teacher/${teacherId.teacherId}`, {
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
    }, [teacherId, token]);

    useEffect(() => getTeacher(), [getTeacher]);

    const handleChange = (event) => {
        const { name, value } = event.target;
        setFormData({
            ...formData,
            [name]: value,
        });
    };

    const handleSubmit = (event) => {
        event.preventDefault();

        fetch(`http://127.0.0.1:8000/teacher/update/${teacherId.teacherId}/`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
                Authorization: `Token ${token}`,
            },
            body: JSON.stringify(formData),
        })
            .then((response) => response.json())
            .then((updatedFlight) => {
                console.log("Grade updated successfully:", updatedFlight);
                navigate("/teacher/all/");
            })
            .catch((error) => console.error("Error updating grade:", error));
    };

    return (
        <div className="container mt-4">
            <h2>Оценка</h2>
            <Form onSubmit={handleSubmit}>
                <Row className="mb-3">
                    <Form.Group controlId="teacher">
                        <Form.Label>Имя:</Form.Label>
                        <Form.Control
                            type="text"
                            name="first_name"
                            value={formData.first_name}
                            onChange={handleChange}
                        />
                    </Form.Group>
                </Row>

                <Row className="mb-3">
                    <Form.Group controlId="teacher">
                        <Form.Label>Фамилия:</Form.Label>
                        <Form.Control
                            type="text"
                            name="last_name"
                            value={formData.last_name}
                            onChange={handleChange}
                        />
                    </Form.Group>
                </Row>
                <Row className="mb-3">
                    <Form.Group controlId="teacher">
                        <Form.Label>Номер кабинета:</Form.Label>
                        <Form.Control
                            type="text"
                            name="last_name"
                            value={formData.room_number}
                            onChange={handleChange}
                        />
                    </Form.Group>
                </Row>

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
}

export default TeacherUpdateForm