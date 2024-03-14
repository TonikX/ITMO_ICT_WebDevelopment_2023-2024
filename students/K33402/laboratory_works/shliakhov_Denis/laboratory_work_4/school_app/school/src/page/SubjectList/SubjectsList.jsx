import useUser from "../../hooks/useUser";
import React, {useCallback, useEffect, useState} from "react";
import Subjects from "./Subjects";

function SubjectsList() {
    const {token} = useUser();
    const [subjects, setSubjects] = useState([]);

    const getSubjects = useCallback(() => {
        fetch("http://localhost:8000/subject/all/", {
            method: "GET",
            headers: {
                Authorization: `Token ${localStorage.getItem("token")}`,
            },
        })
            .then((response) => response.json())
            .then((result) => {
                setSubjects(result);
            })
            .catch((error) => console.error("Error fetching data:", error));
    }, [token]);

    useEffect(() => getSubjects(), [getSubjects]);

    return (
        <div>
            {subjects ? (
                <div className="cell-group">
                    {subjects.map((subject, id) => (
                        <Subjects subject={subject} getSubjects={getSubjects} key={id}/>
                    ))}
                </div>
            ) : (
                <></>
            )}
        </div>
    );
}

export default SubjectsList;