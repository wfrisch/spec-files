#
# spec file for package libretro-atari800
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


Name:           libretro-atari800
Version:        0~git20200429
Release:        0
Summary:        Atari800 libretro core for Atari 5200 emulation
License:        GPL-3.0-only
Group:          System/Emulators/Other
URL:            http://www.retroarch.com
Source:         %{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  zlib-devel

%description
atari800 3.1.0 for libretro/libco WIP

%prep
%setup -q

%build
make GIT_VERSION=%version

%install
mkdir -p %{buildroot}%{_libdir}/libretro
cp atari800_libretro.so %{buildroot}%{_libdir}/libretro

%files
%dir %{_libdir}/libretro
%{_libdir}/libretro/atari800_libretro.so

%changelog
