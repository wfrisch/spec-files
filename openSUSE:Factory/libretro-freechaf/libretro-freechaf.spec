#
# spec file for package libretro-freechaf
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           libretro-freechaf
Version:        0~git20200512
Release:        0
Summary:        FreeChaF libretro core for Fairchild ChannelF emulation
License:        GPL-3.0-only
URL:            http://www.retroarch.com
Source:         %{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  make

%description
FreeChaF is a libretro emulation core for the Fairchild ChannelF / Video
Entertainment System designed to be compatible with joypads from the SNES era
forward. This package is for RetroArch/Libretro front-end.

%prep
%setup -q

%build
make

%install
mkdir -p %{buildroot}%{_libdir}/libretro
cp freechaf_libretro.so %{buildroot}%{_libdir}/libretro

%files
%dir %{_libdir}/libretro
%{_libdir}/libretro/freechaf_libretro.so

%changelog
