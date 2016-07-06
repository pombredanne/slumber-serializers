import unittest
import slumber
import slumber.serialize

from slumber_serializers import CsvSerializer


class CsvSerializerTestCase(unittest.TestCase):
    def setUp(self):
        self.data = [
            [
                "foo", "bar"
            ]
        ]

    def test_csv_serializer(self):
        s = slumber.serialize.Serializer(serializers=[slumber.serialize.JsonSerializer(),
                                                      slumber.serialize.YamlSerializer(),
                                                      CsvSerializer()])

        serializer = None
        for content_type in [
            "text/csv",
        ]:
            serializer = s.get_serializer(content_type=content_type)
            self.assertEqual(type(serializer), CsvSerializer,
                             "content_type %s should produce a CsvSerializer" % content_type)

        result = serializer.dumps(self.data)
        self.assertEqual(result, b"foo,bar\r\n")
        self.assertEqual(self.data, list(serializer.loads(result)))
