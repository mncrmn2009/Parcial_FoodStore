# 📋 Proyecto Integrador - Full Stack Application

Una aplicación web completa que demuestra la integración entre un **backend robusto** con **FastAPI** y un **frontend moderno** con **React**.

---

## 🎯 Descripción del Proyecto

Este proyecto integrador es una aplicación full-stack que implementa una arquitectura profesional con separación clara entre capas de presentación y lógica de negocio. 

**Características principales:**
- ✅ Backend RESTful con validación de datos
- ✅ Base de datos PostgreSQL con relaciones complejas
- ✅ Frontend interactivo con TypeScript y Tailwind CSS
- ✅ Integración seamless entre cliente y servidor
- ✅ Gestión de estado y sincronización automática
- ✅ Interfaz responsiva y profesional

---

## 🏗️ Arquitectura

### Backend (FastAPI + SQLModel)
- **Framework:** FastAPI
- **Base de Datos:** PostgreSQL
- **ORM:** SQLModel
- **Validación:** Pydantic con Annotated, Query y Path
- **Seguridad:** Response models para filtrado de datos
- **Estructura:** Modular (routers, schemas, services, models, UoW)

### Frontend (React + TypeScript + Tailwind)
- **Framework:** React 18
- **Lenguaje:** TypeScript
- **Build Tool:** Vite
- **Estilos:** Tailwind CSS 4
- **State Management:** React Query (useQuery, useMutation)
- **Routing:** React Router v6 con rutas dinámicas

---

## 📹 Video de Demostración

**https://www.youtube.com/watch?v=hnfp_IkaUE0**

<div align="center">

[![Ver video demo](https://img.youtube.com/vi/hnfp_IkaUE0/maxresdefault.jpg)](https://www.youtube.com/embed/hnfp_IkaUE0)

**[Ver video en YouTube](https://www.youtube.com/watch?v=hnfp_IkaUE0)**

</div>

> 📌 **Nota:** Reemplaza `VIDEO_ID` con el ID de tu video de YouTube
>
> Para obtener el ID: Si tu URL es `https://www.youtube.com/watch?v=aBcDeFgHiJk`, el ID es `aBcDeFgHiJk`

---

## 🚀 Inicio Rápido

### Requisitos
- Python 3.10+
- Node.js 18+
- PostgreSQL

### Instalación Backend

```bash
cd BackEnd
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

#### Ejecutar servidor de desarrollo
```bash
python -m fastapi dev main.py
```

El servidor estará disponible en: `http://localhost:8000`

### Instalación Frontend

```bash
cd frontEnd
pnpm install
pnpm run dev
```

El frontend estará disponible en: `http://localhost:5173`

---

## 📁 Estructura de Carpetas

```
.
├── BackEnd/
│   ├── models/          # Modelos SQLModel
│   ├── routers/         # Endpoints API
│   ├── schemas/         # Esquemas Pydantic
│   ├── services/        # Lógica de negocio
│   ├── main.py          # Punto de entrada FastAPI
│   └── requirements.txt
│
├── frontEnd/
│   ├── src/
│   │   ├── components/  # Componentes React
│   │   ├── pages/       # Páginas
│   │   ├── hooks/       # Custom hooks
│   │   ├── App.tsx      # App principal
│   │   └── main.tsx     # Entrada
│   ├── package.json
│   └── vite.config.ts
│
└── README.md            # Este archivo
```

---

## 🔌 API Endpoints

Accede a la documentación interactiva en: `http://localhost:8000/docs`

**Ejemplos principales:**
- `GET /api/items` - Listar elementos
- `POST /api/items` - Crear elemento
- `GET /api/items/{id}` - Obtener detalle
- `PUT /api/items/{id}` - Actualizar
- `DELETE /api/items/{id}` - Eliminar

---

## 🛠️ Tecnologías Utilizadas

| Capa | Tecnología |
|------|-----------|
| Backend | FastAPI, SQLModel, Pydantic |
| Database | PostgreSQL |
| Frontend | React, TypeScript, Vite |
| Styling | Tailwind CSS 4 |
| State | React Query |
| Routing | React Router v6 |

---

