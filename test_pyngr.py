import unittest
from pyngr import cron, website


class TestCronRules(unittest.TestCase):

    def test_wildcard_rule(self):
        self.assertEqual(cron.validate_rule("* * * * * * *"), None)

    def test_invalid_character_rule(self):
        with self.assertRaises(SyntaxError):
            cron.validate_rule("a b c d e f g")

    def test_number_rule(self):
        self.assertEqual(cron.validate_rule("0 0 0 1 1 1 0"), None)

    def test_invalid_value_range_rule(self):
        with self.assertRaises(SyntaxError):
            cron.validate_rule("60 60 24 0 0 0 1")

    def test_list_rule(self):
        self.assertEqual(cron.validate_rule("0,1 0,1,2 0,1,2,3 1,4 1,3 1,5 0,3,5"), None)

    def test_range_rule(self):
        self.assertEqual(cron.validate_rule("0-10 0-2 0-3 1-4 1-3 1-5 0-5"), None)

    def test_interval_with_wildcard_rule(self):
        self.assertEqual(cron.validate_rule("*/10 */5 */2 */3 */8 */6 */2"), None)

    def test_interval_with_number_rule(self):
        self.assertEqual(cron.validate_rule("1-40/10 10-50/5 1-10/2 1-20/3 1-12/8 1-6/3 1-25/2"), None)


class TestWebsites(unittest.TestCase):

    def test_website_json_creation(self):
        result = website.Website("url")
        json_data = {
            "url": "url"
        }
        self.assertEqual(website.Website.generate_from_json(json_data), result)


if __name__ == '__main__':
    unittest.main()
