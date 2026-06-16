#!/usr/bin/env bash
set -euo pipefail

echo "Running ShippingApp for multiple orders..."
echo

for id in 1001 1002 1003; do
    echo "============================"
    echo "Running order ID: $id"
    echo "============================"

    python3 -m legacy_code.src.ShippingApp "$id"

    echo
done

echo "Done."
read -rp "Press Enter to continue..."
