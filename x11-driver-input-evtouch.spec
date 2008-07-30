Name:       x11-driver-input-evtouch
Version:    0.8.7
Release:    %mkrel 2
Summary:    Linux-Touchscreen Driver for X
Group:      System/X11
License:    MIT
URL:        http://stz-softwaretechnik.com/~ke/touchscreen/evtouch.html
Source:     http://stz-softwaretechnik.com/~ke/touchscreen/xf86-input-evtouch-%{version}.tar.bz2
Patch2:     04_include_xf86_ansic_h.patch
Patch3:     06_xf86-input-evtouch-0.8.7-misc.patch
BuildRequires:  x11-proto-devel
BuildRequires:  x11-server-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Evtouch is a Touchscreen-Driver for X. 

%prep
%setup -q -n xf86-input-evtouch-%{version}
%patch2 -p1 -b .ansic
%patch3 -p1 -b .misc

%build
export CURSORDIR=%{_datadir}/xf86-input-evtouch
%configure --enable-evcalibrate
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
