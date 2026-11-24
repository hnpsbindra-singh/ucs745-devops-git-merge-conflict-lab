"""
Cloud Resource Cost Estimator & Metrics Analyzer
UCS 745 Cloud and DevOps Lab Project
Author: Harnimarpreet Singh (hnpsbindra-singh)
"""

# Base pricing per hour in USD (Standard US-East-1 AWS / GCP equivalent)
INSTANCE_PRICING = {
    "t3.nano": 0.0052,
    "t3.micro": 0.0104,
    "t3.small": 0.0208,
    "t3.medium": 0.0416,
    "m5.large": 0.0960,
    "m5.xlarge": 0.1920,
    "c5.large": 0.0850,
    "c5.xlarge": 0.1700,
}

STORAGE_BASE_RATES = {
    "gp3": 0.08,       # USD per GB/month
    "gp2": 0.10,       # USD per GB/month
    "io2": 0.125,      # USD per GB/month
    "s3_standard": 0.023, # USD per GB/month
    "s3_infrequent": 0.0125, # USD per GB/month
    "s3_glacier": 0.004,     # USD per GB/month
}


def calculate_compute_cost(instance_type: str, hours: float, count: int = 1) -> float:
    """Calculate compute instance cost based on instance type and running hours."""
    rate = INSTANCE_PRICING.get(instance_type)
    if rate is None:
        raise ValueError(f"Unknown instance type '{instance_type}'. Available: {list(INSTANCE_PRICING.keys())}")
    return round(rate * hours * count, 4)


def calculate_storage_cost(volume_type: str, size_gb: float, duration_months: float = 1.0, region: str = "us-east-1") -> float:
    """
    Calculate monthly storage cost with regional cost multipliers:
    - us-east-1 (N. Virginia): 1.0x (Baseline)
    - ap-south-1 (Mumbai): 1.15x
    - eu-central-1 (Frankfurt): 1.20x
    """
    rate = STORAGE_BASE_RATES.get(volume_type)
    if rate is None:
        raise ValueError(f"Unknown volume type '{volume_type}'. Available: {list(STORAGE_BASE_RATES.keys())}")

    region_multipliers = {
        "us-east-1": 1.00,
        "ap-south-1": 1.15,
        "eu-central-1": 1.20,
    }
    multiplier = region_multipliers.get(region, 1.00)

    total_cost = (rate * size_gb * multiplier) * duration_months
    return round(total_cost, 4)


def calculate_network_transfer(data_gb: float, free_tier_gb: float = 100.0) -> float:
    """Calculate outbound internet data transfer cost."""
    billable_gb = max(0.0, data_gb - free_tier_gb)
    rate_per_gb = 0.09  # USD per GB
    return round(billable_gb * rate_per_gb, 4)


def calculate_sla_availability(downtime_minutes: float, period_days: int = 30) -> dict:
    """Calculate uptime percentage and SLA breach status for cloud workloads."""
    total_minutes = period_days * 24 * 60
    uptime_minutes = max(0.0, total_minutes - downtime_minutes)
    availability_pct = (uptime_minutes / total_minutes) * 100.0
    return {
        "period_days": period_days,
        "total_minutes": total_minutes,
        "downtime_minutes": downtime_minutes,
        "availability_percentage": round(availability_pct, 4),
        "meets_three_nines": availability_pct >= 99.9,
        "meets_four_nines": availability_pct >= 99.99,
    }


def estimate_monthly_cloud_bill(compute_configs: list, storage_configs: list, egress_gb: float = 250.0) -> dict:
    """Generate consolidated monthly infrastructure expenditure estimate."""
    total_compute = sum(calculate_compute_cost(c["type"], 730, c.get("count", 1)) for c in compute_configs)
    total_storage = sum(calculate_storage_cost(s["type"], s["size_gb"], 1.0) for s in storage_configs)
    total_network = calculate_network_transfer(egress_gb)
    grand_total = total_compute + total_storage + total_network

    return {
        "compute_cost": round(total_compute, 2),
        "storage_cost": round(total_storage, 2),
        "network_cost": round(total_network, 2),
        "total_monthly_usd": round(grand_total, 2),
    }
