#
# spec file for package audit
#
# Copyright (c) 2021 SUSE LLC
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


Name:           audit
Version:        2.8.5
Release:        0
Summary:        Linux kernel audit subsystem utilities
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            http://people.redhat.com/sgrubb/audit/
Source0:        http://people.redhat.com/sgrubb/audit/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
Source2:        README-BEFORE-ADDING-PATCHES
Patch0:         change-default-log_group.patch
BuildRequires:  autoconf >= 2.12
BuildRequires:  gcc-c++
BuildRequires:  kernel-headers >= 2.6.30
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  tcpd-devel
Requires:       libaudit1 = %{version}
Requires:       libauparse0 = %{version}

%description
The audit package contains the user space utilities for storing and
processing the records generated by the audit subsystem in the
Linux kernel.

%package -n libaudit1
Summary:        Library for interfacing with the kernel audit subsystem
License:        LGPL-2.1-or-later
Group:          System/Libraries
Obsoletes:      %{name}-libs < 2.0.4
Provides:       %{name}-libs = %{version}

%description -n libaudit1
The libaudit package contains the shared libraries needed for
applications to use the audit framework.

%package -n libauparse0
Summary:        Library for parsing and interpreting audit events
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libauparse0
The libauparse package contains the shared libraries needed to
parse audit records.

%package -n audit-devel
Summary:        Header files for libaudit
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       libaudit1 = %{version}
Requires:       libauparse0 = %{version}

%description -n audit-devel
The audit-devel package contains the header files
needed for developing applications that need to use the audit framework
libraries.

%prep
%setup -q
%patch0 -p1

%build
autoreconf -fi
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="-Wl,-z,relro,-z,now"
# no krb support (omit --enable-gssapi-krb5=yes), see audit-no-gss.patch
%configure \
	--enable-systemd \
	--libexecdir=%{_libexecdir}/%{name} \
	--with-apparmor \
	--with-libwrap \
	--without-libcap-ng \
	--disable-static \
	--without-python \
%ifarch aarch64
       --with-aarch64 \
%endif
	--disable-zos-remote
make %{?_smp_mflags} -C lib
make %{?_smp_mflags} -C auparse
make %{?_smp_mflags} -C docs

%install
%make_install -C lib
%make_install -C auparse
%make_install -C docs
rm -rf %{buildroot}/%{_mandir}/man[578]
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}/%{_includedir}
mkdir -p %{buildroot}/%{_mandir}/man5
# We manually install this since Makefile doesn't
install -m 0644 lib/libaudit.h %{buildroot}/%{_includedir}
install -D -m 0644 ./m4/audit.m4  %{buildroot}%{_datadir}/aclocal/audit.m4
# Install libaudit.conf files by hand
install -m 0644 docs/libaudit.conf.5 %{buildroot}/%{_mandir}/man5
install -m 0644 init.d/libaudit.conf %{buildroot}%{_sysconfdir}

find %{buildroot} -type f -name "*.la" -delete -print

%check
make %{?_smp_mflags} check -C lib
make %{?_smp_mflags} check -C auparse

%post -n libaudit1 -p /sbin/ldconfig
%post -n libauparse0 -p /sbin/ldconfig
%postun -n libaudit1 -p /sbin/ldconfig
%postun -n libauparse0 -p /sbin/ldconfig

%files -n libaudit1
%{_libdir}/libaudit.so.*
%config(noreplace) %attr(640,root,root) %{_sysconfdir}/libaudit.conf
%{_mandir}/man5/libaudit.conf.5%{ext_man}

%files -n libauparse0
%{_libdir}/libauparse.so.*

%files -n audit-devel
%doc contrib/skeleton.c contrib/plugin
%{_libdir}/libaudit.so
%{_libdir}/libauparse.so
%{_includedir}/libaudit.h
%{_includedir}/auparse.h
%{_includedir}/auparse-defs.h
%{_mandir}/man3/*
%{_datadir}/aclocal/audit.m4
%{_libdir}/pkgconfig/audit.pc
%{_libdir}/pkgconfig/auparse.pc

%changelog
