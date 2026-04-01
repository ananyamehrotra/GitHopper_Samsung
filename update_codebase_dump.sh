#!/bin/bash
# GitHopper Codebase Dumper - Unix/Linux/macOS Script
# Run this file to automatically update CODEBASE_DUMP.md

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║   GitHopper Codebase Dumper                                ║"
echo "║   Consolidating entire codebase...                        ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed"
    echo "Please install Python 3.8+ and try again"
    exit 1
fi

# Run the dumper script
echo "🔄 Running codebase dumper..."
echo ""
python3 codebase_dumper.py

if [ $? -ne 0 ]; then
    echo ""
    echo "❌ Dumper failed!"
    exit 1
fi

echo ""
echo "✅ Codebase dump completed!"
echo "📄 Output file: CODEBASE_DUMP.md"
echo ""
echo "You can now view the complete codebase in CODEBASE_DUMP.md"
echo ""
