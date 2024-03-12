import React, {useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import Button from "react-bootstrap/Button";
import useUser from "../../hooks/useUser";


function Student({ student, getStudents }) {
  const navigate = useNavigate();
  const { token } = useUser();
  const [routeData, setRouteData] = useState("");

  const onDelete = (student) => {
    fetch(`http://127.0.0.1:8000/student/delete/${student.id}/`, {
      method: "DELETE",
      headers: {
        Authorization: `Token ${token}`,
      },
    }).then(() => getStudents());
  };

  return (
    <div className="cell-container">
      <div>
        <div>
           <div>
              {student.first_name} {student.last_name}
            </div>
        </div> 
      </div>
      <div className="cell-route">
        
        <div>{routeData.destination_point}</div>
      </div>
      <div className="cell-button-group">
        <Button
            onClick={() => navigate(`student/info/${student.id}`)}
            variant="outline-primary"
          >
            Посмотреть
          </Button>

        <Button
            onClick={() => onDelete(student)}
            variant="outline-primary"
          >
            Удалить
          </Button>
      </div>
    </div>
  );
}

export default Student;