#! /usr/bin/env python3
##------------------------------------------------------------------------------
##  Copyright (c) 2021 by Strauch Consulting, LLC. and Xpeerant, Inc.
##
##  Licensed under the Apache License, Version 2.0 (the "License");
##  you may not use this file except in compliance with the License.
##  You may obtain a copy of the License at
##
##  http://www.apache.org/licenses/LICENSE-2.0
##
##  Unless required by applicable law or agreed to in writing, software
##  distributed under the License is distributed on an "AS IS" BASIS,
##  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
##  See the License for the specific language governing permissions and
##  limitations under the License.
##------------------------------------------------------------------------------

import sys 
import os
import re

################################################################################
# Read configuration file and return items in a dictionary
################################################################################
def get_config (filename):
  # TODO: trap exception FileNotFoundError
  fhr = open (filename,"r")

  config = {}
  for line in fhr.readlines():
    # get the key:value
    mObj = re.search ('^\s*(\w+)\s*:\s*([\w/]+)', line)
    if mObj:
      key   = mObj.group(1)
      value = mObj.group(2)
      config[key] = value
  return config

