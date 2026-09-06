const BASE_URL = "http://localhost:8000";

export async function getEstudiantes() {
  const res = await fetch(`${BASE_URL}/estudiantes/`);
  if (!res.ok) throw new Error("Error al obtener estudiantes");
  return res.json();
}

export async function getProfesores() {
  const res = await fetch(`${BASE_URL}/profesores/`);
  if (!res.ok) throw new Error("Error al obtener profesores");
  return res.json();
}

export async function getCursos() {
  const res = await fetch(`${BASE_URL}/cursos/`);
  if (!res.ok) throw new Error("Error al obtener cursos");
  return res.json();
}