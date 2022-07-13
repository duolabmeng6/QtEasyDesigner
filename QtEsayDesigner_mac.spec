# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['QtEsayDesigner.py'],
    pathex=[],
    binaries=[],
    datas=[('qt_esay_model', 'qt_esay_model/'), ('resources', 'resources/'), ('qtefun', 'qtefun/'), ('pyefun/pyefun', 'pyefun/')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['.git'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='QtEsayDesigner',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='QtEsayDesigner.icns',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='QtEsayDesigner',
)
app = BUNDLE(
    coll,
    name='QtEsayDesigner.app',
    icon='QtEsayDesigner.icns',
    bundle_identifier=None,
)
