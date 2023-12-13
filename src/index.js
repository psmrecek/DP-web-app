import React from 'react';
import ReactDOM from 'react-dom';
import { HashRouter as Router, Routes, Route } from 'react-router-dom';
import './index.css';
import SurveyComponent from "./SurveyComponent";

const App = () => (
  <Router>
    <Routes>
      <Route path="/h" element={<SurveyComponent experiment_type="h" />} />
      <Route path="/fg" element={<SurveyComponent experiment_type="fg" />} />
    </Routes>
  </Router>
);

ReactDOM.render(<App />, document.getElementById('root'));