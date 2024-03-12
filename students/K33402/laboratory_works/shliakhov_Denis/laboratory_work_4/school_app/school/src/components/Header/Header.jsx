import React from "react";
import Button from "react-bootstrap/Button";
import { useNavigate, useParams } from "react-router-dom";
import useUser from "../../hooks/useUser";
import {Col, Row} from "react-bootstrap";

function Header({ username }) {
  const navigate = useNavigate();
  const { setToken, token } = useUser();

  const onLogout = () => {
    setToken("");
    localStorage.clear()
    navigate("login");
  };

  return (
    <header>
      <div className="container header-div">
        <div className="lable">
          <Row>
            <Col>{username}</Col>
            <Col>Школа № 15</Col>
            <Col>
              <Button
                variant="outline-danger"
                className="logout-button"
                onClick={() => onLogout()}>
              Выйти
            </Button>
            </Col>
          </Row>
        </div>
        <div className="header-left-cell">

        </div>
      </div>
    </header>
  );
}

export default Header;