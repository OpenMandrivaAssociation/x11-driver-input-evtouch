%define _disable_ld_no_undefined 1

Summary:    Linux-Touchscreen Driver for X
Name:       x11-driver-input-evtouch
Version:    0.8.8
Release:    12
Group:      System/X11
License:    MIT
Url:        http://www.conan.de/touchscreen/evtouch.html
Source0:     http://www.conan.de/touchscreen/xf86-input-evtouch-%{version}.tar.bz2
# Debian patches
Patch0:     01_fix_warnings.patch
Patch1:     02_calibration_1.6.patch
Patch2:     03_server-1.6-ftbfs.diff
Patch3:     04_server-1.7-ftbfs.diff
# Patches to fix build with x11 >= 1.10
Patch4:     evtouch-replace-LocalDevicePtr-with-InputInfoPtr.patch
Patch5:     evtouch-remove-libc-wrapper-usage-for-xcalloc-xalloc-xfree.patch
Patch6:     evtouch-use-a-local-variable-for-history_size.patch
Patch7:     evtouch-purge-unused-close_proc.patch
Patch8:     evtouch-add-mode-field-to-InitValuatorAxisStruct.patch
Patch9:     evtouch-adjust-to-new-PreInit.patch

BuildRequires:  pkgconfig(xorg-server)
BuildRequires:  pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires xinput)

%description
Evtouch is a Touchscreen-Driver for X.

%prep
%setup -qn xf86-input-evtouch-%{version}
%apply_patches

%build
export CURSORDIR=%{_datadir}/xf86-input-evtouch
%configure2_5x --enable-evcalibrate
%make

%install
%makeinstall_std

%files
%doc README README.calibration
%{_libdir}/xorg/modules/input/evtouch_drv.so
%{_libdir}/xf86-input-evtouch
%{_datadir}/xf86-input-evtouch

