#!/bin/bash

# This is an example fsscript for use with the livecd-stage2 target (key
# livecd/fsscript).  This file is copied into the rootfs of the CD after the
# kernel(s) and any external modules have been compiled and is then executed
# within the context of the chroot.

# define hostname
rm -f /etc/conf.d/hostname
echo "HOSTNAME=sysresccd" > /etc/conf.d/hostname
sed -i -e 's/livecd/sysresccd/g' /etc/hosts

# clean the resolv.conf file ("dig . ns" to get list of root DNS)
echo "nameserver 8.8.8.8" > /etc/resolv.conf

# change the default shell
chsh -s /bin/zsh root

# remove .svn files
#find / -name ".svn" -exec rm -rf {} \; >/dev/null 2>&1

# Remove python precompiled files
find /usr/lib -name "*.py?" -exec rm -f {} \; >/dev/null 2>&1

# remove warning from clock service
sed -i -e 's:#TIMEZONE="Factory":TIMEZONE="Europe/London":g' /etc/conf.d/clock

# remove warning from freshclam when clamd not running
sed -i -e 's:NotifyClamd:#NotifyClamd:' /etc/freshclam.conf

# disable DHCP by default in autoconfig
sed -i -e 's/ewarn "Skipping DHCP broadcast detection as requested on boot commandline ..."//' /etc/init.d/autoconfig
sed -i -e 's/DHCP="yes"/DHCP="no"/' /etc/init.d/autoconfig

# running hwsetup disturbs the speakup, so run "hwsetup -f" when speakup is used
sed -i -e 's!\[ -x /usr/sbin/hwsetup \] && hwsetup!cat /proc/cmdline | grep -qF "speakup=" \&\& speakupopt=" -f" ; \[ -x /usr/sbin/hwsetup \] \&\& hwsetup ${speakupopt}!g' /etc/init.d/autoconfig

# disable netplug
sed -i -e 's/"netplugd"//' /etc/init.d/net.lo

# make ssh-keygen silent in the sshd initscript
sed -i -e 's!/usr/bin/ssh-keygen!/usr/bin/ssh-keygen -q!g' /etc/init.d/sshd

# disable ALSA sound by default in autoconfig
sed -i -e 's/GPM="yes"/GPM="no"/' /etc/init.d/autoconfig
sed -i -e 's/ALSA="yes"/ALSA="no"/' /etc/init.d/autoconfig
sed -i -e 's/NFS="yes"/NFS="no"/' /etc/init.d/autoconfig
sed -i -e 's/PCMCIA="yes"/PCMCIA="no"/' /etc/init.d/autoconfig
sed -i -e 's/Skipping ALSA detection as requested on command line .../Skipping ALSA detection .../' /etc/init.d/autoconfig

# /etc/udev/rules.d/75-persistent-net-generator.rules conflicts with the sysresccd "nameif=xxx" option
#sed -i -e 's!^ENV{INTERFACE_NEW}!#ENV{INTERFACE_NEW}!g' /etc/udev/rules.d/75-persistent-net-generator.rules

# /sbin/livecd-functions.sh expect 'cdroot' in /proc/cmdline (we removed cdroot)
sed -i -e 's!for x in ${CMDLINE}!for x in ${CMDLINE} cdroot!g' /sbin/livecd-functions.sh

# allow freshclam
chown clamav:clamav /var/log/clamav
chown clamav:clamav /var/run/clamav
chown clamav:clamav /var/lib/clamav
chown clamav:clamav /var/lib/clamav/*

# remove warnings about files with a modification time in the future!
sed -i -e 's!if \[\[ ${clock_screw} == 1 \]\]!if \[\[ ${clock_screw} == 2 \]\]!g' /etc/init.d/depscan.sh
sed -i -e 's!if \[\[ ${clock_screw} == 1 \]\]!if \[\[ ${clock_screw} == 2 \]\]!g' /sbin/depscan.sh

# don't overwrite /proc/sys/kernel/printk in /etc/init.d/autoconfig
# http://www.sysresccd.org/forums/viewtopic.php?p=5800
sed -i -r -e 's!echo "[0-9]" > /proc/sys/kernel/printk!!g' /etc/init.d/autoconfig

# fix /sbin/livecd-functions.sh that fixes inittab
# http://www.sysresccd.org/forums/viewtopic.php?t=2040&postdays=0&postorder=asc&start=15
sed -i -e 's!s0:12345:respawn:/sbin/agetty -nl /bin/bashlogin!s0:12345:respawn:/sbin/agetty -L -nl /bin/bashlogin!g' /sbin/livecd-functions.sh

# prevent the firmware extraction from displaying warnings when the clock is wrong
sed -i -e 's!tar xjf /lib/firmware.tar.bz2!tar xjfm /lib/firmware.tar.bz2!g' /etc/init.d/autoconfig

# fix a bug in the default mtools configuration file
sed -i -e 's!SAMPLE FILE!#SAMPLE FILE!g' /etc/mtools/mtools.conf

# don't use fbdev as the default xorg driver since framebuffer is disabled
sed -i -e 's![ -z "${XMODULE}" ] && XMODULE="fbdev"![ -z "${XMODULE}" ] && XMODULE="vesa"!g' /usr/sbin/mkxf86config.sh

# prevent sshd from complaining
touch /var/log/lastlog

# preserve the 'ar' and 'strings' binaries from the binutils package (and its libs)
cp -a /usr/i486-pc-linux-gnu/binutils-bin/*/ar /usr/sbin/
cp -a /usr/i486-pc-linux-gnu/binutils-bin/*/strings /usr/sbin/
cp -a /usr/lib/binutils/i486-pc-linux-gnu/*/libbfd*.so /usr/lib/

# provide a symblink to libstdc++.so.6 so that we can install all packages
ln -s /lib/lib/gcc/i486-pc-linux-gnu/*/libstdc++.so.6 /usr/lib/libstdc++.so.6

# replace the strings-static binary (provided by app-forensics/chkrootkit) to save splace
rm -f /usr/sbin/strings-static ; ln -s /usr/sbin/strings /usr/sbin/strings-static

# make space by removing the redundant insmod.static binary
rm -f /sbin/insmod.static ; ln -s /sbin/insmod /sbin/insmod.static

# remove rdev-rebuild temp files
rm -f /var/cache/revdep-rebuild/*

# manage mksquashfs/unsquashfs programs
[ ! -f /usr/bin/mksquashfs-lzma ] && ln -s /usr/bin/mksquashfs /usr/bin/mksquashfs-lzma
[ ! -f /usr/bin/unsquashfs-lzma ] && ln -s /usr/bin/unsquashfs /usr/bin/unsquashfs-lzma

# create link for reiserfsck
[ ! -f /sbin/fsck.reiserfs ] && ln /sbin/reiserfsck /sbin/fsck.reiserfs

# prevent the /etc/init.d/net.eth* from being run --> they break the network (done via "ethx, dns, gateway")
rm -f /etc/init.d/net.eth*

# remove xfce icons for missing programs
rm -f /usr/share/applications/{xfce4-file-manager.desktop,xfce4-help.desktop}

# fix the "xfce4-logout" entry in the menu
sed -i -e 's!xfce4-session-logout!killall xinit!g' /usr/share/applications/xfce4-logout.desktop

# decompress oscar files
if [ -f /usr/share/oscar/oscar.tar.gz ]
then
	tar xfzp /usr/share/oscar/oscar.tar.gz -C /usr/share/oscar
	rm -rf /usr/share/oscar/oscar.tar.gz
fi

# prepare the runxserver script
rm -f /usr/bin/X
ln -s /root/runxserver /usr/bin/X

# for programs that expect syslog
ln -s /usr/sbin/syslog-ng /usr/sbin/syslog

# install the 32bits kernel modules
for modtar in /lib/modules/*.tar.bz2
do
	echo '--------------------------------------------------------------'
	kerver=$(basename $modtar | sed -e 's/.tar.bz2//')
	echo "DECOMPRESS32 (version [$kerver]): tar xfjp $modtar -C /lib/modules/"
	tar xfjp $modtar -C /lib/modules/
	echo "DEPMOD32: depmod -ae -v $kerver"
	depmod -ae -v $kerver > /dev/null
	rm -f $modtar
	echo '--------------------------------------------------------------'
done

# install the 64bits kernel modules
for modtar in /lib64/modules/*.tar.bz2
do
	echo '--------------------------------------------------------------'
	kerver=$(basename $modtar | sed -e 's/.tar.bz2//')
	echo "DECOMPRESS64 (version [$kerver]): tar xfjp $modtar -C /lib64/modules/"
	tar xfjp $modtar -C /lib64/modules/
	echo "LINK64: ln -s /lib64/modules/$kerver /lib/modules/$kerver"
	ln -s /lib64/modules/$kerver /lib/modules/$kerver
	echo "DEPMOD64: depmod -ae -v $kerver"
	depmod -ae -v $kerver > /dev/null
	rm -f $modtar
	echo '--------------------------------------------------------------'
done

# workaround for new libexpat version
[ -h /usr/lib/libexpat.so.0 ] || ln -s /usr/lib/libexpat.so /usr/lib/libexpat.so.0

# strip kernel modules which are in the sysrcd.dat to save space
find /lib/modules -name "*.ko" -exec strip --strip-unneeded '{}' \;
find /lib64/modules -name "*.ko" -exec strip --strip-unneeded '{}' \;

# update /etc/make.profile
rm -rf /etc/make.profile
ln -s ../usr/portage/profiles/default/linux/x86/10.0 /etc/make.profile

# update the database for locate
echo "--> locate -u"
locate -u >/dev/null 2>&1

# create the apropos / whatis database
echo "--> makewhatis"
makewhatis >/dev/null 2>&1

# create the locales:
localedef -i /usr/share/i18n/locales/en_US -f UTF-8 /usr/lib/locale/en_US.utf8
localedef -i /usr/share/i18n/locales/en_US -f ISO-8859-1 /usr/lib/locale/en_US
localedef -i /usr/share/i18n/locales/de_DE -f ISO-8859-1 /usr/lib/locale/de_DE
localedef -i /usr/share/i18n/locales/fr_FR -f ISO-8859-1 /usr/lib/locale/fr_FR
