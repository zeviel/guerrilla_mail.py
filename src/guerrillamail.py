from requests import get


class GuerrillaMail:
    def __init__(self, language: str = "en"):
        self.api = "https://api.guerrillamail.com/ajax.php"
        self.language = language
        self.sid_token = None
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
        }

    def get_email_address(self):
        response = get(
            f"{self.api}?f=get_email_address&lang={self.language}",
            headers=self.headers).json()
        self.sid_token = response["sid_token"]
        return response

    def set_email_user(self, email_user: str):
        response = get(
            f"{self.api}?f=set_email_user&email_user={email_user}&language={self.language}&sid_token={self.sid_token}",
            headers=self.headers,
        ).json()
        self.sid_token = response["sid_token"]
        return response

    def check_email(self, seq: int = 0):
        return get(
            f"{self.api}?f=check_email&seq={seq}&sid_token={self.sid_token}",
            headers=self.headers,
        ).json()

    def get_email_list(self, seq: int = None, offset: int = 0):
        url = f"{self.api}?f=get_email_list&offset={offset}&sid_token={self.sid_token}"
        if seq:
            url += f"&seq={seq}"
        return get(url, headers=self.headers).json()

    def fetch_email(self, email_id: int):
        return get(
            f"{self.api}?f=fetch_email&email_id={email_id}&sid_token={self.sid_token}",
            headers=self.headers,
        ).json()

    def delete_email(self, email_id: int):
        return get(
            f"{self.api}?f=del_email&email_ids[]={email_id}&sid_token={self.sid_token}",
            headers=self.headers,
        ).json()
