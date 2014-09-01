#!/usr/bin/env python
# coding: utf-8

import unittest

from crawler.spiders.ecp import EcpSpider


class EcpSpiderTestCase(unittest.TestCase):
    def test_sanitize_removes_leading_and_trailing_characters(self):
        s = "    \n         word1 word2     \n\n\n "
        expected_s = "word1 word2"

        sanitized_s = EcpSpider.sanitize(s)

        self.assertEqual(sanitized_s, expected_s)

    def test_sanitize_removes_all_newline_characters(self):
        s = "    \n         word1 \n\nword2     \n\n\n "
        expected_s = "word1 word2"

        sanitized_s = EcpSpider.sanitize(s)

        self.assertEqual(sanitized_s, expected_s)

if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(EcpSpiderTestCase)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()
