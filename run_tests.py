import subprocess
import time
import signal
import os

def start_appium():
    return subprocess.Popen(
        ["appium"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        preexec_fn=os.setsid  # Allows killing the entire process group
    )

def stop_appium(process):
    try:
        os.killpg(os.getpgid(process.pid), signal.SIGTERM)
    except ProcessLookupError:
        print("Appium process already stopped.")

if __name__ == '__main__':
    appium_process = start_appium()
    time.sleep(10)  # ✅ Allow time for Appium to be ready

    print("🧪 Running tests...")
    subprocess.run([
        "pytest", "tests",
        "--html=reports/report.html",
        "--self-contained-html",
        "--capture=tee-sys",
        "--maxfail=5", "-v"
    ])

    stop_appium(appium_process)
    print("✅ Done! Check the report at: reports/report.html")
