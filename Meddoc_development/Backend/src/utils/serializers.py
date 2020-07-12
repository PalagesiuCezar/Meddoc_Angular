from rest_framework import serializers


class DynamicFieldsModelSerializer(serializers.HyperlinkedModelSerializer):

    def __init__(self, *args, **kwargs):

        fields = kwargs.pop('fields', None)
        exclude = kwargs.pop('exclude', None)

        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields:

            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

        if exclude:

            for field_name in exclude:
                try:
                    self.fields.pop(field_name)
                except KeyError:
                    pass
