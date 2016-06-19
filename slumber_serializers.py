from six import StringIO
from slumber import serialize
from unicodecsv import reader, writer


class CsvSerializer(serialize.BaseSerializer):
    key = "csv"
    content_types = ["text/csv"]

    def loads(self, data):
        output = StringIO(data)
        return reader(output)

    def dumps(self, data):
        output = StringIO()
        writer(output).writerows(data)
        return output.getvalue()
