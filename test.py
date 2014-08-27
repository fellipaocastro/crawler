#!/usr/bin/env python
# coding: utf-8
import unittest

from crawler import crawler


class CrawlerTestCase(unittest.TestCase):
    def test_crawler_should_return_True(self):
        self.assertTrue(crawler())

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CrawlerTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
