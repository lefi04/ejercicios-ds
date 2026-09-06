import { Estudiantes } from "./components/Estudiantes";
import { Profesores } from "./components/Profesores";
import { Cursos } from "./components/Cursos";

function App() {
  return (
    <div>
      <h1>Gestión académica</h1>
      <Estudiantes />
      <Profesores />
      <Cursos />
    </div>
  );
}

export default App;