# -*- coding: utf-8 -*-
"""PyInstaller 打包配置：拼多多运营助手（文件夹模式）。

源布局：业务代码在 _internal/app/ 下（exe 同级），
依赖（customtkinter / PIL / numpy / win32 / openpyxl）在 _internal/ 下。
打包后 _internal/ 内容随 exe 一起分发，运行期不向系统临时目录解压。
"""
import os

SPECPATH = os.path.dirname(os.path.abspath(SPEC))
SRC = os.path.join(SPECPATH, "_internal")

a = Analysis(
    [os.path.join(SRC, "app", "main.py")],
    pathex=[SRC],
    binaries=[],
    datas=[],
    hiddenimports=[
        "PIL.Image", "PIL.ImageDraw", "PIL.ImageFont",
        "darkdetect", "windnd",
        "openpyxl", "openpyxl.styles", "openpyxl.utils",
        "et_xmlfile",
        "customtkinter.windows.widgets.core_rendering.draw_engine",
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        "matplotlib", "scipy", "pandas", "PyQt5", "PySide2", "PySide6",
        "tkinter.test", "pytest", "IPython", "notebook", "sqlite3",
        "test", "unittest", "lib2to3", "idlelib", "turtledemo",
    ],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="拼多多运营助手",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=["python313.dll", "python3.dll", "*.pyd"],
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=os.path.join(SPECPATH, "app.ico"),
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name="拼多多运营助手",
)
