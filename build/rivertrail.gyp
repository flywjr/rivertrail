

{
  'variables': {
    # gyp_chromium script can be found in chromium project.
    'v8_path%': '../../..',
  },
  'targets': [
    {
      'target_name': 'rivertrail',
      'type': 'static_library',
      'sources': [
        '../include/extension.h',
        '../src/extension.cpp',
        '../src/natives.h', 
		'../src/interface.h',
		'../src/interface.cpp',
        '<(SHARED_INTERMEDIATE_DIR)/rivertrail-js.cc',
      ],
      'include_dirs': [
        '..',
        '<(v8_path)',
      ],
      'dependencies': [
        '<(v8_path)/v8/tools/gyp/v8.gyp:v8',
        'api3c#host',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '../..',
        ],
      },
    },
    {
      'target_name': 'api3c',
      'type': 'none',
      'toolsets': ['host'],
      'variables': {
        'js_files': [
          '../src/test.js',
        ],
      },
      'actions': [
        {
          'action_name': 'api3c',
          'inputs': [
            '../tools/js2c.py',
            '<@(js_files)',
          ],
          'outputs': [
            '<(SHARED_INTERMEDIATE_DIR)/rivertrail-js.cc',
          ],
          'action': [
            'python',
            '../tools/js2c.py',
            '<@(_outputs)',
            '<@(js_files)'
          ],
        },
      ],
    },
  ],  # targets
}
