"""Make tests a package so unittest can import test modules reliably in CI.

Having this file helps when CI or other tools import tests as a package
(`tests.TemperatureConverter_UnitTest`) instead of as a top-level module.
"""

__all__ = []
