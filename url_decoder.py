import sys
import re
import urllib.parse
import html.parser

def decode(rewritttenurl):
	match = re.search(r'https://urldefense.proofpoint.com/(v[0-9])/', rewrittenurl)
	if match:
		if match.group(1) == 'v1':
			return_url = decodev1(rewrittenurl)
		elif match.group(1) == 'v2':
			return_url = decodev2(rewrittenurl)
		else:
			phantom.debug('Unrecognized version in: ', rewrittenurl)
            return_url = '' #empty URL case
		#v1 or v2 or empty, what do we do if empty. We will return an empty value
        return return_url
	else:
		phantom.debug('No valid URL found in input: ', rewrittenurl)
        phantom.error('URL not in a valid format')
        return

def decodev1 (rewrittenurl):
	match = re.search(r'u=(.+?)&k=',rewrittenurl)
	if match:
		urlencodedurl = match.group(1)
		htmlencodedurl = urllib.parse.unquote(urlencodedurl)
		url_1 = html.parser.HTMLParser().unescape(htmlencodedurl)
		return url_1

def decodev2 (rewrittenurl):
	match = re.search(r'u=(.+?)&[dc]=',rewrittenurl)
	if match:
		specialencodedurl = match.group(1)
		trans = str.maketrans('-_', '%/')
		urlencodedurl = specialencodedurl.translate(trans)
		htmlencodedurl = urllib.parse.unquote(urlencodedurl)
		url_2 = html.parser.HTMLParser().unescape(htmlencodedurl)
		return url_2
