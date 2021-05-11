#
# spec file for package xf86-video-vmware
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           xf86-video-vmware
Version:        13.3.0
Release:        0
Summary:        VMware SVGA video driver for the Xorg X server
License:        MIT
Group:          System/X11/Servers/XF86_4
Url:            http://xorg.freedesktop.org/
#http://xorg.freedesktop.org/releases/individual/driver/
Source0:        http://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.bz2
ExclusiveArch:  %ix86 x86_64
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(pciaccess) >= 0.8.0
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(renderproto)
BuildRequires:  pkgconfig(videoproto)
BuildRequires:  pkgconfig(xatracker) >= 0.4.0
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xineramaproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xorg-server) >= 1.0.1
BuildRequires:  pkgconfig(xproto)
Supplements:    modalias(xorg-x11-server:pci:v000015ADd*sv*sd*bc03sc*i*)
# This was part of the xorg-x11-driver-video package up to version 7.6
Conflicts:      xorg-x11-driver-video <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%x11_abi_videodrv_req

%description
vmware is an Xorg driver for VMware virtual video cards.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README
%dir %{_libdir}/xorg/modules/drivers
%{_libdir}/xorg/modules/drivers/vmware_drv.so
%{_datadir}/man/man4/vmware.4%{?ext_man}

%changelog
