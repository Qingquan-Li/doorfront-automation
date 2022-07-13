doorfront-automation: Automatically walk in Google Street View and take screenshots.

# How to run the program?

## 1. Run the DoorFront-Automation-Map website locally

DoorFront-Automation-Map website source code:
https://github.com/Qingquan-Li/DoorFront-Automation-Map

You can run the website by following the steps in [source code - README.md](https://github.com/Qingquan-Li/DoorFront-Automation-Map/blob/main/README.md).

After finishing this step, the website will be running on your browser(address is http://localhost:3000/), then you can continue the below steps to control this website automatically.

## 2. Download the source code

Source code: https://github.com/Qingquan-Li/doorfront-automation/archive/refs/heads/main.zip

You can open the code with [VS Code](https://code.visualstudio.com/) or other IDEs.

## 3. Install Python3 and pip

How to install: https://www.python.org/downloads/

`pip` (a package installer for Python) is installed when you install Python3.

## 4. Install the required libraries

3.1 Install [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/index.html), enter the following command in the terminal:

```bash
pip install pyautogui
```

If you cannot run the command above on Windows, please try the commands below:

```bash
# Rollback pip to an older version:
python -m pip install pip==18.1

# Install desired module:
pip install pyautogui

# Update pip:
python -m pip install --upgrade pip
```

3.2 Install Pillow, enter the following command in the terminal:

```bash
pip install Pillow
```

## 5. Adjust some parameters in the code

First, drag Google Street View to make the map show one side of the street, so you can capture the doors of the building when you take screenshots.

Second, open the `src/go.py` file, change some parameters as prompted in that code file.

## 6. Automate the google street view and take screenshots

First, open the DoorFront-Automation-Map website locally, we have already completed this step in first step.

Second, put your mouse cursor over the forward arrow of Google Street View.

Third, run this command in this project root directory:

```bash
python src/go.py
```

🎉 Now you can finally automate the Google Street View and take screenshots!
