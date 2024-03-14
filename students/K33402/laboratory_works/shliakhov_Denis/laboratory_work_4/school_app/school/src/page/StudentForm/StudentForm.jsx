import React, { useEffect, useState } from "react";
import useUser from "../../hooks/useUser";
import { useNavigate } from "react-router-dom";
import { Form, Button, Row, Col } from "react-bootstrap";


function StudentForm() {
  const { setToken, token } = useUser();
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    first_name: "",
    last_name: "",
    group: null,

  });

  const [availableClasses, setAvailableClasses] = useState([]);


  useEffect(() => {
    fetch("http://127.0.0.1:8000/group/all", {
      method: "GET",
      headers: {
        Authorization: `Token ${token}`,
      },
    })
      .then((response) => response.json())
      .then((result) => {
        setAvailableClasses(result);
      })
      .catch((error) => console.error("Error fetching data:", error));
  }, [token]);

  const handleChange = (event) => {
    const { name, value } = event.target;

    if (name === "group") {
      const selectedValues = Array.from(
        event.target.selectedOptions,
        (option) => option.value
      );

      setFormData({
        ...formData,
        [name]: selectedValues[0],
      });
    } else {
      setFormData({
        ...formData,
        [name]: value,
      });
    }
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log("Form submitted:", formData);
    fetch("http://127.0.0.1:8000/student/create/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${token}`,
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
      <h2>Ученик</h2>
      <Form onSubmit={handleSubmit}>
        <Row className="mb-3">
            <Form.Group controlId="student">
                <Form.Label>Имя:</Form.Label>
                        <Form.Control
                    type="text"
                    name="first_name"
                    value={formData.first_name}
                    onChange={handleChange}
                />
              <Form.Label>Фамилия:</Form.Label>
                        <Form.Control
                    type="text"
                    name="last_name"
                    value={formData.last_name}
                    onChange={handleChange}
                />
            </Form.Group>
        </Row>

        <Form.Group controlId="group">
          <Form.Label>Класс:</Form.Label>
          <Form.Select
            name="group"
            value={formData.group}
            onChange={handleChange}
          >
            <option value="">Выбор класса</option>
            {availableClasses.map((group) => (
              <option key={group.id} value={group.id}>
                {group.group_name}
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

export default StudentForm;