{
  "targets": [
    {
      "target_name": "node_aes_gcm",
      "sources": [
        "src/node-aes-gcm.cc"
      ],
      'conditions': [
        [ 'OS=="win"', {
          'conditions': [
            # "openssl_root" is the directory on Windows of the OpenSSL files
            ['target_arch=="x64"', {
            'libraries': ['<(module_root_dir)/src/libcrypto_static.lib'],
                } 
            ],
          ],
          'defines': [
            'uint=unsigned int',
          ],
          'include_dirs': [
            '<(module_root_dir)/src/include',
            '<!(node -e "require(\'nan\')")',
          ],
        }, { # OS!="win"
          'include_dirs': [
            # use node's bundled openssl headers on Unix platforms
            '<(node_root_dir)/deps/openssl/openssl/include',
            '<!(node -e "require(\'nan\')")',
          ],
        }],
      ],
    }
  ]
}
