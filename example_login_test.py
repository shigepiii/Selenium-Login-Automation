# Example

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
---
