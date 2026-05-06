RULES = {
    "Food & Dining": [
        "trader joe", "whole foods", "costco", "dining hall", "chipotle",
        "mcdonald", "starbucks", "taco bell", "five guys", "domino",
        "uber eats", "pizza", "burger", "lunch", "dinner", "grocery",
        "coffee", "restaurant", "cafe",
    ],
    "Housing": [
        "rent", "mortgage", "lease",
    ],
    "Utilities": [
        "electric", "gas bill", "water bill", "internet", "phone bill",
        "utility", "utilities",
    ],
    "Subscriptions": [
        "spotify", "netflix", "hulu", "youtube premium", "amazon prime",
        "icloud", "chegg", "audible", "zoom", "disney+", "apple tv",
        "subscription", "membership",
    ],
    "Transportation": [
        "uber", "lyft", "shell", "gas station", "bus", "metro", "transit",
        "parking", "toll",
    ],
    "Health & Fitness": [
        "planet fitness", "gym", "cvs", "walgreens", "pharmacy",
        "prescription", "vitamin", "doctor", "medical", "health",
    ],
    "Education": [
        "textbook", "barnes", "chegg", "coursera", "udemy", "tuition",
        "school", "notebook", "book", "course",
    ],
    "Shopping": [
        "target", "amazon", "dollar tree", "walmart", "best buy",
        "clothing", "household",
    ],
    "Income": [
        "paycheck", "salary", "income", "tutoring", "freelance", "deposit",
    ],
}

_PRIORITY = list(RULES.keys())


def categorize(description: str) -> str:
    desc_lower = description.lower()
    for category in _PRIORITY:
        for keyword in RULES[category]:
            if keyword in desc_lower:
                return category
    return "Other"
