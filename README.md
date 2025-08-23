# 🌐 E-Gov Accreditation Suite

A streamlined, web-based system to **collect, validate, deduplicate, search, and report** accreditation data (NAAC/NBA/NIRF/QS) across stakeholders (Admin, IQAC/NBA coordinators, HODs, Faculty). Includes **evidence uploads** and a **built-in chatbot**.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95+-teal)
![SQLite](https://img.shields.io/badge/SQLite-DB-blue)
![Frontend](https://img.shields.io/badge/Frontend-HTML%2FCSS%2FJS-orange)

---

## 🚀 Features
- Modular dashboards (Admin, Faculty, IQAC/NBA, HOD)
- Upload evidences (PDFs/images) with duplication prevention (SHA-256)
- Faculty/Dept forms (teaching-learning, research, infrastructure)
- Validation & de-duplication
- Import/Export CSV/JSON
- Dynamic search & filters
- Criteria-based PDF/CSV/JSON reports
- Scalable across departments (SQLite by default; switch DB with `DATABASE_URL`)
- Lightweight chatbot with accreditation FAQs

---

## 📂 Project Structure
