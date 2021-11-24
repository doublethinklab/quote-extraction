import unittest

from quote_extraction.direct_quotes import replace


class TestReplace(unittest.TestCase):

    def test_sentence_end_period_within_quote(self):
        text = 'They said, "This is my quote."'
        result = replace(text)
        expected = 'They said, QUOTE.'
        self.assertEqual(expected, result)

    def test_double_quote_char(self):
        text = 'Five Coalition senators have crossed the floor to support ' \
               'One Nation\'s plan to outlaw "discrimination" against ' \
               'unvaccinated Australians, @JoshButler reports. #auspol'
        result = replace(text)
        expected = 'Five Coalition senators have crossed the floor to ' \
                   'support One Nation\'s plan to outlaw QUOTE against ' \
                   'unvaccinated Australians, @JoshButler reports. #auspol'
        self.assertEqual(expected, result)

    def test_quote_char_as_apostrophe_within_quote(self):
        text = "Taiwan independence: the ‘red line’ that Tsai Ing-wen and " \
               "the DPP ‘won’t cross’ – SCMP talks to anyone but the " \
               "proponents of the Tsai line"
        result = replace(text)
        expected = "Taiwan independence: the QUOTE that Tsai Ing-wen and " \
                   "the DPP QUOTE – SCMP talks to anyone but the " \
                   "proponents of the Tsai line"
        self.assertEqual(expected, result)

    def test_multiple_sentence_quote(self):
        text = 'very strong speech from Jacqui Lambie, bluntly opposing ' \
               'One Nation\'s vaccine mandate "discrimination" bill: ' \
               '"that\'s the way it is. We do that to keep people safe. ' \
               'How about that?"'
        result = replace(text)
        expected = 'very strong speech from Jacqui Lambie, bluntly opposing ' \
                   'One Nation\'s vaccine mandate QUOTE bill: QUOTE.'
        self.assertEqual(expected, result)

    def test_quote_within_quote_different_quote_chars(self):
        text = 'full story: 5 Coalition senators back One Nation, as ' \
               'Lambie blasts Hanson: "You can\'t call the consequences ' \
               'of every choice ‘discrimination’... You\'re choosing ' \
               'to do something that puts people’s lives at risk and you ' \
               'will be held accountable" #auspol'
        result = replace(text)
        expected = 'full story: 5 Coalition senators back One Nation, as ' \
                   'Lambie blasts Hanson: QUOTE #auspol'
        self.assertEqual(expected, result)

    def test_quote_within_quote_same_quote_chars(self):
        text = 'full story: 5 Coalition senators back One Nation, as ' \
               'Lambie blasts Hanson: "You can\'t call the consequences ' \
               'of every choice "discrimination"... You\'re choosing ' \
               'to do something that puts people’s lives at risk and you ' \
               'will be held accountable" #auspol'
        result = replace(text)
        expected = 'full story: 5 Coalition senators back One Nation, as ' \
                   'Lambie blasts Hanson: QUOTE #auspol'
        self.assertEqual(expected, result)
