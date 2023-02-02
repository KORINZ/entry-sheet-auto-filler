# Entry Sheet Auto Filler (エントリーシートオートフィラー) v1.2.0
Automatically filling entry sheet with personal information. Powered by Selenium 4.

### Note
Ocansionally, `NoSuchElementException` will raise due to the customization of the entry sheet. Revise the code accordingly.

### Prerequisite
selenium 4.8.0
```
pip install selenium
```
webdriver-manager 3.8.5
```
pip install webdriver-manager
```
### Currently Supported Websites
1. snar.jp (採用管理システムsonar ATS): ***PATH format**: `https://...-recruit.snar.jp/`*
2. axol.jp (株式会社マイナビ): ***PATH format**: `https://job.axol.jp/.../entry/agreement`*

### Working on Progress
1. i-webs.jp (株式会社ヒューマネージ): ***PATH format**: `https://mypage.....i-webs.jp/.../applicant/.../entrycd/`*
