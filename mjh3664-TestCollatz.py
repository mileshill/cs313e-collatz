#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2014
# Glenn P. Downing
# -------------------------------

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from SphereCollatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        r    = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        i, j = collatz_read(r)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval_5 (self) :
        v = collatz_eval(10000, 20000)
        self.assertEqual(v, 279)

    def test_eval_6(self):
        v = collatz_eval(1,1)
        self.assertEqual(v,1)

    def test_eval_1_MMa (self) :
        v = collatz_eval(7466,19943)
        self.assertEqual(v,279)

    def test_eval_2_MMa (self) :
        v = collatz_eval(1408,18477)
        self.assertEqual(v,279)

    def test_eval_3_MMa (self) :
        v = collatz_eval(1673,19993)
        self.assertEqual(v,279)

    def test_eval_4_MMa (self) :
        v = collatz_eval(7980,14300)
        self.assertEqual(v,276)

    def test_eval_5_MMa (self) :
        v = collatz_eval(8099,18538)
        self.assertEqual(v,279)

    def test_eval_6_MMa (self) :
        v = collatz_eval(5719,19688)
        self.assertEqual(v,279)

    def test_eval_7_MMa (self) :
        v = collatz_eval(9829,16852)
        self.assertEqual(v,276)

    def test_eval_8_MMa (self) :
        v = collatz_eval(3171,12769)
        self.assertEqual(v,268)

    def test_eval_9_MMa (self) :
        v = collatz_eval(491,10167)
        self.assertEqual(v,262)

    def test_eval_10_MMa (self) :
        v = collatz_eval(7078,19808)
        self.assertEqual(v,279)

    def test_eval_11_MMa (self) :
        v = collatz_eval(7166,11681)
        self.assertEqual(v,268)

    def test_eval_12_MMa (self) :
        v = collatz_eval(9367,15921)
        self.assertEqual(v,276)

    def test_eval_13_MMa (self) :
        v = collatz_eval(800,17592)
        self.assertEqual(v,276)

    def test_eval_14_MMa (self) :
        v = collatz_eval(2835,10066)
        self.assertEqual(v,262)

    def test_eval_15_MMa (self) :
        v = collatz_eval(5311,18042)
        self.assertEqual(v,279)

    def test_eval_16_MMa (self) :
        v = collatz_eval(3268,10529)
        self.assertEqual(v,262)

    def test_eval_17_MMa (self) :
        v = collatz_eval(8144,19863)
        self.assertEqual(v,279)

    def test_eval_18_MMa (self) :
        v = collatz_eval(153,10318)
        self.assertEqual(v,262)

    def test_eval_19_MMa (self) :
        v = collatz_eval(3,16868)
        self.assertEqual(v,276)

    def test_eval_20_MMa (self) :
        v = collatz_eval(7111,11816)
        self.assertEqual(v,268)

    def test_eval_21_MMa (self) :
        v = collatz_eval(3846,14675)
        self.assertEqual(v,276)

    def test_eval_22_MMa (self) :
        v = collatz_eval(8644,17189)
        self.assertEqual(v,276)

    def test_eval_23_MMa (self) :
        v = collatz_eval(9598,18269)
        self.assertEqual(v,279)

    def test_eval_24_MMa (self) :
        v = collatz_eval(3257,15245)
        self.assertEqual(v,276)

    def test_eval_25_MMa (self) :
        v = collatz_eval(2650,17111)
        self.assertEqual(v,276)

    def test_eval_26_MMa (self) :
        v = collatz_eval(9569,15199)
        self.assertEqual(v,276)

    def test_eval_27_MMa (self) :
        v = collatz_eval(5863,16463)
        self.assertEqual(v,276)

    def test_eval_28_MMa (self) :
        v = collatz_eval(418,14709)
        self.assertEqual(v,276)

    def test_eval_29_MMa (self) :
        v = collatz_eval(2859,10192)
        self.assertEqual(v,262)

    def test_eval_30_MMa (self) :
        v = collatz_eval(4365,18267)
        self.assertEqual(v,279)

    def test_eval_31_MMa (self) :
        v = collatz_eval(6586,13688)
        self.assertEqual(v,276)

    def test_eval_32_MMa (self) :
        v = collatz_eval(7580,19115)
        self.assertEqual(v,279)

    def test_eval_33_MMa (self) :
        v = collatz_eval(8414,14834)
        self.assertEqual(v,276)

    def test_eval_34_MMa (self) :
        v = collatz_eval(9041,19331)
        self.assertEqual(v,279)

    def test_eval_35_MMa (self) :
        v = collatz_eval(1189,15000)
        self.assertEqual(v,276)

    def test_eval_36_MMa (self) :
        v = collatz_eval(8222,17834)
        self.assertEqual(v,279)

    def test_eval_37_MMa (self) :
        v = collatz_eval(8160,16911)
        self.assertEqual(v,276)

    def test_eval_38_MMa (self) :
        v = collatz_eval(4661,17572)
        self.assertEqual(v,276)

    def test_eval_39_MMa (self) :
        v = collatz_eval(9431,17234)
        self.assertEqual(v,276)

    def test_eval_40_MMa (self) :
        v = collatz_eval(2788,14265)
        self.assertEqual(v,276)

    def test_eval_41_MMa (self) :
        v = collatz_eval(4683,19350)
        self.assertEqual(v,279)

    def test_eval_42_MMa (self) :
        v = collatz_eval(326,15111)
        self.assertEqual(v,276)

    def test_eval_43_MMa (self) :
        v = collatz_eval(1343,18973)
        self.assertEqual(v,279)

    def test_eval_44_MMa (self) :
        v = collatz_eval(4984,15478)
        self.assertEqual(v,276)

    def test_eval_45_MMa (self) :
        v = collatz_eval(716,13380)
        self.assertEqual(v,276)

    def test_eval_46_MMa (self) :
        v = collatz_eval(869,14306)
        self.assertEqual(v,276)

    def test_eval_47_MMa (self) :
        v = collatz_eval(812,14993)
        self.assertEqual(v,276)

    def test_eval_48_MMa (self) :
        v = collatz_eval(2214,18349)
        self.assertEqual(v,279)

    def test_eval_49_MMa (self) :
        v = collatz_eval(6056,10107)
        self.assertEqual(v,262)

    def test_eval_50_MMa (self) :
        v = collatz_eval(7344,16542)
        self.assertEqual(v,276)

    def test_eval_51_MMa (self) :
        v = collatz_eval(1199,16614)
        self.assertEqual(v,276)

    def test_eval_52_MMa (self) :
        v = collatz_eval(350,13479)
        self.assertEqual(v,276)

    def test_eval_53_MMa (self) :
        v = collatz_eval(9654,18291)
        self.assertEqual(v,279)

    def test_eval_54_MMa (self) :
        v = collatz_eval(4221,19638)
        self.assertEqual(v,279)

    def test_eval_55_MMa (self) :
        v = collatz_eval(5678,11311)
        self.assertEqual(v,268)

    def test_eval_56_MMa (self) :
        v = collatz_eval(5502,13181)
        self.assertEqual(v,268)

    def test_eval_57_MMa (self) :
        v = collatz_eval(6576,15127)
        self.assertEqual(v,276)

    def test_eval_58_MMa (self) :
        v = collatz_eval(9635,18914)
        self.assertEqual(v,279)

    def test_eval_59_MMa (self) :
        v = collatz_eval(1985,11072)
        self.assertEqual(v,268)

    def test_eval_60_MMa (self) :
        v = collatz_eval(321,18121)
        self.assertEqual(v,279)

    def test_eval_61_MMa (self) :
        v = collatz_eval(348,15531)
        self.assertEqual(v,276)

    def test_eval_62_MMa (self) :
        v = collatz_eval(8992,19063)
        self.assertEqual(v,279)

    def test_eval_63_MMa (self) :
        v = collatz_eval(5997,16417)
        self.assertEqual(v,276)

    def test_eval_64_MMa (self) :
        v = collatz_eval(2701,19881)
        self.assertEqual(v,279)

    def test_eval_65_MMa (self) :
        v = collatz_eval(6155,13624)
        self.assertEqual(v,276)

    def test_eval_66_MMa (self) :
        v = collatz_eval(5451,17149)
        self.assertEqual(v,276)

    def test_eval_67_MMa (self) :
        v = collatz_eval(364,19763)
        self.assertEqual(v,279)

    def test_eval_68_MMa (self) :
        v = collatz_eval(621,19574)
        self.assertEqual(v,279)

    def test_eval_69_MMa (self) :
        v = collatz_eval(1012,15721)
        self.assertEqual(v,276)

    def test_eval_70_MMa (self) :
        v = collatz_eval(8173,15589)
        self.assertEqual(v,276)

    def test_eval_71_MMa (self) :
        v = collatz_eval(3321,10158)
        self.assertEqual(v,262)

    def test_eval_72_MMa (self) :
        v = collatz_eval(5449,11342)
        self.assertEqual(v,268)

    def test_eval_73_MMa (self) :
        v = collatz_eval(6966,14749)
        self.assertEqual(v,276)

    def test_eval_74_MMa (self) :
        v = collatz_eval(8177,18806)
        self.assertEqual(v,279)

    def test_eval_75_MMa (self) :
        v = collatz_eval(6261,18418)
        self.assertEqual(v,279)

    def test_eval_76_MMa (self) :
        v = collatz_eval(5642,17612)
        self.assertEqual(v,276)

    def test_eval_77_MMa (self) :
        v = collatz_eval(7821,19739)
        self.assertEqual(v,279)

    def test_eval_78_MMa (self) :
        v = collatz_eval(8458,18650)
        self.assertEqual(v,279)

    def test_eval_79_MMa (self) :
        v = collatz_eval(8055,13769)
        self.assertEqual(v,276)

    def test_eval_80_MMa (self) :
        v = collatz_eval(3996,16287)
        self.assertEqual(v,276)

    def test_eval_81_MMa (self) :
        v = collatz_eval(7036,15114)
        self.assertEqual(v,276)

    def test_eval_82_MMa (self) :
        v = collatz_eval(5822,10270)
        self.assertEqual(v,262)

    def test_eval_83_MMa (self) :
        v = collatz_eval(3171,14938)
        self.assertEqual(v,276)

    def test_eval_84_MMa (self) :
        v = collatz_eval(4968,12465)
        self.assertEqual(v,268)

    def test_eval_85_MMa (self) :
        v = collatz_eval(9151,12176)
        self.assertEqual(v,268)

    def test_eval_86_MMa (self) :
        v = collatz_eval(5297,15087)
        self.assertEqual(v,276)

    def test_eval_87_MMa (self) :
        v = collatz_eval(511,16005)
        self.assertEqual(v,276)

    def test_eval_88_MMa (self) :
        v = collatz_eval(8698,19931)
        self.assertEqual(v,279)

    def test_eval_89_MMa (self) :
        v = collatz_eval(2018,10088)
        self.assertEqual(v,262)

    def test_eval_90_MMa (self) :
        v = collatz_eval(9486,14855)
        self.assertEqual(v,276)

    def test_eval_91_MMa (self) :
        v = collatz_eval(4239,16982)
        self.assertEqual(v,276)

    def test_eval_92_MMa (self) :
        v = collatz_eval(7014,13910)
        self.assertEqual(v,276)

    def test_eval_93_MMa (self) :
        v = collatz_eval(807,17207)
        self.assertEqual(v,276)

    def test_eval_94_MMa (self) :
        v = collatz_eval(6220,16760)
        self.assertEqual(v,276)

    def test_eval_95_MMa (self) :
        v = collatz_eval(6939,11583)
        self.assertEqual(v,268)

    def test_eval_96_MMa (self) :
        v = collatz_eval(4050,12138)
        self.assertEqual(v,268)

    def test_eval_97_MMa (self) :
        v = collatz_eval(7493,13345)
        self.assertEqual(v,276)

    def test_eval_98_MMa (self) :
        v = collatz_eval(9997,19382)
        self.assertEqual(v,279)

    def test_eval_99_MMa (self) :
        v = collatz_eval(1028,10835)
        self.assertEqual(v,262)

    def test_eval_100_MMa (self) :
        v = collatz_eval(922,11003)
        self.assertEqual(v,268)








    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

# ----
# main
# ----

main()

"""
% coverage3 run --branch TestCollatz.py
FFFF..F
======================================================================
FAIL: test_eval_1 (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz.py", line 47, in test_eval_1
    self.assertEqual(v, 20)
AssertionError: 1 != 20

======================================================================
FAIL: test_eval_2 (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz.py", line 51, in test_eval_2
    self.assertEqual(v, 125)
AssertionError: 1 != 125

======================================================================
FAIL: test_eval_3 (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz.py", line 55, in test_eval_3
    self.assertEqual(v, 89)
AssertionError: 1 != 89

======================================================================
FAIL: test_eval_4 (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz.py", line 59, in test_eval_4
    self.assertEqual(v, 174)
AssertionError: 1 != 174

======================================================================
FAIL: test_solve (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz.py", line 78, in test_solve
    self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
AssertionError: '1 10 1\n100 200 1\n201 210 1\n900 1000 1\n' != '1 10 20\n100 200 125\n201 210 89\n900 1000 174\n'
- 1 10 1
?      ^
+ 1 10 20
?      ^^
- 100 200 1
+ 100 200 125
?          ++
- 201 210 1
?         ^
+ 201 210 89
?         ^^
- 900 1000 1
+ 900 1000 174
?           ++


----------------------------------------------------------------------
Ran 7 tests in 0.004s

FAILED (failures=5)



% coverage3 report -m
Name           Stmts   Miss Branch BrMiss  Cover   Missing
----------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      33      1      0      0    97%   86
----------------------------------------------------------
TOTAL            51      1      6      0    98%
"""
