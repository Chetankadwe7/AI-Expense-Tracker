def budget_alert(total, budget=50000):
    if total > budget:
        return "⚠️ Budget Exceeded"
    return "✅ Budget Safe"