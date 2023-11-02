from ItemsListGrabber import ItemsListGrabber


class GrabbersPool:
    def __init__(self, grab_config : dict) -> None:
        self.grabbers = dict()
        for grabber_config_key in grab_config.keys():
            value = grab_config[grabber_config_key]
            url = value["url"]
            grabber = ItemsListGrabber(grabber_config_key, url)
            if("title_exclude" in value):
                grabber.add_excluder(value["title_exclude"])
                
            self.grabbers[grabber_config_key] = grabber

    def get_grabber(self, origin_name) -> ItemsListGrabber:
        return self.grabbers[origin_name]