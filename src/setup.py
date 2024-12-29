# Copyright (c) 2024 Riccardo Bean. All Rights Reserved.
# Unauthorized use, modification, or distribution of this software is prohibited.

import PyInstaller.__main__

PyInstaller.__main__.run([
    'main.py',
    '--onefile',
    '--noconsole',
    '--windowed',
    '--noupx',
    '--icon=assets/logo.ico'
])