import requests
from requests.exceptions import RequestException, HTTPError, ConnectionError, Timeout


def search_avatar(user: str, timeout: int = 10) -> str:
    """
    Search a user's avatar from Github.
    Param: Github user name (str)
    Param: timeout - request timeout in seconds (default 10)
    Return: Github avatar link (str)
    Raises: RequestException on network errors
    """
    url = f"https://api.github.com/users/{user}"
    try:
        ans = requests.get(url, timeout=timeout)
        ans.raise_for_status()
        return ans.json()['avatar_url']
    except HTTPError as e:
        raise HTTPError(f"GitHub API returned error for user '{user}': {e}") from e
    except ConnectionError as e:
        raise ConnectionError(f"Failed to connect to GitHub API: {e}") from e
    except Timeout as e:
        raise Timeout(f"Request to GitHub API timed out after {timeout}s: {e}") from e
    except RequestException as e:
        raise RequestException(f"Request to GitHub API failed: {e}") from e
