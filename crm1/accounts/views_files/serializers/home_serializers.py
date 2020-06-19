from ...utils.view_imports_util import serializers

class custumer_serializer(serializers.Serializer):
    id = serializers.IntegerField()

class order_serializer(serializers.Serializer):
    id = serializers.IntegerField()
    product = serializers.CharField()
    custumer = custumer_serializer()
    date_created = serializers.CharField()
    status = serializers.CharField()

class home_serializer(serializers.Serializer):
    page_start = serializers.IntegerField()
    page_end = serializers.IntegerField()
    page_active = serializers.IntegerField()
    items = order_serializer(many=True)

class home_page(object):
    def __init__(self, page_start,page_end, page_active, items):
        self.page_start = page_start
        self.page_end = page_end
        self.page_active = page_active
        self.items = items