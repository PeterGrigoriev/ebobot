import { BrowserRouter, Route, Routes } from "react-router-dom";

import { ChatPage } from "@/pages/ChatPage";
import { PersonaSelectPage } from "@/pages/PersonaSelectPage";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<PersonaSelectPage />} />
        <Route path="/chat/:personaId" element={<ChatPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
