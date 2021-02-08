from unittest import TestCase
from time import sleep
from random import random
from scrapic import Scrapic


class ScrapicTest(TestCase):
    def setUp(self) -> None:
        self.key = 'key'
        self.value = 'value'

    def test_main(self):
        scrapic = Scrapic()
        self.assertIsNone(scrapic.get(self.key))
        self.assertEqual(self.value, scrapic.get(self.key, self.value))

        scrapic.set('other_key', 'other_value')
        self.assertEqual('other_value', scrapic.get('other_key'))

    def test_ttl(self):
        scrapic = Scrapic()
        scrapic.set(self.key, self.value, 1)
        self.assertEqual(self.value, scrapic.get(self.key))
        sleep(1)
        self.assertIsNone(scrapic.get(self.key))

    def test_callable(self):
        scrapic = Scrapic()
        result = []
        for i in range(3):
            result.append(scrapic.closure('callable', lambda: random()))
        self.assertIsNotNone(result[0])
        self.assertTrue(result[0] == result[1] == result[2])

    def test_callable_exception(self):
        scrapic = Scrapic()
        self.assertRaises(ValueError, scrapic.closure, 'key', 'value')

    def test_callable_ttl(self):
        scrapic = Scrapic()
        result = []
        for i in range(2):
            if i == 2:
                sleep(1)
            result.append(scrapic.closure('callable', lambda: random(), 1))
        self.assertIsNotNone(result[0])
        self.assertTrue(result[0] == result[1])
