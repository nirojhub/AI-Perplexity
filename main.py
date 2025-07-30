import requests
import json

myAPIKey = ''
url = "https://api.perplexity.ai/chat/completions"
headers = {
    "Authorization": f"Bearer {myAPIKey}",
    "Content-Type": "application/json"
}

data = {
    "model": "sonar",
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful assistant that provides interesting, accurate, and concise facts. Respond within 100 words."
        },
        {
            "role": "user",
            "content": "Tell me an interesting and unexpected fact about {topic} that most people don't know."
        }
    ],
    "max_tokens": 200,
    "temperature": 1
}
response = requests.post(url, headers=headers, json=data)
response.raise_for_status()  # Raise an error for HTTP error responses
result = response.json() 
print(result["choices"][0]["message"]["content"], result["citations"])


#from perplexipy import PERPLEXITY_API_PREFIX

#myAPIKey = PERPLEXITY_API_PREFIX+'3a45' # bogus value
#Now let's try to instantiate the client:

'''from perplexipy import PerplexityClient

client = PerplexityClient(key = myAPIKey)
try:
    client.query('This query will fail and throw an exception')
except Exception as e:
    print('Oh, no!  %s' % str(e))'''

#Simple query
#Set your actual API key here, then run the code:

#
# *** Assign your real API key here!
#
'''myAPIKey = ''
client = PerplexityClient(key = myAPIKey)
try:
    result = client.query('Provide a brief answer to:  what is a query?')
except Exception as e:
    print('Oh, no!  %s' % str(e))

display(result)'''

#Streaming API
#Let's run a long query and emulate the "natural flow of conversation" that the streaming API provides:

'''results = client.queryStreamable('Show me a comprehensive list of Jedi Knights including their planet of origin.')

output = ''
for result in results:
    output += result
    if '\n' in result:
        display('%s' % output)
        output = ''
'''
#Changing the which model to use
#Not all models will result in the same output; each has different training and audience focus. Let's find out what the current model was used for the previous, then change it to a different model and run the query again.

'''import pandas as pd
from IPython.display import Markdown

display(pd.DataFrame(client.models))'''

#Models only:

'''for model in client.models.keys():
    display(Markdown('- %s' % model))

display(Markdown('And the active model is: %s' % client.model))
client.model = 'sonar-small-chat'
results = client.queryStreamable('Show me a comprehensive list of Jedi Knights including their planet of origin.')

output = ''
for result in results:
    output += result
    if '\n' in result:
        display('%s' % output)
        output = ''
'''
#The last query may work better in a batch reply:

'''results = client.query('Show me a comprehensive list of Jedi Knights including their planet of origin.')

output = ''
for result in results:
    output += result
    if '\n' in result:
        display('%s' % output)
        output = ''
'''