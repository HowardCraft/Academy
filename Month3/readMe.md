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

