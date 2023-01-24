#!/bin/bash
#
# Clean up files created by performing package builds.
#

# Simple helper function to check if there are any instances of a wild card preceeded file type.
# This helps us check if various compiled files when doing our cleanup.
shopt -s nullglob
function have_any () {
    [ $# -gt 0 ]
}

# Clean up any generated build files.
if [ -d ../deploy ]; then
    echo "Removing existing deployment directory."
    rm -rf ../deploy
fi

# Clean up any remaining artifacts.
if [ -d rpms ]; then
    echo "Removing existing build artifacts."
    rm -rf rpms
fi
