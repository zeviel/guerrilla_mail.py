# guerrilla_mail.py
Web-API for [guerrillamail.com](https://www.guerrillamail.com) disposable temporary email address website

## Example
```python3
import guerrilla_mail
guerrilla_mail = guerrilla_mail.GuerrillaMail()
email_address = guerrilla_mail.get_email_address()["email_addr"]
print(email_address)
```
