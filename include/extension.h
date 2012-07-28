// Copyright 2012 the rivertrail autheors.
//

#ifndef RIVERTRAIL_INCLUDE_EXTENSION_H_
#define RIVERTRAIL_INCLUDE_EXTENSION_H_

#include "v8/include/v8.h"

namespace rivertrail {

class Extension : public v8::Extension {
 public:
  Extension();

  virtual v8::Handle<v8::FunctionTemplate> GetNativeFunction(
      v8::Handle<v8::String> name);

  // V8 code prefers Register, while Chrome and WebKit use get kind of methods.
  static void Register();
  static Extension* get();

 private:
  static Extension* extension_;
};

}  // namespace rivertrail

#endif  // RIVERTRAIL_INCLUDE_EXTENSION_H_
