// Copyright 2011 the rivertrail authors.
//
#ifndef RIVERTRAIL_SRC_NATIVES_H_
#define RIVERTRAIL_SRC_NATIVES_H_

namespace rivertrail {

class Natives {
 public:
  // Gets script source from generated file.
  // Source is statically allocated string.
  static const char* GetScriptSource();
};

}  // namespace rivertrail

#endif  // RIVERTRAIL_SRC_NATIVES_H_
