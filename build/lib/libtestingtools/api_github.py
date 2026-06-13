import requests
# pip install requests


def search_avatar(user: str, timeout: float = 10) -> str:
    """
    Search a user's avatar from Github.

    Param: Github user name (str)
    Param: request timeout in seconds (float)
    Return: Github avatar link (str)
    Raises: RuntimeError if the HTTP request fails (network error,
        timeout, or non-2xx response).
    """
    url = f"https://api.github.com/users/{user}"
    try:
        ans = requests.get(url, timeout=timeout)
        ans.raise_for_status()
    except requests.RequestException as exc:
        raise RuntimeError(f"Failed to fetch avatar for user {user!r}: {exc}") from exc
    return ans.json()['avatar_url']
