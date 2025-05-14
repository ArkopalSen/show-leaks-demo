def demo_func(param: str):
    api_key = "Ojh8qbasd8oih12uhsdnou23_sdah2cc12"
    url = f"https://notarealurl/api/v1/access/{param}"
    headers = {
        "X-API-Key": api_key,
        "accept": "application/json"
    }
    response = requests.get(url, headers=headers)
    return response.json()
