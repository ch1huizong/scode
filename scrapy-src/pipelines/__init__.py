# -*- coding:UTF-8 -*-
# 阅
"""
Item pipeline

See documentation in docs/item-pipeline.rst
"""

from scrapy.middleware import MiddlewareManager
from scrapy.utils.conf import build_component_list

class ItemPipelineManager(MiddlewareManager):

    component_name = 'item pipeline'

    @classmethod
    def _get_mwlist_from_settings(cls, settings):   # 得到item pipeline列表 
        return build_component_list(settings.getwithbase('ITEM_PIPELINES'))

    def _add_middleware(self, pipe): # 增加pipeline 
        super(ItemPipelineManager, self)._add_middleware(pipe)
        if hasattr(pipe, 'process_item'):
            self.methods['process_item'].append(pipe.process_item) # 处理链条?

    def process_item(self, item, spider):   # 顺序处理?
        return self._process_chain('process_item', item, spider)
