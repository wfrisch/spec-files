#
# spec file for package pmdk-convert
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright 2016, Intel Corporation
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


Name:           pmdk-convert
Version:        1.7
Release:        0
Summary:        PMDK pool conversion tool
License:        BSD-3-Clause
Group:          System/Base
Url:            http://pmem.io/pmdk/
Source:         https://github.com/pmem/pmdk-convert/archive/%version.tar.gz#/%{name}-%{version}.tar.gz
# Script to predownload the artifacts needed for building and add them for commit
Source999:      download_artifacts.sh
Patch0:         cmake_hash.patch

# This section is autogenerated by download_artifacts.sh
# DO NOT MODIFY it nor the START/END markers
## START_NVML_SOURCE
Source1:        1.0.tar.gz
Source2:        1.1.tar.gz
Source3:        1.2.4.tar.gz
Source4:        1.3.3.tar.gz
Source5:        1.4.3.tar.gz
Source6:        1.5.2.tar.gz
Source7:        1.6.1.tar.gz
Source8:        1.7.tar.gz

## END_NVML_SOURCE

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

# By design, NVML does not support any 32-bit architecture.
# Due to dependency on xmmintrin.h and some inline assembly, it can be
# compiled only for x86_64 at the moment.
# Other 64-bit architectures could also be supported, if only there is
# a request for that, and if somebody provides the arch-specific
# implementation of the low-level routines for flushing to persistent
# memory.
ExclusiveArch:  x86_64

%description
pmdk-convert allows conversion of PMDK pools from any version, starting from 1.0, to
all later versions. It replaces pmempool-convert.

%prep
%setup -q
%patch0 -p1
# Copy And Extract pre downloaded nvml tarball
# This section is autogenerated by download_artifacts.sh
# This copy/extract is needed to mimic a previous execution of
# cmake so it will not try to download those file from the network.
# DO NOT MODIFY it nor the START/END markers
## START_NVML_SETUP
cp %{S:1} .
tar -xf %{S:1}
cp %{S:2} .
tar -xf %{S:2}
cp %{S:3} .
tar -xf %{S:3}
cp %{S:4} .
tar -xf %{S:4}
cp %{S:5} .
tar -xf %{S:5}
cp %{S:6} .
tar -xf %{S:6}
cp %{S:7} .
tar -xf %{S:7}
cp %{S:8} .
tar -xf %{S:8}

## END_NVML_SETUP

%build
# For some reason cmake fails to extract the nvml tarball if LANG is not UTF8
export LANG=en_US.UTF-8
# Enable RPATH as the build system itself requires it
%cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_SKIP_RPATH:BOOL=OFF
%cmake_build

%install
%cmake_install

%files
%defattr(-,root,root)
%_bindir/pmdk-convert
%_libdir/pmdk-convert/
%_mandir/man1/pmdk-convert.1*
%license LICENSE
%doc ChangeLog

%changelog