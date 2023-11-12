import time
import subprocess

from pathlib import Path

from lib_not_dr.nuitka.compile import CompilerHelper
from lib_not_dr.types.version import Version


def gen_compiler() -> CompilerHelper:
    compiler = CompilerHelper(
        src_file=Path("QtEasyDesigner.py"),
        use_clang=True,
        use_msvc=True,
        use_mingw=False,
        use_lto=True,
        standalone=True,
        show_progress=False,
        # icon_path=Path("QtEasyDesigner.icns"),
        follow_import=[],
        include_packages=['qt_esay_model'],
        include_data_dir=[['resources', 'resources']],
        enable_plugin=[
            "pyside6"
        ]
    )
    return compiler


if __name__ == '__main__':
    
    compiler = gen_compiler()
    
    print(compiler.as_markdown())
    
    print(compiler.gen_subprocess_cmd())
    
    if input("Continue? (y/n) ").lower() != "y":
        exit(1)
    
    start_time = time.time()
        
    subprocess.run(compiler.gen_subprocess_cmd(), shell=True)
    
    stop_time = time.time()
    
    print(f"Time: {stop_time - start_time}")
