from parsel import Selector
from GrabGroup import GrabGroup
from GrabbedItemLists import GrabbedItemLists
from Item import Item
from ItemRaw import ItemRaw
from ItemHead import ItemHead


class ItemsExtractor:
    
    def extract_raw_item(self, item_raw: ItemRaw) -> Item:
        sel = Selector(item_raw.raw_html)
        return Item(item_raw.item_head,
                    self.getItemDescription(sel),
                    self.getItemDate(sel))
    
    def extract(self, grabbed : GrabbedItemLists):
        sel = Selector(grabbed.raw_html)
        result = sel.xpath('//div[@data-marker="item"]').getall()
        item_selectors = [Selector(x) for x in result]
        return [ItemHead(
            self.getItemUrl(x),
            self.getItemTitle(x),
            self.getItemPrice(x),
            self.getItemId(x),
            GrabGroup(grabbed.origin_name, grabbed.date)) for x in item_selectors]

    def getItemUrl(self, item : Selector):
        result = item.xpath('//a[@itemprop="url"][not(contains(@title, "Объявление"))]/@href').getall()
        assert(len(result) == 1)
        return result[0]

    def getItemTitle(self, item : Selector):
        result = item.xpath('//a[@itemprop="url"][not(contains(@title, "Объявление"))]/@title').getall()
        assert(len(result) == 1)
        return result[0]
    
    def getItemPrice(self, item : Selector):
        result = item.xpath('//meta[@itemprop="price"]/@content').getall()
        assert(len(result) == 1)
        return float(result[0])
    
    def getItemDescription(self, item : Selector):
        result = item.xpath('//div[@data-marker="item-view/item-description"]/text()').getall()
       # result = item.xpath('//div[@data-marker="item-view/item-description"]/text()').getall()
        
        assert(len(result) == 1)
        return float(result[0])
    
    def getItemDate(self, item : Selector):
        result = item.xpath('//span[@data-marker="\&quot;item-view/item-id\&quot;"]/text()').getall()
        assert(len(result) == 1)
        return float(result[0])
    
    def getItemId(self, item : Selector):
        result = item.xpath('//div[@data-item-id]/@data-item-id').getall()
        assert(len(result) == 1)
        return float(result[0])