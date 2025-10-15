"""Run test discovery from the project root so imports resolve the same in CI and locally."""
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

if __name__ == "__main__":
    tests = unittest.TestLoader().discover('tests', pattern='*Test*.py')
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(tests)
    sys.exit(not result.wasSuccessful())
