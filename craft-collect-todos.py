import json
import glob
from datetime import date
import pync
import webbrowser
import urllib.parse

# Set your Craft Library path, e.g. /Users/me/Library/Mobile Documents/com~apple~CloudDocs/CRAFT
libraryPath = 'path/to/Craft/Library' 

docTitle 	= 'Open Todos for ' + str (date.today())
todoItems = []
todoString = ''

for filepath in glob.iglob( libraryPath + '/*.json' ) :
	
	with open(filepath) as f:
		data = json.load(f)
		
		# make sure we are not parsing some of Craft's folder.json or other files
		if ( 'spaceID' in data ) :
			
			spaceID = data['spaceID']
			content = data['content']
			
			for item in content:
				if ( item.get('type') == 'text' and 'todo' in item.get('style') and not '"isTodoChecked":"1"' in item.get('rawProperties') ) :
					# todoItems.append("<li><a href='craftdocs://open?spaceId=" + spaceID + "&blockId=" + item.get('id') + "'>" + item.get('content') + "</a></li>") 
					todoItems.append('* [' + item.get('content') + '](craftdocs://open?spaceId=' + spaceID + '&blockId=' + item.get('id') + ') \n' )

todoCount = len( todoItems );
todoString = ' '.join(todoItems);
url = 'craftdocs://createdocument?spaceId=' + urllib.parse.quote ( spaceID ) + '&title=' + urllib.parse.quote ( docTitle ) + '&content=' + urllib.parse.quote ( todoString ) 
webbrowser.open( url )
pync.notify( str( todoCount ) + ' Todos open', title='Craft Todos Collected' )