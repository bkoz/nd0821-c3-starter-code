#!/bin/bash
#
# Cleanup temporary files
#
rm -f starter/screenshots/*.png
rm -f starter/models/*.pkl
find . -name "__pycache__" -type d -exec rm -rf {} \;