# Demand Forecasting Application

## Executive Summary

This project delivers a **production-ready demand forecasting solution** designed to support **data‑driven commercial and operational decision‑making**.  
The application enables business users to estimate product demand by simulating real‑world scenarios such as pricing changes, promotions, inventory levels, and competitive positioning.

The solution follows an **end‑to‑end analytics lifecycle**:
- Model development and validation in **Kaggle**
- Operationalization via a **web‑based decision interface**
- Deployment on **Hugging Face Spaces** for scalable access

🔗 **Live Business Demo**  
https://dannymoreira-demand-forecasting.hf.space/
---

## Business Objective

The primary objective of this application is to **improve forecast accuracy and decision quality** in areas such as:

- Inventory planning  
- Promotion effectiveness analysis  
- Pricing strategy evaluation  
- Commercial scenario simulation  

By allowing stakeholders to test “what‑if” scenarios interactively, the tool reduces reliance on static reports and enables **faster, more informed decisions**.

---

## Solution Overview

The application exposes a demand prediction model through an intuitive web interface that abstracts technical complexity while preserving analytical rigor.

### Key Characteristics
- Scenario‑based demand estimation
- Real‑time model inference
- No manual data manipulation required
- Designed for non‑technical business users

---

## Analytical Model

- **Model Type**: Gradient Boosting (XGBoost Regressor)
- **Task**: Demand forecasting (regression)
- **Training Environment**: Kaggle
- **Deployment Mode**: Inference‑only (production‑safe)

### Feature Engineering
- Numerical variables used directly
- Categorical variables encoded with persistent label encoders
- Consistent preprocessing between training and inference

---

## Input Variables

| Variable | Business Meaning |
|--------|------------------|
| Price | Product selling price |
| Discount (%) | Promotional discount |
| Inventory Level | Available stock |
| Promotion | Promotion active indicator |
| Competitor Pricing | Market competitive reference |
| Category | Product category |

---

## Business Value Delivered

- **Reduced forecasting latency**: instant predictions vs manual analysis  
- **Improved alignment** between pricing, promotions, and inventory decisions  
- **Scenario evaluation** without re‑running analytical pipelines  
- **Reusable analytics asset** deployable across teams  

---

## Technology Stack

- **Python**
- **XGBoost**
- **Scikit‑learn**
- **Pandas / NumPy**
- **Gradio** (UI & interaction layer)
- **Hugging Face Spaces** (deployment)
- **Kaggle** (model experimentation and training)

---

## Repository Structure

```text
.
demand-forecasting-app/
│
├── app/                    # Código productivo (deploy)
│   ├── app.py              # Gradio app
│   ├── model.pkl           # Modelo entrenado
│   └── label_encoders.pkl  # Encoders
│
├── notebooks/              # Experimentación (Kaggle / análisis)
│   ├── demand-forecasting.ipynb
│
├── requirements.txt        # Dependencias
├── README.md               # Documentación de negocio


