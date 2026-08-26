name: Build APK
on: [push]
jobs:
  build:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - name: Install deps
        run: |
          sudo apt update
          sudo apt install -y openjdk-17-jdk zip unzip libffi-dev libssl-dev
          pip install buildozer cython==0.29.36

      - name: Accept All Android Licenses
        run: |
          mkdir -p ~/.buildozer/android/platform/android-sdk/licenses
          echo "8933bad161af4178b1185d1a37fbf41ea5269c55" > ~/.buildozer/android/platform/android-sdk/licenses/android-sdk-license
          echo "d56f5187479451eabf01fb78af6dfcb131a6481e" >> ~/.buildozer/android/platform/android-sdk/licenses/android-sdk-license
          echo "24333f8a63b6825ea9c5514f83c1059b8ea73142" >> ~/.buildozer/android/platform/android-sdk/licenses/android-sdk-license
          echo "y" > ~/.buildozer/android/platform/android-sdk/licenses/android-sdk-preview-license
          echo "y" >> ~/.buildozer/android/platform/android-sdk/licenses/android-sdk-preview-license

      - name: Build APK
        run: buildozer android debug

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: apk-stela
          path: bin/*.apk
