#!/bin/bash

echo "🚀 Starting Appium server..."
appium > appium.log 2>&1 &

APPIUM_PID=$!

# Wait for Appium to be ready
echo "⏳ Waiting for Appium to be ready..."
sleep 5

# Test if Appium is up
curl -s http://127.0.0.1:4723 > /dev/null
if [ $? -ne 0 ]; then
    echo "❌ Appium server failed to start. Check appium.log for details."
    kill $APPIUM_PID
    exit 1
fi

echo "✅ Appium is running. Starting tests..."

python3 run_tests.py

echo "🛑 Stopping Appium server..."
kill $APPIUM_PID

echo "✅ Done! Check the report at: reports/report.html"
