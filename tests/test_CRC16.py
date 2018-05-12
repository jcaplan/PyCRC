#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TEST CRC16 Module
"""

import unittest

from PyCRC.CRC16 import CRC16  # NOQA


class CRC16Test(unittest.TestCase):
    def setUp(self):
        self.crc = CRC16()
        self.crc_modbus = CRC16(modbus_flag=True)

    def testCalculateModBus(self):
        msg = "Calculated CRC16 MODBUS for 0123456789 should be 0x434D"
        self.assertEqual(
            self.crc_modbus.calculate("0123456789"), int('0x434D', 0), msg)

    def testModbusInit(self):
        msg = "Initializing with modbus flag True should setup internal flag to True"
        self.assertEqual(self.crc_modbus.mdflag, 1, msg)

    def testNoneArgCalculate(self):
        msg = ("Providing calculate method with argument set to None should "
               "result in an Exception")
        self.assertRaises(Exception, self.crc.calculate(None), msg)

    def testNoArgCalculate(self):
        msg = ("Providing calculate method with no argument should return "
               "result in an Exception")
        self.assertRaises(Exception, self.crc.calculate(), msg)

    def testCalculate(self):
        msg = "Calculated CRC16 for 0123456789 should be 0x443D"
        self.assertEqual(self.crc.calculate("0123456789"), int('0x443D', 0), msg)

    def testCalculateBytearray(self):
        msg = "Calculated CRC16 for 0123456789 should still be 0x443D" \
              " when passing a bytearray parameter."
        self.assertEqual(
            self.crc.calculate(bytearray("0123456789".encode('utf-8'))), int('0x443D', 0), msg)

    def testCalculateMultiple(self):
        msg = "Calculated CRC16 for 0x1234567812345678 in segments"
        x = self.crc.calculate("1234567812345678".encode('utf-8'))
        y = self.crc.calculate("12345678".encode('utf-8'))
        y = self.crc.calculate("12345678".encode('utf-8'), y)
        self.assertEqual(x, y, msg)

    def testTableItem42(self):
        msg = "The precalculated table's item #42 should be 57217 (0xdf81)"
        self.assertEqual(self.crc.crc16_tab[42], 57217, msg)

    def testTableItem10(self):
        msg = "The precalculated table's item #10 should be 1920 (0x780)"
        self.assertEqual(self.crc.crc16_tab[10], 1920, msg)

    def testTableItems(self):
        msg = ("After creating a CRC16 object we must have a precalculated "
               "table with 256 items")
        self.assertEqual(len(self.crc.crc16_tab), 256, msg)

    def testTableNotEmpty(self):
        msg = ("After creating a CRC16 object we must have a precalculated "
               "table not empty")
        self.assertIsNot(self.crc.crc16_tab, [], msg)

    def tearDown(self):
        pass


def buildTestSuite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)


def main():
    buildTestSuite()
    unittest.main()

if __name__ == "__main__":
    main()
