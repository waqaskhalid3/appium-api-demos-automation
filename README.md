# Appium API Demos Test Suite

## 🧰 Environment Setup

- ✅ Install Android Studio & set up an emulator
- ✅ Install Java 17 and set `JAVA_HOME`
- ✅ Install Node.js and Appium:
  ```bash
  npm install -g appium
  ```
- ✅ Install Python test runner and HTML report plugin:
  ```bash
  pip install pytest pytest-html
  ```
- ✅ Install additional Python dependencies:
  ```bash
  pip install -r requirements.txt
  ```

---

## 📦 How to Build and Install the App

- Make sure your **Android Emulator is running**
- Run:
  ```bash
  npm install
  npm run build
  ```
- Install the APK:
  ```bash
  adb install -r ./apks/ApiDemos-debug.apk
  ```

---

## ⚙️ Pre-requisites

- Replace `PATH_TO_YOUR_APK` in `appium_driver.py` with the actual APK path:
  ```python
  app = '/absolute/path/to/apks/ApiDemos-debug.apk'
  ```
- Launch the emulator **via Android Studio or CLI** before running tests
- Start Appium in a separate terminal:
  ```bash
  appium
  ```

---

## 🧪 How to Execute Tests

### 🐚 Using Shell Script

- Make `run_tests.sh` executable:
  ```bash
  chmod +x run_tests.sh
  ```
- Then run:
  ```bash
  ./run_tests.sh
  ```

### 🐍 Using Python

- Execute:
  ```bash
  python run_tests.py
  ```

---

## 📁 Artifacts

- 📸 Screenshots (on failure): `./screenshots/`
- 📄 Logs per test case: `./logs/`
- 📊 HTML Report: `./reports/report.html`

---

## ✅ Final Flow Summary

| **Test Step**       | **In-App Flow**                                                    |
|---------------------|--------------------------------------------------------------------|
| Launch app          | App launch                                                         |
| Product list        | Navigate to `Views → Expandable Lists → Custom Adapter`            |
| Select item         | Tap `"People Names"` → Validate the group expands                  |
| Simulate cart       | Validate child item appears (e.g., `"Arnold"`)                     |
| Checkout            | Navigate to `Views → Controls → 2. Light Theme`                    |
| Order confirm       | Fill form controls and assert submission (simulate confirmation)   |


## 🔗 Useful Commands

- Run a specific test:
  ```bash
  pytest tests/test_launch_app.py
  ```
- Check if Appium is running:
  ```bash
  lsof -i :4723
  ```

---

## 📌 Notes

- This suite maps e-commerce app scenarios to the API Demos app
- You may extend `test_*.py` files with more validations or Appium features like gestures, waits, etc.
