# Reliance Jio Supply Chain Diagnostics & Revenue Leakage Analysis

### *(Simulated Project | Indian Telecom Context | Reliance Jio Inspired)*

> **“High delivery efficiency ≠ high business value realization.”**

---

## Overview

This is a **simulated end-to-end supply chain analytics project**, built using an **AI-generated dataset** to replicate real-world operations of an Indian telecom distribution network—**inspired by Reliance Jio’s ecosystem**.

The goal:

> **Identify where value is lost across the supply chain, why it happens, and how it impacts business outcomes.**

This project moves beyond reporting and delivers:

* **Descriptive analytics → What is happening**
* **Diagnostic analytics → Why it is happening**
* **Financial impact → Where revenue is lost**

---

## 🇮🇳 Context

* Market Focus: **India**
* Business Context: **Telecom device distribution (Jio-style ecosystem)**
* Dataset: **AI-generated synthetic data (500K+ records)**
* Objective: Build a **realistic, resume-grade supply chain case study**

---

## Tech Stack

* **PySpark (Databricks)** — large-scale processing
* **Pandas** — analytical transformations
* **Matplotlib / Seaborn** — visualization
* **Databricks Genie AI** — dashboard creation

---

## Analytical Framework

### 🔹 Descriptive Layer (What’s happening)

* SKU Velocity (demand concentration)
* Inventory Health
* Order Funnel (Created → Delivered → Activated)
* Shipment Performance
* Reverse Logistics

---

### 🔹 Diagnostic Layer (Why it’s happening)

* OEM Constraints
* Inventory Reconciliation Breaks
* Store Stockouts
* Split Shipments
* Carrier Exception RCA

---

### 🔹 Financial Layer (Business Impact)

* Activation Failure → Return Loop
* Revenue Leakage Attribution

---

## Key Findings

### 1. Strong Operations — Weak Conversion

* **Delivery Rate:** ~95%
* **End-to-End Conversion:** ~87%

> The system is operationally efficient up to delivery, but struggles to convert delivery into actual product usage 

---

### 2. Critical Failure Point = Post-Delivery

Major drop-offs occur at:

* Delivery → Activation
* Activation → Return

---

### 3. Activation Failure = Guaranteed Loss 

* **100% Failure → Return conversion**
* Drives **46.6% of total revenue leakage**

> No recovery mechanism exists between activation failure and return, creating a direct loss pipeline 

---

### 4. Revenue Leakage Drivers

| Driver             | Contribution |
| ------------------ | ------------ |
| Activation Failure | **46.6%**    |
| Carrier Damage     | 30.5%        |
| Carrier Loss       | 22.9%        |

> Leakage is driven more by **system-level failures than logistics inefficiency** 

---

### 5. Reverse Logistics = Value Destruction

* ~33% scrap rate
* Loss concentrated in high-value devices

---

### 6. Systemic (Not Localized) Issues

* Failures consistent across:

  * Brands
  * Regions
  * Carriers

> Indicates **process design gaps**, not isolated execution issues 

---

### 7. Inventory & Planning Instability

* Reactive cycle-count adjustments
* Region-specific stockouts
* Heavy dependence on emergency transfers

---

## Core Insight

> **The supply chain is optimized for delivery speed, not value realization.**

* Products are delivered efficiently
* But fail during activation
* Leading to:

  * Returns
  * Scrap
  * Revenue leakage

---

## Dashboard

A fully interactive dashboard was built using **Databricks Genie AI**, covering all use cases:

### Features:

* End-to-end supply chain visibility
* Scenario-level breakdowns
* Pareto analysis
* Root cause attribution
* Brand & region interaction views

---

## Geo Layer (India Mapping)

* Warehouse-level mapping using Indian cities
* Enables:

  * Regional hotspot detection
  * Supply-demand imbalance analysis

---

## Limitations

* Synthetic dataset (AI-generated)
* No real pricing → revenue approximated via counts
* Event linkage handled via modeling (not raw tracking)

---

## Future Improvements

* Add **₹-level revenue estimation**
* Integrate **real-world datasets**
* Build **predictive models (failure / stockout / leakage)**
* Deploy as **real-time monitoring system**

---

## Why This Project Matters

This project demonstrates:

* Transition from **analytics → business impact**
* Ability to diagnose **system-level failures**
* Understanding of **end-to-end supply chain dynamics**

---

###  Note

This is a **simulation-based project inspired by real-world supply chain systems** (e.g., Reliance Jio) and is intended for learning, portfolio, and interview demonstration purposes.

---
