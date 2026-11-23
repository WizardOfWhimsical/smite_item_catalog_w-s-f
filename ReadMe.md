# Smite 2 Item Catalog

A learning project for cataloging **Smite 2** items and building custom searches
over item properties.

## Contents

- [Project overview](#project-overview)
- [Goals](#goals)
- [Planned technology](#planned-technology)
- [Data storage](#data-storage)
- [Current status](#current-status)
- [Frontend development](#frontend-development)
- [Project structure](#project-structure)

## Project overview

The application will provide a catalog of Smite 2 items. Users will be able to
create, view, update, and delete catalog entries, then search the catalog using
item parameters they choose.

This is a practice project for applying college coursework, including frontend
development, backend operations, and working with structured data.

## Goals

- Keep a structured catalog of Smite 2 items.
- Support CRUD operations (create, read, update, and delete) for catalog entries.
- Let users build searches around item parameters they choose.
- Practice connecting a React frontend to a Python backend.

## Planned technology

- **Frontend:** React, with Vite for development and builds.
- **Backend:** Python, providing the application's CRUD operations.
- **Catalog storage:** A JSON file initially; a database may replace it later.

## Data storage

The initial catalog will be stored as JSON rather than in a local database. This
keeps the first version simple while the application and its CRUD workflow are
being developed. The storage approach is temporary and can be replaced with a
database in a later version.

## Current status

The frontend is scaffolded with React and Vite. The Python script in `BackEnd/`
is currently a small JSON experiment; a complete backend API and its connection
to the frontend are still to be implemented.

## Frontend development

From the `frontend/` directory, install the dependencies and start the Vite
development server:

```bash
npm install
npm run dev
```

Other available frontend commands:

```bash
npm run build
npm run lint
```

## Project structure

```text
BackEnd/      Python backend prototype
frontend/     React and Vite frontend
ReadMe.md     Project documentation
```