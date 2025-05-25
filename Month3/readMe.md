FAQ:

# Q: How to Run `.sh` Files on Raspberry Pi

## why we have `.sh`?

Installing dependenices and libreries on Raspberry Pi can be a bit challenging, so we prepare `.sh` as much as possible to reduce the struggleing users with errors while instaling the files/libreries.

## What is a `.sh` file?

A `.sh` file is a **shell script** — a text file that contains a list of terminal commands. It’s often used to automate tasks like installing software or setting up your Raspberry Pi.

---

## How do I run a `.sh` file?

Follow these simple steps to run a `.sh` file on your Raspberry Pi:

### 1. Open the Terminal
Click the Terminal icon on your Raspberry Pi (it looks like a black screen with a `>_` symbol).

### 2. Navigate to the Folder
Use the `cd` command to change to the folder where your `.sh` file is located. Example:

```bash
cd Downloads
```

### 3. Make the Script Executable (only needed once)
Before running the script, give it permission to execute:

```bash
chmod +x yourscript.sh
```

Replace yourscript.sh with the name of your file.

### 4. Run the Script

```bash
./yourscript.sh
```

## Tips
Make sure the file ends in .sh

Always include ./ before the filename when running it

Read any error messages carefully — they usually help you understand what's missing or needs fixing




# Q: What is a virtual environment (venv) in Python?

A virtual environment is a **self-contained directory** that holds a specific Python version and any libraries or dependencies your project needs. It keeps your project isolated from other Python projects and from the system-wide Python installation.

---

## Q: Why are virtual environments important?

Here are a few reasons:

- ✅ **Avoid Conflicts**: Different projects may require different versions of the same package. `venv` keeps them separate.
- 🔒 **Safe Testing**: You can test libraries or code changes without affecting your main system.
- 📦 **Clean Dependency Management**: All dependencies for your project are kept in one place.
- 🚀 **Professional Standard**: Most modern Python workflows use virtual environments.

---

## Q: How do I create a virtual environment?

In your terminal, navigate to your project folder and run:

```bash
python3 -m venv venv
```

This will create a folder named `venv` containing the virtual environment.

---

## Q: How do I activate the virtual environment?

### On Raspberry Pi or Linux/macOS:

```bash
source venv/bin/activate
```

### On Windows (Command Prompt):

```cmd
venv\Scripts\activate
```

---

## Q: How do I know it's activated?

Once activated, your terminal prompt will change and show the name of the environment like this:

```bash
(venv) pi@raspberrypi:~/myproject $
```

---

## Q: How do I deactivate it?

To leave the virtual environment, just type:

```bash
deactivate
```

---

## Q: How do I reactivate the virtual environment later?

Just run the activation command again from your project folder:

```bash
source venv/bin/activate
```

---

## Q: What if I forget to activate it?

If you install packages without activating your virtual environment, they might be installed globally or in the wrong location. Always activate `venv` first before running or installing anything in your project.

---

## Bonus Tip: Install Packages in venv

After activating:

```bash
pip install package-name
```

All packages will be installed only inside the virtual environment.

---

Stay organized and safe with `venv`! 🐍🛡️
