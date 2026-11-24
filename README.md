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

## 3. Storage Pricing Specification
Storage cost calculation logic:
Standard base rates apply across all storage tiers with flat linear pricing per GB/month.
No automated volume discounts or regional adjustments are applied in the baseline version.

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
