#!/usr/bin/env python3
"""
CLI Application for Cloud Cost & DevOps Metrics Estimator
UCS 745 Cloud & DevOps Lab
"""

import sys
from calculator import (
    calculate_compute_cost,
    calculate_storage_cost,
    calculate_network_transfer,
    calculate_sla_availability,
    estimate_monthly_cloud_bill,
    INSTANCE_PRICING,
    STORAGE_BASE_RATES,
)


def print_banner():
    banner = """
================================================================
     CLOUD COST ESTIMATOR & DEVOPS METRICS CALCULATOR
        UCS 745: Cloud & DevOps Lab - Academic Project
================================================================
"""
    print(banner)


def run_interactive():
    print_banner()
    print("1. Estimate EC2 Compute Instance Cost")
    print("2. Estimate Storage (EBS / S3) Cost")
    print("3. Estimate Network Data Transfer Egress")
    print("4. Compute SLA Availability & Downtime")
    print("5. Full Monthly Multi-Tier Bill Simulation")
    print("0. Exit")
    print("----------------------------------------------------------------")

    choice = input("Select an option (0-5): ").strip()
    if choice == "1":
        print(f"Available Instances: {list(INSTANCE_PRICING.keys())}")
        inst = input("Enter instance type (e.g. t3.medium): ").strip()
        hours = float(input("Enter hours of operation (e.g. 730 for 1 month): ") or 730)
        count = int(input("Enter instance count: ") or 1)
        cost = calculate_compute_cost(inst, hours, count)
        print(f"\n[+] Total Compute Cost for {count}x {inst} ({hours} hrs): ${cost:.2f} USD\n")

    elif choice == "2":
        print(f"Available Storage: {list(STORAGE_BASE_RATES.keys())}")
        st = input("Enter storage type (e.g. gp3): ").strip()
        gb = float(input("Enter storage size in GB: ") or 100)
        months = float(input("Enter duration in months: ") or 1)
        cost = calculate_storage_cost(st, gb, months)
        print(f"\n[+] Total Storage Cost for {gb} GB {st} ({months} months): ${cost:.2f} USD\n")

    elif choice == "3":
        gb = float(input("Enter outbound transfer in GB: ") or 500)
        cost = calculate_network_transfer(gb)
        print(f"\n[+] Billable Egress Cost: ${cost:.2f} USD (First 100 GB Free)\n")

    elif choice == "4":
        down = float(input("Enter total downtime in minutes: ") or 43.2)
        res = calculate_sla_availability(down)
        print(f"\n[+] SLA Report (30-day window):")
        print(f"    - Availability: {res['availability_percentage']}%")
        print(f"    - Meets 99.9% (Three Nines): {'YES' if res['meets_three_nines'] else 'NO'}")
        print(f"    - Meets 99.99% (Four Nines): {'YES' if res['meets_four_nines'] else 'NO'}\n")

    elif choice == "5":
        demo_compute = [{"type": "t3.medium", "count": 2}, {"type": "c5.large", "count": 1}]
        demo_storage = [{"type": "gp3", "size_gb": 200}, {"type": "s3_standard", "size_gb": 1000}]
        bill = estimate_monthly_cloud_bill(demo_compute, demo_storage, egress_gb=400)
        print("\n[+] Consolidated Monthly Infrastructure Breakdown:")
        print(f"    - Compute Total:  ${bill['compute_cost']:.2f} USD")
        print(f"    - Storage Total:  ${bill['storage_cost']:.2f} USD")
        print(f"    - Network Total:  ${bill['network_cost']:.2f} USD")
        print(f"    ------------------------------------")
        print(f"    - GRAND TOTAL:    ${bill['total_monthly_usd']:.2f} USD / month\n")
    else:
        print("Exiting...")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        print_banner()
        demo_compute = [{"type": "t3.medium", "count": 2}, {"type": "c5.large", "count": 1}]
        demo_storage = [{"type": "gp3", "size_gb": 200}, {"type": "s3_standard", "size_gb": 1000}]
        bill = estimate_monthly_cloud_bill(demo_compute, demo_storage, egress_gb=400)
        print(f"Auto-demo bill: {bill}")
    else:
        run_interactive()
