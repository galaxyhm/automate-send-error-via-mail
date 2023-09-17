#! /usr/bin/env python3

import unittest
import emails
class TestEmail(unittest.TestCase):
    def test_base_generate_email(self):
        testcase = {
            "sender" : "sender@example.com",
            "recipient" : "recipient@example.com",
            "subject" : "test",
            "body" : "한글 this is test\n body"
        }
        returntest = emails.generate_email(**testcase)
        
        #Test sender value 
        expected = testcase['sender']
        self.assertEqual(returntest['From'], expected)


        #Test recipient value 
        expected = testcase['recipient']
        self.assertEqual(returntest['To'], expected)

        #Test subject value 
        expected = testcase['subject']
        self.assertEqual(returntest['Subject'], expected)

        # Test body value 
        expected = testcase['body']
        # remove a "\n" sign. 
        result = returntest.get_payload(decode=True).decode('utf-8')[:-1]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()