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

# set project directory
# PROJ_HOME needs to be set to top level before first use

# When running for first time, run in intended PROJ_HOME directory.
# This allows the script to find the proj_config file.
# If PROJ_HOME: item is missing then prompt user to enter the PROJ_HOME path.
#open $PROJ_HOME/sim_config file 

proj_config = 'proj_config'
message = {
          'HOME' : "",
          'PROJ_HOME' : "Enter full path to project's home directory", 
          'PROJ_SIM'  : "Enter full path to project's sim directory", 
          'PROJ_TB'   : "Enter full path to project's testbench directory", 
          }

if os.access (proj_config, os.F_OK):
  sys.exit ('ERROR: file %s already exists' % proj_config)
else:
  fhw = open (proj_config,"w")

for key in list(message.keys()):
  if key == 'HOME':
    HOME = os.environ['HOME']
    fhw.write('%s: %s\n' % (key, HOME))
  elif key == 'PROJ_HOME':
    print ('\n', message[key], sep='')
    print ('Use $HOME for home directory', HOME)
    value = input('%s: ' % key)
    value = re.sub ('\$HOME', HOME, value)
    fhw.write('%s:\t%s\n' % (key, value))
    PROJ_HOME = value
  else:
    print ('\n', message[key], sep='')
    print ('Use $PROJ_HOME for project home directory', PROJ_HOME)
    value = input('%s: ' % key)
    value = re.sub ('\$PROJ_HOME', PROJ_HOME, value)
    fhw.write('%s:\t%s\n' % (key, value))

