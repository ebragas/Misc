
from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as Types

oauth_token = "S=s1:U=94432:E=167d3aa2947:C=1607bf8fb38:P=1cd:A=en-devtoken:V=2:H=340ffdbe6e147a1c053eb28f877ac446"

# Connect client
client = EvernoteClient(token=oauth_token)

# Get note store
note_store = client.get_note_store()

# Create note

# Upload note

