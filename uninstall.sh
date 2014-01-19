#!/bin/bash

if [ "$(whoami)" != "root" ]; then
echo "Error: you need to be root to uninstall stringgenerator"
  exit 1
fi

echo -e "Removing StringGenerator file...\n"
rm -r /opt/strgen/
rm /usr/local/bin/stringgenerator

echo "Uninstalling finished."
