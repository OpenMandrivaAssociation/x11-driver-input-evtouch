Name:       x11-driver-input-evtouch
Version:    0.8.6
Release:    %mkrel 1
Summary:    Linux-Touchscreen Driver for X
Group:      System/X11
License: MIT
URL:        http://stz-softwaretechnik.com/~ke/touchscreen/evtouch.html
Source:     http://stz-softwaretechnik.com/~ke/touchscreen/xf86-input-evtouch-%{version}.tar.bz2
BuildRequires:  x11-proto-devel >= 1.0.0
BuildRequires:  x11-server-devel >= 1.0.1
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Evtouch is a Touchscreen-Driver for X. 

%prep
%setup -q -n xf86-input-evtouch-%{version}

%build
%configure2_5x \
    --x-includes=%{_includedir}\
    --x-libraries=%{_libdir} \
    --enable-evcalibrate
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
