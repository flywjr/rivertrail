#!/usr/bin/env python
#
# Copyright 2012 the rivertrail authors.
#

# This is a utility for converting RIVERTRAIL JavaScript source code into C-style
# char arrays. It is used for embedded JavaScript code in the V8
# library.

import os, re, sys, string


def ToCArray(lines):
  result = []
  for chr in lines:
    value = ord(chr)
    assert value < 128
    result.append(str(value))
  result.append("0")
  return ", ".join(result)


def RemoveCommentsAndTrailingWhitespace(lines):
  lines = re.sub(r'//.*\n', '\n', lines) # end-of-line comments
  lines = re.sub(re.compile(r'/\*.*?\*/', re.DOTALL), '', lines) # comments.
  lines = re.sub(r'\s+\n+', '\n', lines) # trailing whitespace
  return lines


def ReadFile(filename):
  file = open(filename, "rt")
  try:
    lines = file.read()
  finally:
    file.close()
  return lines


EVAL_PATTERN = re.compile(r'\beval\s*\(');
WITH_PATTERN = re.compile(r'\bwith\s*\(');


def Validate(lines, file):
  lines = RemoveCommentsAndTrailingWhitespace(lines)
  # Because of simplified context setup, eval and with is not
  # allowed in the natives files.
  eval_match = EVAL_PATTERN.search(lines)
  if eval_match:
    raise ("Eval disallowed in natives: %s" % file)
  with_match = WITH_PATTERN.search(lines)
  if with_match:
    raise ("With statements disallowed in natives: %s" % file)


HEADER_TEMPLATE = """\
// Copyright 2011 Google Inc. All Rights Reserved.

// This file was generated from .js source files by gyp.  If you
// want to make changes to this file you should either change the
// javascript source files or the tools/js2c.py script.

#include "../src/natives.h"

namespace rivertrail {

// static
const char* Natives::GetScriptSource() {
  // JavaScript source gets injected here.
  static const char api_source[] = {%s};

  return api_source;
}

}  // rivertrail
"""


def JS2C(source_files, target_file):
  all_lines = []
  for source in source_files:
    filename = str(source)
    lines = ReadFile(filename)
    Validate(lines, filename)
    all_lines.extend(lines)
  data = ToCArray(all_lines)

  # Emit result
  output = open(target_file, "w")
  output.write(HEADER_TEMPLATE % data)
  output.close()


def main():
  target_file = sys.argv[1]
  source_files = sys.argv[2:]
  JS2C(source_files, target_file)


if __name__ == "__main__":
  main()
