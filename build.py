import os
import shutil
import subprocess
from pathlib import Path
from shlex import split
from textwrap import dedent

this_dir = Path(__file__).resolve().parent
os.chdir(this_dir)

target_dir = "dist"


def npm_run_build():
    return subprocess.run(
        split("npm run build"),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        encoding="utf-8",
    )


def prepend_license(path):
    content = Path(path).read_text()
    content = (
        dedent(
            """\
            @charset "UTF-8";/*!
            * Bootstrap-xlwings v5.2.3-2
            * Copyright 2023 Zoomer Analytics GmbH
            * Licensed under MIT
            * Based on Bootstrap
            *//*!
            * Bootstrap v5.2.3 (https://getbootstrap.com/)
            * Copyright 2011-2022 The Bootstrap Authors
            * Copyright 2011-2022 Twitter, Inc.
            * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
            */"""
        )
        + content
    )
    Path(path).write_text(content)


def build():
    # Clear
    if Path(target_dir).exists():
        shutil.rmtree(target_dir)

    # Minified build
    print(npm_run_build())
    prepend_license(f"{target_dir}/bootstrap-xlwings.css")
    os.rename(f"{target_dir}/bootstrap-xlwings.css", f"{target_dir}/bootstrap-xlwings.min.css")
    content = Path(f"{target_dir}/bootstrap-xlwings.min.css").read_text()
    content = content.replace('bootstrap-xlwings.css.map', 'bootstrap-xlwings.min.css.map')
    Path(f"{target_dir}/bootstrap-xlwings.min.css").write_text(content)
    os.rename(f"{target_dir}/bootstrap-xlwings.css.map", f"{target_dir}/bootstrap-xlwings.min.css.map")


if __name__ == "__main__":
    build()
