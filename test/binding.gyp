{
  'targets': [
    {
      'target_name': 'struct_tests',
      'sources': [ 'struct_tests.cc' ],
      'include_dirs': [
        '<!(node -e "require(\'nan\')")',
        '<!(node -e "require(\'electron-updater-tools\')")'
      ],
      'target_conditions': [
        [ 'OS=="win"', {
            'libraries': [
              '-lShlwapi.lib'
            ],
            'msvs_settings': {
                'VCLinkerTool': {
                    'DelayLoadDLLs': [ 'node.dll', 'iojs.exe', 'node.exe' ],
                    # Don't print a linker warning when no imports from either .exe
                    # are used.
                    'AdditionalOptions': [ '/ignore:4199' ],
                },
            },
        }]
      ]
    }
  ]
}
