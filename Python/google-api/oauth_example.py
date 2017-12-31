#!/usr/bin/python

import sys
import httplib2

from apiclient.discovery import build
from oauth2client import tools
from oauth2client.file import Storage
from oauth2client.client import AccessTokenRefreshError
from oauth2client.client import OAuth2WebServerFlow

# Client ID and Secret are command line arguments
# client_id = sys.argv[1]
# client_secret = sys.argv[2]
client_id = '913949980794-fmq6jj8krpes78t2ehs48ql4tgmtbdd6.apps.googleusercontent.com'
client_secret = 'nwflWfnUF1O8NFy1v_jZPHcm'

# Google Calendar scope URL for read/write access
scope = 'https://www.googleapis.com/auth/calendar'

# Create flow object. Contains client_id and client_secret and assists
# with OAuth 2.0 steps for user authorization and credentials
flow = OAuth2WebServerFlow(client_id, client_secret, scope)

def main():

    # Create Storage object. Holds credentials required to authorize
    # access to user data. Name of credentials file is provided. If one
    # doesn't exist, create one. Object only holds credentials for a
    # single user.
    storage = Storage('credentials.dat')

    # The get() function returns the credentials for the Storage object.
    # If none found, None returned.
    credentials = storage.get()

    # If no credentials found or are expired, new creds are obtained from 
    # authorization server. oauth2client.tools.run_flow() will attempt to
    # open an authorization page in your browser. If user grants permission,
    # the run_flow() function returns new credentials.

    # New credentials are stored in Storage object, which updates file.
    if credentials is None or credentials.invalid:
        credentials = tools.run_flow(flow, storage, tools.argparser.parse_args())

    # Create an httplib2.Http object to handle our HTTP requests, and authorize it
    # using the credentials.authorize() function.
    http = httplib2.Http()
    http = credentials.authorize(http)

    # The apiclient.discovery.build() function returns an API service object
    # which can be used to make (generate?) API calls (http requests?).
    service = build('calendar', 'v3', http=http)

    try:

        # The Calendar APIs events().list method returns paginated results, so we
        # have to execute the request in a paging loop. First, build the request
        # object.
        request = service.events().list(calendarId='primary')

        # Loop until all pages processed
        while request != None:

            # Get the next page
            response = request.execute()

            # Accessing the respsonse like a dict object with 'items' key returns
            # a list of item objects (events)
            for event in response.get('items', []):

                # The event object is a dict with a 'summary' key
                print(repr(event.get('summary', 'NO SUMMARY')) + '\n')

            # Get the next request object by passing the current to the list_next
            # method.
            request = service.events().list_next(request, response)

    except AccessTokenRefreshError:

        # Raised if the credentials have been revoked by the user or they have
        # expired.
        print('The credentials have been revoked or expired, please re-run'
              'the application to re-authorize.')

if __name__ == '__main__':
    main()
