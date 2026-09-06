import { useEffect, useState } from "react";
import { getCursos } from "../api";
import type { Curso } from "../types";

export function Cursos() {
  const [cursos, setCursos] = useState<Curso[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    getCursos()
      .then(setCursos)
      .catch((err) => setError(err.message));
  }, []);

  if (error) return <p>Error: {error}</p>;

  return (
    <section>
      <h2>Cursos</h2>
      <ul>
        {cursos.map((c) => (
          <li key={c.id}>
            {c.titulo} ({c.creditos} créditos)
          </li>
        ))}
      </ul>
    </section>
  );
}