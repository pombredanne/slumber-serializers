import unittest
import slumber
import slumber.serialize

from slumber_serializers import CsvSerializer


class CsvSerializerTestCase(unittest.TestCase):
    def setUp(self):
        self.data = [
            ['foo', 'bar'],
            ['1', '2'],
            ['3', '4'],
        ]

        self.serializers = slumber.serialize.Serializer(serializers=[slumber.serialize.JsonSerializer(),
                                                                     slumber.serialize.YamlSerializer(),
                                                                     CsvSerializer()])

    def test_get_serializer(self):
        serializer = self.serializers.get_serializer(content_type='text/csv')

        self.assertEqual(type(serializer), CsvSerializer,
                         'content_type text/csv should produce a CsvSerializer')

    def test_dumps(self):
        serializer = self.serializers.get_serializer(content_type='text/csv')

        result = serializer.dumps(self.data)
        self.assertEqual(result, b'foo,bar\r\n1,2\r\n3,4\r\n')

    def test_loads(self):
        serializer = self.serializers.get_serializer(content_type='text/csv')
        result = b'foo,bar\r\n1,2\r\n3,4'

        self.assertEqual(self.data, list(serializer.loads(result)))
