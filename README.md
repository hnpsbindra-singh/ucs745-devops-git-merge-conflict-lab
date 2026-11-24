# Cloud Cost Estimator & DevOps Metrics Calculator

**Course:** UCS 745 Cloud and DevOps  
**Student Name:** Harnimarpreet Singh  
**Repository:** [https://github.com/hnpsbindra-singh/ucs745-devops-git-merge-conflict-lab](https://github.com/hnpsbindra-singh/ucs745-devops-git-merge-conflict-lab)  

---

## 1. Project Overview
This project provides a lightweight, modular CLI utility to calculate and simulate multi-tier cloud infrastructure costs across compute instances (EC2), storage volumes (EBS/S3), network egress bandwidth, and service availability (SLA uptime).

Developed as part of the **UCS 745 Cloud and DevOps Lab Assignment**, this repository serves as a live demonstration of professional Git version control workflows, including repository initialization, branching strategies, intentional merge conflicts, manual conflict resolution, and remote synchronization.

---

## 2. System Architecture & Features
- **Compute Sizing**: Hourly and monthly billing estimations for multiple instance tiers.
- **Storage Tier Calculation**: Standard rates across EBS `gp3`, `gp2`, `io2`, and S3 storage tiers.
- **Data Transfer Analytics**: Outbound bandwidth pricing with automated 100 GB free-tier allowance.
- **SLA Uptime Tracker**: Real-time evaluation of outage minutes against 99.9% (Three Nines) and 99.99% (Four Nines) compliance.

---

## 3. Storage Pricing Specification (Resolved & Merged)
Storage cost calculation logic incorporates both feature additions:
1. **Enterprise Volume Discount Tiers** (from `feature/volume-discount`):
   - Tier 1 (0 – 499 GB): 1.00x baseline rate (0% discount).
   - Tier 2 (500 – 1999 GB): 0.90x rate (10% volume discount).
   - Tier 3 (2000+ GB): 0.80x rate (20% enterprise bulk discount).
2. **Multi-Region Cost Adjustment** (from `feature/regional-pricing`):
   - `us-east-1` (N. Virginia): 1.00x base reference rate.
   - `ap-south-1` (Mumbai): 1.15x regional infrastructure surcharge (+15%).
   - `eu-central-1` (Frankfurt): 1.20x power and compliance surcharge (+20%).

**Consolidated Pricing Formula:**
$$\text{Storage Cost} = \text{Base Rate} \times \text{Size (GB)} \times \text{Discount Factor} \times \text{Regional Multiplier} \times \text{Months}$$

---

## 4. Execution Instructions
Run the interactive CLI application:
```bash
python3 app.py
```

Run automated demonstration mode:
```bash
python3 app.py --demo
```
