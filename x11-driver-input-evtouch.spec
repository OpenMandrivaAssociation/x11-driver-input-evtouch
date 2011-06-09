%define _disable_ld_no_undefined 1

Name:       x11-driver-input-evtouch
Version:    0.8.8
Release:    %mkrel 6
Summary:    Linux-Touchscreen Driver for X
Group:      System/X11
License:    MIT
URL:        http://www.conan.de/touchscreen/evtouch.html
Source:     http://www.conan.de/touchscreen/xf86-input-evtouch-%{version}.tar.bz2
# Debian patches
Patch0:     01_fix_warnings.patch
Patch1:     02_calibration_1.6.patch
Patch2:     03_server-1.6-ftbfs.diff
Patch3:     04_server-1.7-ftbfs.diff
BuildRequires:  x11-proto-devel
BuildRequires:  x11-server-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}

Requires: x11-server-common %(xserver-sdk-abi-requires xinput)

%description
Evtouch is a Touchscreen-Driver for X. 

%prep
%setup -q -n xf86-input-evtouch-%{version}
%apply_patches

%build
export CURSORDIR=%{_datadir}/xf86-input-evtouch
%configure2_5x --enable-evcalibrate
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README README.calibration
%{_libdir}/xorg/modules/input/evtouch_drv.la
%{_libdir}/xorg/modules/input/evtouch_drv.so
%{_libdir}/xf86-input-evtouch
%{_datadir}/xf86-input-evtouch
