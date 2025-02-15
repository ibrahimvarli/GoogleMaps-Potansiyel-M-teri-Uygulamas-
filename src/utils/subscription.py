from enum import Enum
from dataclasses import dataclass
from typing import List

class PlanType(Enum):
    FREE = "free"
    PRO = "pro"

@dataclass
class PlanFeatures:
    max_businesses: int
    max_customers: int
    export_data: bool
    advanced_analytics: bool
    api_access: bool
    custom_reports: bool
    email_support: bool
    priority_support: bool

class SubscriptionPlans:
    @staticmethod
    def get_plan_features(plan_type: PlanType) -> PlanFeatures:
        if plan_type == PlanType.FREE:
            return PlanFeatures(
                max_businesses=50,
                max_customers=100,
                export_data=False,
                advanced_analytics=False,
                api_access=False,
                custom_reports=False,
                email_support=True,
                priority_support=False
            )
        elif plan_type == PlanType.PRO:
            return PlanFeatures(
                max_businesses=float('inf'),
                max_customers=float('inf'),
                export_data=True,
                advanced_analytics=True,
                api_access=True,
                custom_reports=True,
                email_support=True,
                priority_support=True
            )

    @staticmethod
    def get_plan_price(plan_type: PlanType) -> float:
        prices = {
            PlanType.FREE: 0,
            PlanType.PRO: 299.99
        }
        return prices.get(plan_type, 0) 