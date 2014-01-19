#!/bin/bash

if [ "$(whoami)" != "root" ]; then
  echo "Error: you need to be root to install stringgenerator"
  exit 1
fi

echo "Creating StringGenerator directory..."
mkdir /opt/strgen
cp -r * /opt/strgen

echo "Installation StringGenerator..."
chmod +x /opt/strgen/main.py
ln -s /opt/strgen/main.py /usr/local/bin/stringgenerator

echo -e "Removing install.sh file...\n"
rm /opt/strgen/install.sh

echo "Installation finished. Type stringgenerator --help"
