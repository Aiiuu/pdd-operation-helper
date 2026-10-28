# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['D:/拼多多运营助手/_internal/app/main.py'],
    pathex=['D:/拼多多运营助手/_internal'],
    binaries=[],
    datas=[],
    hiddenimports=['PIL.Image', 'PIL.ImageDraw', 'PIL.ImageFont', 'windnd', 'windnd.windnd', 'openpyxl', 'openpyxl.styles', 'openpyxl.utils', 'pywin32', 'win32api', 'win32gui', 'win32con', 'pywintypes', 'customtkinter.windows.widgets.core_rendering.draw_engine'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='pdd_probe',
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
    icon=['D:/拼多多运营助手/app.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='pdd_probe',
)
