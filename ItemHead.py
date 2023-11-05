from GrabGroup import GrabGroup


class ItemHead:
    def __init__(self, url : str, title : str, price : float, id : str, grab_group: GrabGroup) -> None:
        self.url = url
        self.title = title
        self.grab_group = grab_group
        self.price = price
        self.id = id
        pass