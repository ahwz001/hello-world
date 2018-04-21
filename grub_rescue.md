# Grub Rescue修复方法

## 症状：
开机显示
`GRUB loading`
`error:unknow filesystem`
`grub rescue>`

## 原因：
已经发现下面几种操作会导致这种问题：
1. 想删除ubuntu，于是直接在windows下删除/格式化了ubuntu所在的分区。
2. 调整磁盘，利用工具合并/分割/调整/删除分区，使磁盘分区数目发生了变化。
3. 重新安装系统，把linux安装到了新分区，原有分区已经格式化，但是没有重新安装grub2。
4. 用ubuntu备份工具/衍生版制造工具等，把主分区回复成了8.X的老版本，结果老版本的grub是grub1,于是把grub2破坏掉了。

 总归，是由于操作者不知道grub2分为两部分，一部分（一般情况下）写在了mbr上，另一部分写在了某个分区的/boot/grub目录（如果/boot单独分区，则直接写在对应分区的/grub目录）里面。由于上述操作，致使grub2的mbr里面的那一部分找不到/grub目录里面的那一部分了（或者那一部分已经删除了）。
## 思路：
### 方法1 彻底删除grub2,让这个提示不再出现
1. 适用于已经不想再使用ubuntu，要转回windows的人。
这个很简单，只要你有Windows启动盘（非Ghost），用它启动，至选择安装位置，不用真正安装，退出重启就可以。
2. 或者用它启动到故障修复台，运行fixboot或者fixmbr都可以。
win7命令行下，则是执行：BootRec.exe /fixmbr
（/fixmbr修复mbr， /FixBoot修复启动扇区，/ScanOs检测已安装的win7，/RebuildBcd重建bcd。）
### 方法2 重新安、装修复grub2
1. 先使用ls命令，找到Ubuntu的安装在哪个分区：
在 grub rescue>下输入以下命令：
`ls`
会罗列所有的磁盘分区信息，比方说：
`(hd0,1),(hd0,5),(hd0,3),(hd0,2)`
2. 然后依次调用如下命令： X表示各个分区号码
如果/boot没有单独分区，用以下命令：
`ls (hd0,X)/boot/grub`
如果/boot单独分区，则用下列命令：
`ls （hd0,X)/grub/`
3. 正常情况下，会列出来几百个文件，很多文件的扩展名是.mod和.lst和.img，还有一个文件是grub.cfg。假设找到（hd0,5）时，显示了文件夹中的文件，则表示Linux安装在这个分区。
4. 如果找到了正确的grub目录，则设法临时性将grub的两部分关联起来，方法如下：
以下是/boot没有单独分区的命令：
`grub rescue>set root=(hd0,5)`
`grub rescue>set prefix=(hd0,5)/boot/grub`
`grub rescue>insmod /boot/grub/normal.mod`
以下是/boot 单独分区的命令：
`grub rescue>set root=(hd0,5)`
`grub rescue>set prefix=(hd0,5)/grub`
`grub rescue>insmod normal`
或尝试此命令
`grub rescue>insmod normal.mod`
然后调用如下命令，就可以显示出丢失的grub菜单了。
`grub rescue>normal`
不过不要高兴，如果这时重启，问题依旧存在，我们需要进入Linux中，对grub进行修复。
启动起来，进入ubuntu之后，在终端执行：
`sudo update-grub`
`sudo grub-install /dev/sda`
（sda是你的硬盘号码，千万不要指定分区号码，例如sda1，sda5等都不对）
重启测试是否已经恢复了grub的启动菜单？ 恭喜你恢复成功！
5. 如果找不到正确的/grub目录，比如第3、4种误操作，则尝试寻找是否有linux核心文件，则依次调用如下命令： X表示各个分区号码：
grub rescue>下，输入：
如果/boot没有单独分区：
`ls (hd0,X)/boot`
如果/boot单独分区，则：
`ls （hd0,X)`
找名字类似与vmlinuz-3.0.0-12-generic这样的文件，这是linux核心文件，如果找到，记下(hd0,X)中的X值。假设找到（hd0,5）时，显示了文件夹中的文件。
然后用live cd 或者 live usb启动，在live cd的ubuntu的终端中依次输入以下命令（sda5中的“5”必须改成上面记录下来数值）（这两句需要验证）：
如果/boot没有单独分区：
`sudo mount /dev/sda5 /mnt`
`sudo grub-install --boot-directory=/mnt/boot /dev/sda`
如果/boot单独分区，则：
`sudo mount /dev/sda5 /mnt`
`sudo grub-install --boot-directory=/mnt /dev/sda`
然后重新启动即可。
（以上这两句命令也可以解决安装ubuntu时grub安装位置不对，没有将grub安装到/dev/sda，造成启动时不出现ubuntu启动项直接进入windows的问题，不过需要自行确定sda5中的“5”改成什么数字。）
6. 如果连linux核心文件都没有，那么，彻底重新安装吧