#
# spec file for package log4cpp
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           log4cpp
Version:        1.1.3
Release:        0
Summary:        C++ logging library
License:        LGPL-2.1-only
Group:          Development/Languages/C and C++
Url:            http://%{name}.sourceforge.net/
Source:         %{name}-%{version}.tar.xz
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
%if 0%{?suse_version}
BuildRequires:  fdupes
%endif

%define libname lib%{name}5

%description
Log for C++ is a library of classes for flexible logging to files,
syslog, and other destinations. It is modeled after the Log for Java
library and stays as close to its API as is reasonable.

%package -n %{libname}
Summary:        Logging for C++
Group:          System/Libraries

%description -n %{libname}
Logging facilities providing library.

%package devel
Summary:        Development tools for Log for C++
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
The %{name}-devel package contains the static libraries and header files
needed for development with %{name}.

%package doc
Summary:        HTML formatted API documention for Log for C++
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
The %{name}-doc package contains HTML formatted API documention generated by
the popular doxygen documentation generation tool.

%prep
%setup -q -n %{name}

%build
%configure --enable-doxygen --disable-static
make %{?_smp_mflags}

%install
%make_install mandir="%{buildroot}/%{_mandir}" docdir="%{buildroot}/%{_docdir}/%{name}"
find %{buildroot} -type f -name "*.la" -delete -print
%if 0%{?suse_version}
%fdupes -s %{buildroot}/%{_docdir}/%{name}/api
%endif

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}
%{_mandir}/man3/%{name}*.3%{?ext_man}
%{_bindir}/%{name}-config
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%dir %{_datadir}/aclocal
%attr(644,root,root) %{_datadir}/aclocal/%{name}.m4

%files doc
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README THANKS
%doc %{_docdir}/%{name}
%license COPYING

%changelog
