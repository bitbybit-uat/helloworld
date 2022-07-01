# helloworld
Hello World program in Python

Clone this project to see a basic project, written in Python, which will output 'Hello World' to the terminal

# Installing Git
To install the git command-line interface (CLI) on a Windows machine:
- If you have Chocolatey installed (which you can do [here](https://chocolatey.org/install#individual), type this in a PowerShell or command line window:
```
choco install -y git
```
- If you have the [winget](https://docs.microsoft.com/en-us/windows/package-manager/winget/) tool installed, type this in a PowerShell or command line window:
```
winget installed --id Git.Git -e --source winget
```
- If you want to be a pleb and just install git via GUI, click [here](https://github.com/git-for-windows/git/releases/download/v2.37.0.windows.1/Git-2.37.0-64-bit.exe)

To install the git command-line interface (CLI) on a MacOS machine:
- If you have homebrew insatlled (which you can do [here](brew.sh), type this in a Terminal window (or your favorite terminal emulator):
```
brew install git
```
- If you have MacPorts installed (which you can do [here](https://guide.macports.org/chunked/installing.macports.html), type this in a Terminal window (or your favorite terminal emulator:
```
sudo port install git
```
- MacOS may automatically run a GUI git install if you type ```git``` in Terminal
- If you want to be a pleb and just install git via GUI, click [here](https://sourceforge.net/projects/git-osx-installer/files/latest/download)

To install the git command-line interface (CLI) on a Linux machine
- If you are on Fedora or any of its children (RHEL, CentOS, etc.), type the following in a terminal:
```
sudo dnf install git-all
```
- If you are on Debian or any of its children (Ubuntu, Parrot OS, etc.), type the following in a terminal:
```
sudo apt install git-all
```
- If you are on Arch or any of its children (Manjaro, Anarchy, etc.), type the following in a terminal:
```
sudo pacman -S git
```
- For other distributions of Linx or other Unix-based systems, install git via instructions found [here](https://git-scm.com/download/linux)

To clone this project, use
```
git clone https://github.com/bitbybit-uat/helloworld.git
```

# Ensure you have python insatlled
- On Windows, type this in a PowerShell or command line window:
`python -V` or `python --version`
- On MacOS or Linux, type this in a Terminal window (or you favorite terminal emulator):
`python3 -V` or `python3 --version`
If those commands don't return a version or return an error, you can find a complete guide on installing Python on your machine [here](https://realpython.com/installing-python/)

# Running the project
Change directory into the **helloworld** directory
```
cd helloworld
```
- If you are on Windows, type the following in the **helloworld** directory:
```
python helloworld.py
```
- If you are on MacOS or Linux, type the following in the **helloworld** directory:
```
python3 helloworld.py
```

# Enjoy!!
