"""
Cost and billing calculation for GitHopper analysis.
Tracks API usage and estimates costs.
"""

import json
from datetime import datetime, timedelta

# AWS Bedrock Claude 3 Haiku pricing (per 1M tokens)
# Input: $0.80, Output: $4.00
BEDROCK_PRICING = {
    "input_per_1m": 0.80,      # $0.80 per 1M input tokens
    "output_per_1m": 4.00,     # $4.00 per 1M output tokens
    "average_input_tokens": 8000,   # ~8K avg input tokens per request
    "average_output_tokens": 2000,  # ~2K avg output tokens per request
}

# Free tier limits
FREE_TIER_MONTHLY = {
    "bedrock_requests": 1000,      # 1000 free API calls/month
    "bedrock_input_tokens": 10_000_000,  # 10M free input tokens
}

class BillingTracker:
    """Track and calculate billing for GitHopper analysis."""
    
    def __init__(self):
        self.reset()
    
    def reset(self):
        """Reset billing tracker for new analysis."""
        self.bedrock_calls = 0
        self.input_tokens_used = 0
        self.output_tokens_used = 0
        self.start_time = datetime.now()
    
    def add_bedrock_call(self, input_tokens=None, output_tokens=None):
        """Record a Bedrock API call."""
        self.bedrock_calls += 1
        # Use average estimates if not provided
        self.input_tokens_used += input_tokens or BEDROCK_PRICING["average_input_tokens"]
        self.output_tokens_used += output_tokens or BEDROCK_PRICING["average_output_tokens"]
    
    def calculate_cost(self) -> dict:
        """Calculate total cost based on usage."""
        # Cost calculation
        input_cost = (self.input_tokens_used / 1_000_000) * BEDROCK_PRICING["input_per_1m"]
        output_cost = (self.output_tokens_used / 1_000_000) * BEDROCK_PRICING["output_per_1m"]
        total_cost = input_cost + output_cost
        
        # Free tier calculation
        free_calls_remaining = max(0, FREE_TIER_MONTHLY["bedrock_requests"] - self.bedrock_calls)
        in_free_tier = self.bedrock_calls <= FREE_TIER_MONTHLY["bedrock_requests"]
        
        return {
            "bedrock_calls": self.bedrock_calls,
            "input_tokens": self.input_tokens_used,
            "output_tokens": self.output_tokens_used,
            "input_cost": round(input_cost, 4),
            "output_cost": round(output_cost, 4),
            "total_cost": round(total_cost, 4),
            "free_tier": {
                "monthly_limit": FREE_TIER_MONTHLY["bedrock_requests"],
                "calls_used": self.bedrock_calls,
                "calls_remaining": free_calls_remaining,
                "in_free_tier": in_free_tier,
            },
            "analysis_duration_seconds": (datetime.now() - self.start_time).total_seconds(),
        }
    
    def get_billing_summary(self) -> dict:
        """Get human-readable billing summary."""
        cost = self.calculate_cost()
        
        # Determine billing status
        will_be_charged = not cost["free_tier"]["in_free_tier"]
        
        return {
            "calls_made": cost["bedrock_calls"],
            "estimated_cost": cost["total_cost"],
            "free_calls_remaining": cost["free_tier"]["calls_remaining"],
            "will_be_charged": will_be_charged,
            "cost_breakdown": {
                "input": cost["input_cost"],
                "output": cost["output_cost"],
            },
            "alternatives": [
                {
                    "name": "AWS Free Tier",
                    "cost": f"{cost['free_tier']['calls_remaining']} API calls remaining",
                    "url": "https://aws.amazon.com/bedrock/pricing/"
                },
                {
                    "name": "Self-Hosted LLM",
                    "cost": "One-time setup cost",
                    "url": "https://ollama.ai/"
                }
            ] if will_be_charged else [],
        }

# Global tracker instance
_tracker = BillingTracker()

def reset_billing():
    """Reset billing tracker (call at start of analysis)."""
    global _tracker
    _tracker.reset()

def track_bedrock_call(input_tokens=None, output_tokens=None):
    """Track a Bedrock API call."""
    global _tracker
    _tracker.add_bedrock_call(input_tokens, output_tokens)

def get_billing_summary() -> dict:
    """Get current billing summary."""
    global _tracker
    return _tracker.get_billing_summary()

def get_cost_tracker() -> dict:
    """Get detailed cost tracking info (for health_score page)."""
    global _tracker
    return _tracker.calculate_cost()
