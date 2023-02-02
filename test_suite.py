
import unittest
from HTMLTestRunner.runner import HTMLTestRunner

from delivery_country_change import TestDeliveryCountryChange
from first_page import TestFirstPage
from language_change import TestLanguageChange
from log_in_page import TestLogIn
from sigh_in import TestSignIn

test1 = unittest.TestLoader().loadTestsFromTestCase(TestDeliveryCountryChange)
test2 = unittest.TestLoader().loadTestsFromTestCase(TestFirstPage)
test3 = unittest.TestLoader().loadTestsFromTestCase(TestLanguageChange)
test4 = unittest.TestLoader().loadTestsFromTestCase(TestLogIn)
test5 = unittest.TestLoader().loadTestsFromTestCase(TestSignIn)

suite = unittest.TestSuite([test1, test2, test3, test4, test5])

runner = HTMLTestRunner(log=True, verbosity=5, output='report', title='Test report', report_name='report',
                        open_in_browser=True, description="HTMLTestReport", tested_by="Monica P.",
                        add_traceback=False)

runner.run(suite)
