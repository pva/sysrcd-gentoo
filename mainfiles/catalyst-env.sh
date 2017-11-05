export XORGSTD_VIDEO_CARDS="vesa modesetting intel radeon nouveau nv dummy glint i128 i740 r128 mach64 rendition s3 siliconmotion trident sis savage cirrus voodoo sisusb ast tdfx via vmware apm"
export XORGSTD_INPUT_DEVICES="keyboard vmmouse mouse evdev synaptics"
export XORGMIN_VIDEO_CARDS="vesa modesetting nv dummy glint rendition s3 trident sis voodoo sisusb ast apm"
export XORGMIN_INPUT_DEVICES="keyboard mouse evdev synaptics"
export VIDEO_CARDS="${XORGSTD_VIDEO_CARDS}"
export INPUT_DEVICES="${XORGSTD_INPUT_DEVICES}"
export FEATURES="parallel-fetch -collision-protect -protect-owned -xattr"
export MAKEOPTS="-j5"
export PORTAGE_NICENESS="19"
export ACCEPT_LICENSE="*"
export CFLAGS="-Os -pipe"
export CXXFLAGS="-Os -pipe"
export CONFIG_PROTECT="-*"
export PYTHON_TARGETS="python2_7 python3_5"
export PYTHON_SINGLE_TARGET="python2_7"
export RUBY_TARGETS="ruby22"
export GRUB_PLATFORMS="efi-64 pc"
