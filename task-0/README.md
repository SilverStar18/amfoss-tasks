link to the [dev.to post](https://dev.to/silverstar18/install-ubuntu-20-04-lts-alongside-windows-10-in-dual-boot-136e)






# Install Ubuntu 20.04 LTS Alongside Windows 10 in Dual Boot

In this blog, I am going to share how to *install Ubuntu 20.04 LTS (latest) on Windows 10*. Although a lot of you might be aware of dual booting linux with windows 7. But its slightly differnet compared to the older versions as newer systems have **UEFI**, instead of **BIOS**. 

This is because of the **secure boot enabled** in UEFI that stops system from dual booting. So that will be the most important step in this process. I performed this task on my newly bought *Lenovo IdeaPad 3 15IIL05 i5 10th generation, RAM 8 GB, 256 SSD, 1 HDD, Intel Iris Plus Graphics*.

## Prerequisites 

- Ubuntu live USB (step-1)


## **Step - 1** Download Ubuntu ISO file
You can download the disk image (ISO file) for Ubuntu 20.04 LTS by clicking [here](https://ubuntu.com/download/desktop/thank-you?version=20.04.1&architecture=amd64)


## **Step - 2** Create Bootable USB stick
![Rufus](https://dev-to-uploads.s3.amazonaws.com/i/7i5v0i4dcxd65yksfv3d.png)
To create the live USB I have used **Rufus**. But you can also use **Universal USB Installer**. 
Select your USB stick to be formatted. 
Select the ubuntu iso image file. Since the file is only 2GB type of partition scheme does not matter (MBR or GPT). 
Click on Start. 


## **Step - 3** Create the Partition for Ubuntu
![Disk Partition](https://dev-to-uploads.s3.amazonaws.com/i/90oq7w38m6t0j0l2lfxr.png)
You can manage, resize or create partitions in ***Control Panel > System and Security > Administrative Tools > Create and format hard disk partition***.
I searched for **Create and format hard disk partition** in settings.
Shrink the size of the drive where we want to install Ubuntu (in this case **c:** drive).
Leave the free space as it is since we will create partitions at the time of install.


## **Step - 4** Disable Secure Boot
![advanced startup](https://dev-to-uploads.s3.amazonaws.com/i/wnorz1fozkfklusop22k.png)
Open UEFI settings by 
1. Search for **Change advanced startup options**
2. Go to **settings > Update and Security > Recovery**
3. Hold Shift while selecting *Restart*. There, I selected  *Restart now* in the **Advanced startup**. 
![Troubleshoot](https://dev-to-uploads.s3.amazonaws.com/i/z515ov380vbvwgorkdro.jpg)
Now we are presented with 4 set of options. Out of those choose **Troubleshoot**, then **Advanced options** and then **UEFI Firmware settings**. Now click on *Restart*.
Once Rebooted, disable **Secure Boot** in the **Security** tab. Save changes and Exit.


## **Step - 5** Boot with the USB
Now that I can start on actually installing Ubuntu. We can boot from a disk/USB by choosing **Use a device** in the same way as we selected Troubleshoot. At first, I couldnot find my USB, So I choose *EFI USB drive* Which gave me 2 options as the selected was not found. I chose **Linpus Lite** which turned out to be my Ubuntu live. 


## **Step - 6** Install Ubuntu
After a Filecheck, I was persented with 2 options; *Try Ubuntu* and *Install Ubuntu*. Select Install Ubuntu. I was presented with a screen to chose keyboard layout and Language. Once selected, click continue.
On the next window, I selected **Normal installation** as well as the 2 check boxes to download *update* and *Third Party Software*.
Next on Installation type, I selected *Something else* and made partitions using the free space we had created. 

I made 4 partitions using my 50gb space, namely : /boot(750mb), swap(8gb),/ (root)(34gb), /home(8gb). The 'use as' for all is *ext4 journaling file system*, except for swap that used *Swap area*.Click on 'Install now'.
The next window will ask you to create name password etc. ***Rmenber to note it down as once lost it cannot be recovered.*** once the installation is finished, reboot the computer and remove the usb when prompted.

**And thus we have finished installing Ubuntu in dual boot alongside Windows 10.**
![u-1](https://dev-to-uploads.s3.amazonaws.com/i/i7zmzu3md509ddiui3ml.png)
![u-2](https://dev-to-uploads.s3.amazonaws.com/i/lrggqwzxwd8lt3e7uz6v.png)
***Note:*** *Windows 10 comes with the WIndows Subsystem for Linux (WSL1) which allows us to use the same linux commands on windows by mapping the screen to linux. However as this was a task given club'AMFOSS', I decided to go about the normal way and install in dual boot.*
