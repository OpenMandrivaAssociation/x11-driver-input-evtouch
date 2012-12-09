%define _disable_ld_no_undefined 1

Name:       x11-driver-input-evtouch
Version:    0.8.8
Release:    9
Summary:    Linux-Touchscreen Driver for X
Group:      System/X11
License:    MIT
URL:        http://www.conan.de/touchscreen/evtouch.html
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
BuildRequires:  x11-proto-devel
BuildRequires:  x11-server-devel

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

%files
%doc README README.calibration
%{_libdir}/xorg/modules/input/evtouch_drv.so
%{_libdir}/xf86-input-evtouch
%{_datadir}/xf86-input-evtouch


%changelog
* Sun Mar 25 2012 Andrew Lukoshko <andrew.lukoshko@rosalab.ru> 0.8.8-6rosa.lts2012.0
- fixed build with x11 >= 1.10

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 0.8.8-5mdv2011.0
+ Revision: 671123
- mass rebuild

* Fri Nov 19 2010 Thierry Vignaud <tv@mandriva.org> 0.8.8-4mdv2011.0
+ Revision: 599050
- use %%apply_patches
- sync with updates/2010.1 branch: Add another Debian patch for new input API
  (from Glenn Sommer)
- require xorg server with proper ABI
- bump release before rebuilding for xserver 1.9

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt for 2010.1

* Tue May 19 2009 Frederik Himpe <fhimpe@mandriva.org> 0.8.8-1mdv2010.0
+ Revision: 377767
- Update to new version 0.8.8
- Remove old patches
- Sync patches with Debian to make it build with xserver 1.6
- Use %%configure2_5x instead of %%configure to make it build with new libtool

* Wed Jul 30 2008 Olivier Blin <oblin@mandriva.com> 0.8.7-3mdv2009.0
+ Revision: 255550
- disable ld no_undefined (weird 2mdv passed the build system)
- add more fixes from Debian (reverting parts of the other Debian patch..)

* Wed Jul 30 2008 Olivier Blin <oblin@mandriva.com> 0.8.7-2mdv2009.0
+ Revision: 255221
- add Xorg 1.4 support and various fixes (from Debian)
- drop compile fixes
- drop Q1U patch (hopefully handled by EV_SYN changes in Debian patch)
- fix includes (from Debian)
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 15 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 0.8.7-1mdv2008.1
+ Revision: 98619
- new upstream version: 0.8.7
- added compile-fix.patch (upstream compilation is broken)
- ported q1u.patch to the new version

* Fri Aug 31 2007 Olivier Blin <oblin@mandriva.com> 0.8.6-4mdv2008.0
+ Revision: 76965
- add support for Samsung Q1U touchscreen axes (patch from Pepper, taken from Ubuntu)

* Fri Aug 03 2007 Olivier Blin <oblin@mandriva.com> 0.8.6-3mdv2008.0
+ Revision: 58611
- fix cursor path in ev_calibrate (thanks to rtp for the bug report)

* Thu Jun 28 2007 Olivier Blin <oblin@mandriva.com> 0.8.6-2mdv2008.0
+ Revision: 45242
- remove buildrequires versions (not needed even for 2007.0)
- remove useless X configure options
- remove unused x11-util-macros buildrequire
- add README files

* Tue Jun 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.6-1mdv2008.0
+ Revision: 41314
- fix package name
- wrong name
- import x11-input-driver-evtouch
