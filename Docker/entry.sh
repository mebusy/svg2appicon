#!/bin/sh
cp -f /opt/res/* /opt/svg2appicon/
python svg2appicon.py "$@"

