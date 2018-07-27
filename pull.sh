#!/bin/sh

echo "===== Downloading roundup sources ====="
hg clone -q https://hg.python.org/tracker/roundup tracker/roundup
(
    cd tracker/roundup
    hg up -q bugs.python.org
)

echo "===== Downloading python-dev sources ====="
hg clone -q https://hg.python.org/tracker/python-dev tracker/python-dev
(
    cd tracker/python-dev
    mkdir db
    cp config.ini.template config.ini
    cp detectors/config.ini.template detectors/config.ini
)

echo "===== All downloads finished successfully ====="
