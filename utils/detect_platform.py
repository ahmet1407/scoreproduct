def detect_platform(link):
    if "amazon" in link:
        return "amazon"
    elif "hepsiburada" in link:
        return "hepsiburada"
    elif "trendyol" in link:
        return "trendyol"
    else:
        return "unknown"
