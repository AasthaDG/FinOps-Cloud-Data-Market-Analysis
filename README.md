# 💰 FinOps Cost Intelligence Dashboard (StubHub-style Simulation)

A lightweight FinOps analytics dashboard that simulates cloud cost visibility, allocation, and optimization insights for a large-scale marketplace platform like StubHub.

---

## 📌 Overview

Modern marketplace platforms experience highly variable cloud costs driven by user demand, event-based traffic spikes, and multi-service architectures.

This project simulates a **FinOps observability layer** that helps engineering and finance teams:

- Track cloud spending across services and teams
- Identify cost drivers and inefficiencies
- Understand cost trends over time
- Simulate event-driven cost spikes
- Improve cost accountability and visibility

---

## 🧠 Problem Statement

In large-scale platforms like ticket marketplaces:

- Cloud costs are distributed across multiple services (compute, storage, serverless)
- Spend varies heavily based on demand events (concerts, sports events, etc.)
- Lack of visibility leads to delayed cost optimization
- Teams often lack ownership of infrastructure spend

This project demonstrates how FinOps practices can solve these challenges.

---

## ⚙️ Features

### 📊 Cost Visibility
- Total cost overview
- Average cost metrics
- Top cost-driving services

### 📈 Trend Analysis
- Daily cloud cost trends
- Spike detection visualization

### ⚙️ Service-Level Breakdown
- Cost distribution across EC2, Lambda, S3, VM, Blob Storage, etc.

### 👥 Team-Level Allocation
- Cost breakdown by engineering, data, and platform teams

### ☁️ Multi-Cloud Simulation
- AWS vs Azure cost comparison

### 🚨 Event-Driven Cost Simulation
- Simulated demand spikes to reflect real-world marketplace traffic surges

---

## 🧰 Tech Stack

- Python
- Streamlit
- Pandas
- Plotly

---

## 📁 Project Structure
