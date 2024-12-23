

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

 bash  git clone https://github.com/yourusername/web-application-login-automation.git  cd web-application-login-automation  
 
このコマンドでリポジトリをローカルにクローンし、プロジェクトディレクトリに移動します。


2, Create a virtual environment and activate it（仮想環境を作成し、有効にします）:

bash  python -m venv env  source env/bin/activate  # For Windows: env\Scripts\activate 

仮想環境を作成して有効化します。Windowsではコマンドが異なりますので、注意してください。



3, Install the required packages（必要なパッケージをインストールします）:

 bash  pip install -r requirements.txt 
 
このコマンドでプロジェクトに必要なパッケージをインストールします。






**Usage**

1, Open login_test.py and update the URL, username, and password variables with your web application’s login details.

login_test.py を開き、URL、username、password 変数に自分のウェブアプリケーションのログイン情報を入力します。



2, Run the test script（テストスクリプトを実行します）:

 bash  python login_test.py  
 
このコマンドでテストを実行します。


3. Check the test results in the terminal（結果をターミナルで確認します）。



   


**Example**

from selenium import webdriver  # Import WebDriver module
from selenium.webdriver.common.by import By  # For locating elements by specific criteria
from selenium.webdriver.common.keys import Keys  # To simulate keyboard inputs
import time  # To add delays for demonstration purposes

# Configure WebDriver
driver = webdriver.Chrome()  # Use Chrome WebDriver (Alternatively, you can use Firefox)
# WebDriverの設定
# Chromeを使用します（Firefoxを使用する場合はwebdriver.Firefox()を使用）

# Navigate to the login page
driver.get("https://example.com/login")
# ログインページに移動

# Locate and fill in the login form
username_input = driver.find_element(By.NAME, "username")  # Find the username field
password_input = driver.find_element(By.NAME, "password")  # Find the password field
login_button = driver.find_element(By.NAME, "login")  # Find the login button
# ログインフォームを見つけて入力フィールドを特定

username_input.send_keys("testuser")  # Input the username
password_input.send_keys("password123")  # Input the password
login_button.click()  # Click the login button
# ユーザー名とパスワードを入力し、ログインボタンをクリック

# Wait for the result
time.sleep(5)  # Pause to let the page load
# 結果が表示されるまで5秒待機

# Check for successful login
if "Welcome" in driver.page_source:  # Check if "Welcome" is present in the page source
  print("Login successful")
else:
  print("Login failed")
# ログイン成功を確認 ("Welcome"がページ内に表示されているかをチェック)

# Close the browser
driver.quit()
# ブラウザを閉じる
