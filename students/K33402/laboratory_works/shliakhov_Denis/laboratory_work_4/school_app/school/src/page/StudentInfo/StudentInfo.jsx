import React, { useCallback, useEffect, useState } from "react";
import {useParams} from "react-router-dom";


function StudentInfo() {
    const studentId = useParams()
    const [group , setGroup] = useState("")
    const [student , setStudent] = useState([])

    const getStudent = useCallback(() => {fetch(`http://127.0.0.1:8000/student/${studentId.studentId}`,{
        method: "GET",
        headers: {
            Authorization: `Token ${localStorage.getItem("token")}`,
        },
    })
        .then(response => response.json())
        .then(data => {setStudent(data)})
        .catch(error => console.error('Ошибка:', error));}, [studentId.studentId]);

    useEffect(() => getStudent(), [getStudent]);

    const getGroup = useCallback(() => {fetch(`http://127.0.0.1:8000/group/${student.group}`,{
        method: "GET",
        headers: {
          Authorization: `Token ${localStorage.getItem("token")}`,
        },
      })
        .then(response => response.json())
        .then(data => {setGroup(data)})
        .catch(error => console.error('Ошибка:', error));}, [student]);

    useEffect(() => getGroup(), [getGroup]);
    return (
      <div>
        <h3>{student.first_name} {student.last_name}</h3>
        <p>Класс: {group.group_name}</p>
        <h3>Оценки:</h3>
        <ul>
        {student.grade_set?.map(grade => (
          <li key={grade.id}>
            Оценка: {grade.grade}
          </li>
        ))}
      </ul>
      </div>
    );
}

export default StudentInfo;