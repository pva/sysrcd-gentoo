subarch: i486
version_stamp: full
target: livecd-stage1
rel_type: default
profile: default/linux/x86/13.0
snapshot: 20160115
source_subpath: default/stage4-i486-baseos
portage_confdir: /worksrc/sysresccd-src/portage-etc-x86
portage_overlay: /worksrc/sysresccd-src/portage-overlay

livecd/use: sysrcdfull X consolekit icu gtk gtk2 -svg -opengl -glx -berkdb -gdbm -minimal -introspection dri bindist fbcon ipv6 livecd ncurses pam readline ssl unicode zlib nptl nptlonly multilib multislot jfs ntfs reiserfs xfs fat reiser4 samba png jpeg xorg usb pdf acl nologin atm bash-completion slang -kdrive vram loop-aes crypt device-mapper 7zip xattr bzip2 server lzo xpm bash-completion -fam -doc -hardened -spoof-source -static -tcpd -mailwrapper -milter -nls -selinux -ermt -pic -dar32 -dar64 -openct -pcsc-lite -smartcard -caps -qt3 -qt4 -aqua -cscope -gnome -gpm -motif -netbeans -nextaw -perl -python -ruby -xterm -emacs -justify -spell -vim-pager -vim-with-x -sqlite -afs -bashlogger -plugins -vanilla -examples -maildir pcre -accessibility -ithreads -perlsuid -php -pike -tcl -tk -nocxx -no-net2 -kerberos -sse2 -aio -cups -ldap -quotas -swat -syslog -winbind -socks5 -guile -X509 dbus -gnutls -gsm -cracklib -nousuid -skey -old-linux -pxeserial -multitarget -test -clvm -cman -gulm -gd -glibc-compat20 -glibc-omitfp -bidi -xinerama -qt3support -alsa -xcb nfsv4 -gallium -fortran

livecd/packages:
	app-admin/hddtemp
	app-admin/hwreport
	app-admin/ide-smart
	app-admin/mcelog
	app-admin/passook
	app-admin/procinfo-ng
	app-admin/pwgen
	app-admin/sudo
	app-admin/syslog-ng
	app-admin/sysstat
	app-admin/testdisk
	app-arch/afio
	app-arch/arj
	app-arch/bzip2
	app-arch/cabextract
	app-arch/cfv
	app-arch/cpio
	app-arch/dpkg
	app-arch/dump
	app-arch/gzip
	app-arch/lbzip2
	app-arch/lrzip
	app-arch/lz4
	app-arch/lzip
	app-arch/lzop
	app-arch/mt-st
	app-arch/ncompress
	app-arch/p7zip
	app-arch/par2cmdline
	app-arch/pbzip2
	app-arch/pigz
	app-arch/pixz
	app-arch/pxz
	app-arch/rpm
	app-arch/rpm2targz
	app-arch/rzip
	app-arch/sharutils
	app-arch/star
	app-arch/tar
	app-arch/unace
	app-arch/unrar
	app-arch/unshield
	app-arch/unzip
	app-arch/xz-utils
	app-arch/zip
	app-backup/bacula
	app-backup/dar
	app-backup/duplicity
	app-backup/fsarchiver
	app-backup/rsnapshot
	app-backup/tob
	app-benchmarks/bonnie++
	app-benchmarks/cpuburn
	app-benchmarks/iozone
	app-benchmarks/stress
	app-benchmarks/systester
	app-cdr/dvd+rw-tools
	app-cdr/isomaster
	app-cdr/xfburn
	app-crypt/chntpw
	app-crypt/md5deep
	app-crypt/nwipe
	app-editors/gvim
	app-editors/hexcurse
	app-editors/hexedit
	app-editors/joe
	app-editors/nano
	app-editors/qemacs
	app-editors/vim
	app-editors/vim-core
	app-editors/zile
	app-emulation/open-vm-tools
	app-forensics/afflib
	app-forensics/chkrootkit
	app-forensics/cmospwd
	app-forensics/foremost
	app-forensics/magicrescue
	app-misc/beep
	app-misc/ckermit
	app-misc/colordiff
	app-misc/emelfm2
	app-misc/fdupes
	app-misc/livecd-tools
	app-misc/mc
	app-misc/screen
	app-misc/scrub
	app-misc/symlinks
	app-misc/tmux
	app-misc/vlock
	app-misc/wipe
	app-portage/eix
	app-portage/gentoolkit
	app-portage/mirrorselect
	app-portage/portage-utils
	app-shells/bash
	app-shells/bash-completion
	app-shells/gentoo-bashcomp
	app-shells/ksh
	app-shells/tcsh
	app-shells/zsh
	app-text/dos2unix
	app-text/epdfview
	app-text/tree
	app-text/wgetpaste
	app-vim/gentoo-syntax
	dev-lang/ruby
	dev-libs/expat
	dev-libs/libconfig
	dev-libs/libdnet
	dev-libs/libisoburn
	dev-libs/libusb
	dev-libs/lzo
	dev-libs/openssl
	dev-libs/pkcs11-helper
	dev-libs/popt
	dev-scheme/guile
	dev-util/cmake
	dev-util/debootstrap
	dev-util/geany
	dev-util/intltool
	dev-util/ltrace
	dev-util/patchutils
	dev-util/pkgconfig
	dev-util/strace
	dev-vcs/git
	gnome-extra/nm-applet
	lxde-base/lxrandr
	media-fonts/font-adobe-75dpi
	media-fonts/font-bh-ttf
	media-fonts/font-bh-type1
	media-fonts/font-cursor-misc
	media-fonts/font-misc-misc
	media-fonts/font-util
	media-fonts/terminus-font
	media-fonts/unifont
	net-analyzer/arping
	net-analyzer/dnstracer
	net-analyzer/httping
	net-analyzer/ifstat
	net-analyzer/iftop
	net-analyzer/iptraf-ng
	net-analyzer/macchanger
	net-analyzer/netcat
	net-analyzer/ngrep
	net-analyzer/nmap
	net-analyzer/tcpdump
	net-analyzer/tcptraceroute
	net-analyzer/traceroute
	net-analyzer/vnstat
	net-dialup/gtkterm
	net-dialup/linux-atm
	net-dialup/mingetty
	net-dialup/minicom
	net-dialup/ppp
	net-dialup/pppconfig
	net-dialup/pptpclient
	net-dialup/rp-pppoe
	net-dns/bind-tools
	net-firewall/ipsec-tools
	net-firewall/iptables
	net-fs/curlftpfs
	net-fs/nfs-utils
	net-fs/samba
	net-ftp/ftp
	net-ftp/lftp
	net-ftp/ncftp
	net-ftp/tftp-hpa
	net-irc/irssi
	net-misc/autossh
	net-misc/bridge-utils
	net-misc/dhcp
	net-misc/dhcpcd
	net-misc/ethercard-diag
	net-misc/ifenslave
	net-misc/iperf
	net-misc/iputils
	net-misc/modemmanager
	net-misc/netkit-rsh
	net-misc/networkmanager
	net-misc/networkmanager-openvpn
	net-misc/networkmanager-vpnc
	net-misc/ntp
	net-misc/openssh
	net-misc/openvpn
	net-misc/pssh
	net-misc/rdate
	net-misc/rdesktop
	net-misc/rsync
	x11-misc/spacefm
	net-misc/telnet-bsd
	net-misc/tigervnc
	net-misc/udpcast
	net-misc/vconfig
	net-misc/vpnc
	net-misc/wget
	net-misc/whois
	net-misc/wput
	sys-firmware/atmel-firmware
	net-wireless/b43-fwcutter
	net-wireless/bcm43xx-fwcutter
	sys-firmware/ipw2100-firmware
	sys-firmware/ipw2200-firmware
	net-wireless/iw
	net-wireless/madwifi-ng-tools
	net-wireless/rfkill
	net-wireless/wireless-tools
	net-wireless/wpa_supplicant
	sys-firmware/zd1201-firmware
	sys-firmware/zd1211-firmware
	sys-apps/acl
	sys-apps/attr
	sys-apps/cciss_vol_status
	sys-apps/coreutils
	sys-apps/dcfldd
	sys-apps/debianutils
	sys-apps/diffutils
	sys-apps/dmapi
	sys-apps/dmidecode
	sys-apps/dstat
	sys-apps/dumpdisklayout
	sys-apps/ed
	sys-apps/ethtool
	sys-apps/fbset
	sys-apps/file
	sys-apps/findutils
	sys-apps/flashrom
	sys-apps/fxload
	sys-apps/gawk
	sys-apps/gptfdisk
	sys-apps/groff
	sys-apps/hdparm
	sys-apps/hwids
	sys-apps/hwsetup
	sys-apps/ipmitool
	sys-apps/iproute2
	sys-apps/kbd
	sys-apps/lm_sensors
	sys-apps/lshw
	sys-apps/man
	sys-apps/man-pages
	sys-apps/memtester
	sys-apps/miscfiles
	sys-apps/mlocate
	sys-apps/netplug
	sys-apps/net-tools
	sys-apps/openrc
	sys-apps/pcmciautils
	sys-apps/pv
	sys-apps/rename
	sys-apps/rescan-scsi-bus
	sys-apps/sdparm
	sys-apps/sed
	sys-apps/setserial
	sys-apps/sg3_utils
	sys-apps/shadow
	sys-apps/smartmontools
	sys-apps/sysresccd-custom
	sys-apps/tcp-wrappers
	sys-apps/udevil
	sys-apps/usb_modeswitch
	sys-apps/usbutils
	sys-apps/util-linux
	sys-apps/which
	sys-apps/x86info
	sys-auth/pambase
	sys-block/aic94xx-firmware
	sys-block/gpart
	sys-block/gparted
	sys-block/mbuffer
	sys-block/mpt-status
	sys-block/ms-sys
	sys-block/mtx
	sys-block/nbd
	sys-block/partclone
	sys-block/parted
	sys-block/partimage
	sys-block/scsiadd
	sys-block/whdd
	sys-boot/efibootmgr
	=sys-boot/grub-0.97-r16
	=sys-boot/grub-2.02_beta2-r8
	sys-boot/lilo
	sys-boot/mbr
	sys-boot/os-prober
	sys-boot/syslinux
	sys-cluster/drbd
	sys-cluster/glusterfs
	sys-devel/autoconf
	sys-devel/autogen
	sys-devel/automake
	sys-devel/bc
	sys-devel/crossdev
	sys-devel/gettext
	sys-devel/libtool
	sys-fs/btrfs-progs
	sys-fs/cryptsetup
	sys-fs/ddrescue
	sys-fs/dd-rescue
	sys-fs/diskdev_cmds
	sys-fs/dmraid
	sys-fs/dosfstools
	sys-fs/e2fsprogs
	sys-fs/ecryptfs-utils
	sys-fs/ext3grep
	sys-fs/extundelete
	sys-fs/fuse-exfat
	sys-fs/hfsplusutils
	sys-fs/hfsutils
	sys-fs/jfsutils
	sys-fs/lsscsi
	sys-fs/lufis
	sys-fs/lufs
	sys-fs/lvm2
	sys-fs/mac-fdisk
	sys-fs/mdadm
	sys-fs/mtd-utils
	sys-fs/multipath-tools
	sys-fs/ntfs3g
	sys-fs/ntfsreloc
	sys-fs/reiser4progs
	sys-fs/reiserfsprogs
	sys-fs/safecopy
	sys-fs/scrounge-ntfs
	sys-fs/squashfs-tools
	sys-fs/sshfs-fuse
	sys-fs/sysfsutils
	sys-fs/udftools
	sys-fs/xfsdump
	sys-fs/xfsprogs
	sys-fs/zerofree
	sys-kernel/gentoo-sources
	sys-kernel/linux-firmware
	sys-libs/libstdc++-v3
	sys-libs/openipmi
	sys-libs/pam
	sys-libs/pwdb
	sys-libs/readline
	sys-libs/zlib
	sys-power/acpi
	sys-process/atop
	sys-process/cronbase
	sys-process/htop
	sys-process/iotop
	sys-process/lsof
	sys-process/nmon
	sys-process/procps
	sys-process/psmisc
	sys-process/vixie-cron
	www-client/elinks
	www-client/midori
	www-servers/thttpd
	x11-apps/setxkbmap
	x11-apps/xcalc
	x11-apps/xdpyinfo
	x11-apps/xgamma
	x11-apps/xhost
	x11-apps/xinit
	x11-apps/xkbcomp
	x11-apps/xmodmap
	x11-apps/xrandr
	x11-apps/xset
	x11-apps/xwd
	x11-base/xorg-server
	x11-drivers/xf86-input-evdev
	x11-drivers/xf86-input-keyboard
	x11-drivers/xf86-input-mouse
	x11-drivers/xf86-input-vmmouse
	x11-libs/libXvMC
	x11-libs/libXxf86misc
	x11-libs/wxGTK
	x11-misc/grsync
	x11-misc/read-edid
	x11-misc/util-macros
	x11-misc/xkeyboard-config
	x11-proto/dri2proto
	x11-proto/glproto
	x11-proto/inputproto
	x11-proto/xextproto
	x11-proto/xf86driproto
	x11-proto/xf86miscproto
	x11-proto/xineramaproto
	x11-terms/xfce4-terminal
	x11-themes/gnome-icon-theme
	x11-wm/jwm
	xfce-base/xfce4-meta
	xfce-extra/xfce4-battery-plugin
	xfce-extra/xfce4-datetime-plugin
	xfce-extra/xfce4-notifyd
	xfce-extra/xfce4-taskmanager
	xfce-extra/xfce4-wavelan-plugin

