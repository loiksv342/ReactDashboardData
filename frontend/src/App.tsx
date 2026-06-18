import { BrowserRouter, Route, Routes } from "react-router-dom";
import HeaderSection from "./components/HeaderSection/HeaderSection";
import AboutStackProject from "./components/AboutStackProject/AboutStackProject";

export default function App() {
  return (
    <BrowserRouter>
      <HeaderSection />
        <Routes>
          <Route path="/" element={<App />} />
          <Route path="/aboutprojectstack" element={<AboutStackProject />} />
        </Routes>
      </BrowserRouter>
    ) 
}