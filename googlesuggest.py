import requests
import xml.etree.ElementTree as ET

def googlesuggest(q):
    reply = requests.get(
        'http://www.google.com/complete/search',
        params=dict(
            output='toolbar',
            q=q))
    if reply.status_code != 200:
        raise RuntimeError('connection error')

    root = ET.fromstring(reply.content)
    return [child.attrib['data'] for child in root.iter('suggestion')]
