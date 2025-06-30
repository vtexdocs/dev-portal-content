import os
import requests

comment_body = os.getenv('COMMENT_BODY')
user = os.getenv('USER')
comment_url = os.getenv('COMMENT_URL')
pr_number = os.getenv('PR_NUMBER')

if "<h2 id=\"ai-feedback\">Was this feedback useful?</h2>" in comment_body:
    if "- [x] Yes" in comment_body:
        response = "Yes"
    elif "- [x] No" in comment_body:
        response = "No"
    else:
        response = "No valid answer."
    
    print(f"URL: {comment_url}, User: {user}, Response: {response}")
    
    data = {
        'comment_url': comment_url,
        'user': user,
        'response': response,
        'pr_number': pr_number
    }
    
    zapier_webhook_url = 'https://hooks.zapier.com/hooks/catch/10752880/2pfxxhk/'
    response = requests.post(zapier_webhook_url, json=data)

    if response.status_code == 200:
      print("Data successfully sent to Zapier.")
    else:
        print(f"Failed to send data to Zapier. Status code: {response.status_code}, Response: {response.text}")
  
else:
    print("Comment does not contain the expected feedback")
    exit(1)
