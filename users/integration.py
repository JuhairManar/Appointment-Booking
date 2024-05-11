# calendar_integration/integration.py

import os
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
credentials_file_path = os.path.join(BASE_DIR, 'credentials', 'credentials.json')

def authorize_access():
    flow = InstalledAppFlow.from_client_secrets_file(
        credentials_file_path, scopes=['https://www.googleapis.com/auth/calendar'])

    creds = flow.run_local_server(port=0)

    return creds

def get_user_credentials(user):
    user_credentials_path = os.path.join(BASE_DIR, 'credentials', f'{user.username}_credentials.json')
    
    if os.path.exists(user_credentials_path):
        creds = Credentials.from_authorized_user_file(user_credentials_path)
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            credentials_file_path, ['https://www.googleapis.com/auth/calendar'])
        creds = flow.run_local_server(port=0)
        
        with open(user_credentials_path, 'w') as token:
            token.write(creds.to_json())
    
    return creds

def create_calendar_event_for_user(summary, start_datetime, end_datetime, user):
    credentials = get_user_credentials(user)
    
    service = build('calendar', 'v3', credentials=credentials)

    event = {
        'summary': summary,
        'start': {
            'dateTime': start_datetime.strftime('%Y-%m-%dT%H:%M:%S'),
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'dateTime': end_datetime.strftime('%Y-%m-%dT%H:%M:%S'),
            'timeZone': 'Asia/Kolkata',
        },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Event created: %s' % event.get('htmlLink'))
