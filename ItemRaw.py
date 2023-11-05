from ItemHead import ItemHead


class ItemRaw:
    def __init__(self, item_head : ItemHead, raw_html, save_provider) -> None:
        self.item_head = item_head
        self.raw_html = raw_html
        self.save_provider = save_provider
        pass
    
    def save(self):
        self.save_provider.save(self)
        
        
    non_save_attr = {"save_provider"}
        
