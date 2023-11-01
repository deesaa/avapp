from GrabbedItemLists import GrabbedItemLists
from main import SaveProvider, avitoSsdUrl


import requests


import datetime


class ItemsListGrabber:
    def __init__(self, name, url):
        self.name = name
        self.url = url

    def create_grab(self):
        currentTime = datetime.datetime.utcnow().isoformat(sep=" ", timespec="seconds")
        headers = {'Content-Type': 'text/html',}
        response = requests.get(avitoSsdUrl, headers=headers)
        raw_html = response.text
        return GrabbedItemLists(self.name, currentTime, raw_html)

    def restore(self):
        loaded = SaveProvider.loadAll(self.name)
        return [GrabbedItemLists(self.name, l[0], l[1]) for l in loaded]