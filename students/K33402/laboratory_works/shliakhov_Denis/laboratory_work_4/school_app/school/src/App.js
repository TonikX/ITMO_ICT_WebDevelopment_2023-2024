import React, { useEffect, useState } from "react";
import { Route, Routes, useLocation, useNavigate } from "react-router-dom";
import Login from "./page/Login";
import { PrivateRoute } from "./components/PrivateRoute";
import "./App.css";
import Registration from "./page/Registration";
import StudentList from "./page/StudentList"
import StudentForm from "./page/StudentForm/StudentForm";
import GradesList from "./page/GradesList/GradesList";
import GradesForm from "./page/GradesForm/GradesForm";
import GradeUpdateForm from "./page/GradeUpdateForm/GradeUpdateForm";
import Main from "./page/Main";
import StudentInfo from "./page/StudentInfo/StudentInfo";
import SubjectsList from "./page/SubjectList/SubjectsList";
import TeachersList from "./page/TeachersList/TeachersList";
import TeacherUpdateForm from "./page/TeacherUpdateForm/TeacherUpdateForm";

function App() {
  return (
    <div>
      <Routes>
        <Route path="/">
          <Route path="/login" element={<Login />} />
          <Route path="/registration" element={<Registration />} />

          <Route element={<PrivateRoute />}>
            <Route index element={<Main />} />
            <Route path="/student" element={<StudentList />} />
            <Route path="/student/create" element={<StudentForm />} />
            <Route path="/grade/create" element={<GradesForm />} />
            <Route path="/grade/update/:gradeId" element={<GradeUpdateForm />} />
            <Route path="student/info/:studentId" element={<StudentInfo />} />
            <Route path="/grade" element={<GradesList />} />
            <Route path="/subject/all/" element={<SubjectsList />} />
            <Route path="/teacher/all/" element={<TeachersList />} />
            <Route path="/teacher/update/:teacherId" element={<TeacherUpdateForm />} />
          </Route>
        </Route>
      </Routes>
    </div>
  );
}

export default App;
