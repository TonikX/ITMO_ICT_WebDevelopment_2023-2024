import useUser from "../../hooks/useUser";
import React, {useCallback, useEffect, useState} from "react";
import Teachers from "./Teachers";

function TeachersList() {
    const {token} = useUser();
    const [teachers, setTeachers] = useState([]);

    const getTeachers = useCallback(() => {
        fetch("http://localhost:8000/teacher/all/", {
            method: "GET",
            headers: {
                Authorization: `Token ${localStorage.getItem("token")}`,
            },
        })
            .then((response) => response.json())
            .then((result) => {
                setTeachers(result);
            })
            .catch((error) => console.error("Error fetching data:", error));
    }, [token]);

    useEffect(() => getTeachers(), [getTeachers]);

    return (
        <div>
            {teachers ? (
                <div className="cell-group">
                    {teachers.map((teacher, id) => (
                        <Teachers teacher={teacher} getTeachers={getTeachers} key={id}/>
                    ))}
                </div>
            ) : (
                <></>
            )}
        </div>
    );
}

export default TeachersList