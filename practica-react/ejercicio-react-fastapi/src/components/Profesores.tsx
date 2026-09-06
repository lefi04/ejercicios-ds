import { useEffect, useState } from "react";
import { getProfesores } from "../api";
import type { Profesor } from "../types";

export function Profesores() {
  const [profesores, setProfesores] = useState<Profesor[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    getProfesores()
      .then(setProfesores)
      .catch((err) => setError(err.message));
  }, []);

  if (error) return <p>Error: {error}</p>;

  return (
    <section>
      <h2>Profesores</h2>
      <ul>
        {profesores.map((p) => (
          <li key={p.id}>
            {p.nombre} — {p.email}
          </li>
        ))}
      </ul>
    </section>
  );
}