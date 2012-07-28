// Copyright 2012 the rivertrail authors.


#include "../include/extension.h"
#include "natives.h"


namespace rivertrail {

Extension* Extension::extension_ = NULL;

Extension::Extension()
    : v8::Extension("rivertrail", Natives::GetScriptSource()) {
}

v8::Handle<v8::FunctionTemplate> Extension::GetNativeFunction(
    v8::Handle<v8::String> name) {/*
  if (name->Equals(v8::String::New("NativeJSLocale"))) {
    return v8::FunctionTemplate::New(Locale::JSLocale);
  } else if (name->Equals(v8::String::New("NativeJSBreakIterator"))) {
    return v8::FunctionTemplate::New(BreakIterator::JSBreakIterator);
  } else if (name->Equals(v8::String::New("NativeJSCollator"))) {
    return v8::FunctionTemplate::New(Collator::JSCollator);
  } else if (name->Equals(v8::String::New("NativeJSDateTimeFormat"))) {
    return v8::FunctionTemplate::New(DateTimeFormat::JSDateTimeFormat);
  } else if (name->Equals(v8::String::New("NativeJSNumberFormat"))) {
    return v8::FunctionTemplate::New(NumberFormat::JSNumberFormat);
  } else if (name->Equals(v8::String::New("NativeJSCanonicalizeLanguageTag"))) {
    return v8::FunctionTemplate::New(JSCanonicalizeLanguageTag);
  } else if (name->Equals(v8::String::New("NativeJSAvailableLocalesOf"))) {
    return v8::FunctionTemplate::New(JSAvailableLocalesOf);
  } else if (name->Equals(v8::String::New("NativeJSCreateDateTimeFormat"))) {
    return v8::FunctionTemplate::New(IntlDateFormat::JSCreateDateTimeFormat);
  } else if (name->Equals(v8::String::New("NativeJSInternalDateFormat"))) {
    return v8::FunctionTemplate::New(IntlDateFormat::JSInternalFormat);
  } else if (name->Equals(v8::String::New("NativeJSCreateNumberFormat"))) {
    return v8::FunctionTemplate::New(IntlNumberFormat::JSCreateNumberFormat);
  } else if (name->Equals(v8::String::New("NativeJSInternalNumberFormat"))) {
    return v8::FunctionTemplate::New(IntlNumberFormat::JSInternalFormat);
  } else if (name->Equals(v8::String::New("NativeJSCreateCollator"))) {
    return v8::FunctionTemplate::New(IntlCollator::JSCreateCollator);
  } else if (name->Equals(v8::String::New("NativeJSInternalCompare"))) {
    return v8::FunctionTemplate::New(IntlCollator::JSInternalCompare);
  } else if (name->Equals(v8::String::New("NativeJSCreateBreakIterator"))) {
    return v8::FunctionTemplate::New(IntlBreakIterator::JSCreateBreakIterator);
  } else if (name->Equals(v8::String::New("NativeJSBreakIteratorAdoptText"))) {
    return v8::FunctionTemplate::New(
	IntlBreakIterator::JSInternalBreakIteratorAdoptText);
  } else if (name->Equals(v8::String::New("NativeJSBreakIteratorFirst"))) {
    return v8::FunctionTemplate::New(
        IntlBreakIterator::JSInternalBreakIteratorFirst);
  } else if (name->Equals(v8::String::New("NativeJSBreakIteratorNext"))) {
    return v8::FunctionTemplate::New(
        IntlBreakIterator::JSInternalBreakIteratorNext);
  } else if (name->Equals(v8::String::New("NativeJSBreakIteratorCurrent"))) {
    return v8::FunctionTemplate::New(
        IntlBreakIterator::JSInternalBreakIteratorCurrent);
  } else if (name->Equals(v8::String::New("NativeJSBreakIteratorBreakType"))) {
    return v8::FunctionTemplate::New(
	IntlBreakIterator::JSInternalBreakIteratorBreakType);
  }*/

  return v8::Handle<v8::FunctionTemplate>();
}

Extension* Extension::get() {
  if (!extension_) {
    extension_ = new Extension();
  }
  return extension_;
}

void Extension::Register() {
  static v8::DeclareExtension extension_declaration(Extension::get());
}

}  // namespace rivertrail
