import unittest
import slumber
import slumber.serialize

from slumber_serializers import CsvSerializer, BinarySerializer


class CsvSerializerTestCase(unittest.TestCase):
    def setUp(self):
        self.data = [
            ['foo', 'bar'],
            ['1', '2'],
            ['3', '4'],
        ]

        self.slumber_serializer = slumber.serialize.Serializer(serializers=[slumber.serialize.JsonSerializer(),
                                                                            slumber.serialize.YamlSerializer(),
                                                                            CsvSerializer()])

    def test_get_serializer(self):
        serializer = self.slumber_serializer.get_serializer(content_type='text/csv')

        self.assertEqual(type(serializer), CsvSerializer,
                         'content_type text/csv should produce a CsvSerializer')

    def test_dumps(self):
        serializer = self.slumber_serializer.get_serializer(content_type='text/csv')
        result = serializer.dumps(self.data)

        self.assertEqual(result, b'foo,bar\r\n1,2\r\n3,4\r\n')

    def test_loads(self):
        serializer = self.slumber_serializer.get_serializer(content_type='text/csv')
        result = b'foo,bar\r\n1,2\r\n3,4'

        self.assertEqual(self.data, list(serializer.loads(result)))


class BinarySerializerTestCase(unittest.TestCase):
    def setUp(self):
        self.data = b'binary data'
        self.slumber_serializer = slumber.serialize.Serializer(serializers=[slumber.serialize.JsonSerializer(),
                                                                            slumber.serialize.YamlSerializer(),
                                                                            BinarySerializer()], default='binary')

    def test_get_serializer(self):
        for content_type in [
            'image/gif',
        ]:
            serializer = self.slumber_serializer.get_serializer(content_type=content_type)

            self.assertEqual(type(serializer), BinarySerializer,
                             'content_type %s should produce a BinarySerializer' % content_type)

    def test_dumps(self):
        serializer = self.slumber_serializer.get_serializer(content_type='image/gif')
        result = serializer.dumps(self.data)

        self.assertEqual(result, b'binary data')

    def test_binary_serializer(self):
        serializer = self.slumber_serializer.get_serializer(content_type='image/gif')
        result = b'binary data'

        self.assertEqual(self.data, serializer.loads(result))
