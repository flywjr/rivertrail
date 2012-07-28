#!/usr/bin/python
#
# Copyright 2012 the v8-i18n authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#import os
#import sys

#script_dir = os.path.dirname(__file__)
#rivertrail_root = os.path.normpath(os.path.join(script_dir, os.pardir))

#if __name__ == '__main__':
 # os.chdir(rivertrail_root)
 # script_dir = os.path.dirname(__file__)
 # rivertrail_root = '.'

#sys.path.insert(0, os.path.join(rivertrail_root, 'build', 'gyp', 'pylib'))
import gyp

args = []
rivertrail_root='rivertrail.gyp'
# Points to the parent of the src folder, in this case, project root.
args.append('--depth=' + rivertrail_root)

# Include some gypi files.
#args.append('-I' + os.path.join(rivertrail_root, 'build', 'common.gypi'))

# Necessary for building standalone v8 project.
#args.append('-I' + os.path.join(rivertrail_root, '..', 'v8', 'build', 'standalone.gypi'))

# Point to v8 and icu checkouts.
#args.append('-Dicu_path=' + os.path.join(rivertrail_root, '..', '..', 'icu'))
#args.append('-Dv8_path=' + os.path.join(rivertrail_root, '..', '..'))
#args.append('-Dclang=1')

# ICU build fails if werror is on.
#args.append('-Dwerror=')

# Process unittest.gyp file.
#args.append(os.path.join(rivertrail_root, 'build','unittest.gyp'))

print 'Generating project files from gyp rules...'

status = gyp.main(args)
if  status != 0:
  print 'Error running gyp.'
  sys.exit(status)
