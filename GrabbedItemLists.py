
class GrabbedItemLists:
    def __init__(self, origin_name, date, raw_html, save_provider):
        self.date = date
        self.raw_html = raw_html
        self.origin_name = origin_name
        self.save_provider = save_provider

    def save(self):
        self.save_provider.save(self)