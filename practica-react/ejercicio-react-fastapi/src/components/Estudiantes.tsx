import { useEffect, useState } from "react";
import { getEstudiantes } from "../api";
import type { Estudiante } from "../types";

export function Estudiantes() {
  const [estudiantes, setEstudiantes] = useState<Estudiante[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    getEstudiantes()
      .then(setEstudiantes)
      .catch((err) => setError(err.message));
  }, []);

  if (error) return <p>Error: {error}</p>;

  return (
    <section>
      <h2>Estudiantes</h2>
      <ul>
        {estudiantes.map((e) => (
          <li key={e.id}>
            {e.nombre} (legajo {e.legajo})
          </li>
        ))}
      </ul>
    </section>
  );
}