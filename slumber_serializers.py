from six import BytesIO
from slumber import serialize
from unicodecsv import reader, writer


class CsvSerializer(serialize.BaseSerializer):
    key = "csv"
    content_types = ["text/csv"]

    def loads(self, data):
        output = BytesIO(data)
        return reader(output)

    def dumps(self, data):
        output = BytesIO()
        writer(output).writerows(data)
        return output.getvalue()
