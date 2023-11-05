import time
from GrabbersPool import GrabbersPool
from ItemsExtractor import ItemsExtractor
from GrabConfig import GrabConfig
import asyncio

class Executor:
    def DoGrab():
        grabbers_pool = GrabbersPool(GrabConfig)
        grabber = grabbers_pool.get_grabber("SSD_cheap_600rub_allregions")
        itemExtractor = ItemsExtractor()
        grab = grabber.create_grab()
        grab.save()
        
        item_heads = itemExtractor.extract(grab)
        item_heads_included = [x for x in item_heads if not grabber.is_exclude_item_head(x)]
        items_raw = [grabber.create_item_from_head(x) for x in item_heads_included[:2]]
        [x.save() for x in items_raw[:2]]

        items = [itemExtractor.extract_raw_item(x) for x in items_raw]
        itemExtractor.extract(items[0])
        
        
        
class Scheduler:
    def post():
        pass