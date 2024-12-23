

# Selenium Login Automation

**Overview**

This project demonstrates how to automate the testing of a web application’s login functionality using Selenium with Python. The goal is to ensure that the login functionality works correctly and to provide an example of how to use Selenium for browser automation.

このプロジェクトは、SeleniumとPythonを使用して、ウェブアプリケーションのログイン機能を自動化するテスト方法を示しています。目的は、ログイン機能が正しく動作することを確認し、Seleniumを使用したブラウザの自動化の例を提供することです。


**Features**

・Automated testing of login functionality（ログイン機能の自動化テスト）

・Verifies login success and failure scenarios（ログイン成功と失敗シナリオの検証）

・Supports configuration for different environments（異なる環境向けの設定サポート）


**Prerequisites**

Before you begin, ensure you have met the following requirements:

このプロジェクトを開始する前に、以下の要件を満たしていることを確認してください。


・Python 3.6 or higher （Python 3.6以上）

・Google Chrome or Mozilla Firefox installed（Google ChromeまたはMozilla Firefoxがインストールされていること）

・WebDriver for your browser (e.g., ChromeDriver or GeckoDriver)（使用するブラウザ用のWebDriver（例: ChromeDriverやGeckoDriver））


**Installation**

1, Clone the repository（リポジトリをクローンします）:

``` bash  git clone https://github.com/yourusername/Selenium-Login-Automation.git  cd Selenium-Login-Automation  ```
 
このコマンドでリポジトリをローカルにクローンし、プロジェクトディレクトリに移動します。


2, Create a virtual environment and activate it（仮想環境を作成し、有効にします）:

```bash  python -m venv env  source env/bin/activate ```
For Windows:
```env\Scripts\activate``` 

仮想環境を作成して有効化します。Windowsではコマンドが異なりますので、注意してください。



3, Install the required packages（必要なパッケージをインストールします）:

``` bash  pip install -r requirements.txt ```
 
このコマンドでプロジェクトに必要なパッケージをインストールします。

**Usage**

1, Open login_test.py and update the URL, username, and password variables with your web application’s login details.

login_test.py を開き、URL、username、password 変数に自分のウェブアプリケーションのログイン情報を入力します。



2, Run the test script（テストスクリプトを実行します）:

``` bash  python login_test.py  ```
 
このコマンドでテストを実行します。


3. Check the test results in the terminal（結果をターミナルで確認します）。

   
**Example**

```from selenium import webdriver  # Import WebDriver module（WebDriverモジュールをインポート）
from selenium.webdriver.common.by import By  # For locating elements by specific criteria（特定の基準で要素を探すため）
from selenium.webdriver.common.keys import Keys  # To simulate keyboard inputs（キーボード入力をシミュレート）
import time  # To add delays for demonstration purposes（デモンストレーション用に遅延を追加）

# Configure WebDriver（WebDriverの設定）
driver = webdriver.Chrome()  # Use Chrome WebDriver (Alternatively, you can use Firefox)（Chrome WebDriverを使用します。代わりにFirefoxを使用することもできます）

# Navigate to the login page（ログインページに移動）
driver.get("https://example.com/login")

# Locate and fill in the login form（ログインフォームを見つけて入力）
username_input = driver.find_element(By.NAME, "username")  # Find the username field（ユーザー名フィールドを見つけます）
password_input = driver.find_element(By.NAME, "password")  # Find the password field（パスワードフィールドを見つけます）
login_button = driver.find_element(By.NAME, "login")  # Find the login button（ログインボタンを見つけます）

# Input the username and password, then click login button（ユーザー名とパスワードを入力し、ログインボタンをクリック）
username_input.send_keys("testuser")  # Input the username（ユーザー名を入力）
password_input.send_keys("password123")  # Input the password（パスワードを入力）
login_button.click()  # Click the login button（ログインボタンをクリック）

# Wait for the result（結果が表示されるまで待機）
time.sleep(5)  # Pause to let the page load（ページの読み込みが完了するまで待機）

# Check for successful login（ログイン成功を確認）
if "Welcome" in driver.page_source:  # Check if "Welcome" is present in the page source（ページソースに「Welcome」が含まれているかを確認）
 print("Login successful")  # Print success message（成功メッセージを表示）
else:
 print("Login failed")  # Print failure message（失敗メッセージを表示）

# Close the browser（ブラウザを閉じる）
driver.quit()```
