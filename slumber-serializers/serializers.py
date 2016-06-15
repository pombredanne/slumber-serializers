import csv
from StringIO import StringIO

from slumber import serialize


class CsvSerializer(serialize.BaseSerializer):
    key = "csv"
    content_types = ["text/csv"]

    def loads(self, data):
        output = StringIO(data)
        csv.reader(output)
        return output.getvalue()

    def dumps(self, data):
        raise NotImplementedError("CsvSerializer method dumps is not implemented")
