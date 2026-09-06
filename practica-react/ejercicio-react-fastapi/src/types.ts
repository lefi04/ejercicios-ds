export interface Profesor {
  id: number;
  nombre: string;
  email: string;
  fecha_ingreso: string;
}

export interface Curso {
  id: number;
  titulo: string;
  creditos: number;
  profesor_id: number;
}

export interface Estudiante {
  id: number;
  nombre: string;
  legajo: number;
  inscripciones: unknown[]; // si después necesitás el detalle, lo tipamos bien
}