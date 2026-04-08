def grade(query, response):
    query = query.lower()
    response = response.lower()
    if "order" in query and "track" in response:
        return 1.0
    elif "return" in query and "refund" in response:
        return 1.0
    elif "charged" in query and ("refund" in response or "apology" in response):
        return 1.0
    return 0.0
