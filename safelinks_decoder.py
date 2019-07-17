import re
import urllib
import HTMLParser

urlRegex = re.compile(r'(.+)&data=')
match=urlRegex.search('https://na01.safelinks.protection.outlook.com/?url=https%3A%2F%2Foffice.memoriesflower.com%2FPermission%2F%2525%2524%255E%2526%2526*%2523%2523%255E%2524%2525%255E%2526%255E*%2526%2523%255E%2525%2525%2526%2540%255E*%2523%2526%255E%2525%2523%2526%2540%2525*%255E%2540%255E%2523%2525%255E%2540%2526%2525*%255E%2540%2Foffice.php&data=01%7C01%7Cdavid.levin%40mheducation.com%7C0ac9a3770fe64fbb21fb08d50764c401%7Cf919b1efc0c347358fca0928ec39d8d5%7C0&sdata=PEoDOerQnha%2FACafNx8JAep8O9MdllcKCsHET2Ye%2B4%3D&reserved=0')
x = match.group()
urlRegex_1 = re.compile(r'url=(.+)&data=')
match_1 = urlRegex_1.search(x)
print match1.group(1)
htmlencodedurl = urllib.unquote(urllib.unquote(match1.group(1)))
actual_url = HTMLParser.HTMLParser().unescape(htmlencodedurl)
