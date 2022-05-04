# guerrillamail.py
Web-API for [guerrillamail.com](https://www.guerrillamail.com) disposable temporary email address website

## Example
```python3
import guerrillamail
guerrilla_mail = guerrillamail.GuerrillaMail()
email_address = guerrilla_mail.get_email_address()["email_addr"]
print(f"-- Email address is::: {email_address}")
```
