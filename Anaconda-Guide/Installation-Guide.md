# Anaconda Installation Guide

# Installing On Linux:

1. Download [Anaconda installer for Linux](https://docs.anaconda.com/anaconda/install/linux)
2. + Enter the following to install Anaconda for Python 3.6:
```bash
  bash ~/dirname/Anaconda3-5.0.1-Linux-x86_64.sh
```
+ Or Enter the following to install Anaconda for Python 2.7:
```bash
  bash ~/dirname/Anaconda2-5.0.1-Linux-x86_64.sh
```
* Note: replace ~/dirname/ with the path to the file you downloaded.
3. The installer prompts “In order to continue the installation process, please review the license agreement.” Click Enter to view license terms. Scroll to the bottom of the license terms and enter “Yes” to agree.
4. The installer prompts you to click Enter to accept the default install location, CTRL-C to cancel the installation, or specify an alternate installation directory. If you accept the default install location, the installer displays “```PREFIX=/home/<user>/anaconda<2 or 3>```” and continues the installation. It may take a few minutes to complete
5. The installer prompts “Do you wish the installer to prepend the Anaconda 2 or 3  install location to PATH in your ```/home/<user>/.bashrc ?```” Enter Yes.
6. The installer finishes and displays “Thank you for installing Anaconda 2 or 3 !”
7. Close and open your terminal window for the installation to take effect, or you can enter the command source ```~/.bashrc.```
8. After your install is complete, verify it by opening Anaconda Navigator, a program that is included with Anaconda: Open a Terminal window and type ```anaconda-navigator```. If Navigator opens, you have successfully installed Anaconda
