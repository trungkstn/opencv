#!/usr/bin/env python
from __future__ import print_function

import numpy as np
import cv2

from tests_common import NewOpenCVTests

class Bindings(NewOpenCVTests):

    def test_inheritance(self):
        bm = cv2.StereoBM_create()
        bm.getPreFilterCap() # from StereoBM
        bm.getBlockSize() # from SteroMatcher

        boost = cv2.ml.Boost_create()
        boost.getBoostType() # from ml::Boost
        boost.getMaxDepth() # from ml::DTrees
        boost.isClassifier() # from ml::StatModel

if __name__ == '__main__':
    NewOpenCVTests.bootstrap()
