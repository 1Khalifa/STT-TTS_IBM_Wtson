# IBM Watson Speech to Text & Text to Speech

To begin with IBM’s API, you first need to have an IBM Cloud account. Once you have created your account, follow the following steps.

1. from the top left navigation menu on the dashboard, go to Resources list.
2. then, click on Create Resource.
3. then, in the categories section, select AI and select Speech to Text. Create your service without changing anything.
4. after your service is created, click on the service.
5. select manage from the navigation menu and click on show credentials.
6. copy the api key and url generated.
7. do the same steps to create Text to Speech service.

## Installing

Run the following commands in the terminal.


```
pip install --upgrade "ibm-watson>=5.2.2"
```
```
pip install SpeechRecognition
```
Place your IBM Watson Service credentials in `main.py`
```python
# Text to Speech service credentials
stt_api = 'YOUR_API_KEY'
stt_url = 'YOUR_URL'

# Speech to Text service credentials
tts_api = 'YOUR_API_KEY'
tts_url = 'YOUR_URL'
```
