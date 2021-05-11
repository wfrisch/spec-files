#
# spec file for package xaos
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


%define alt_name XaoS
Name:           xaos
Version:        4.2.1
Release:        0
Summary:        Powerful fractal generator
License:        GPL-2.0-or-later
Group:          Amusements/Toys/Graphics
URL:            https://xaos-project.github.io
Source0:        https://github.com/xaos-project/XaoS/archive/release-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  libQt5Widgets-devel >= 5.7
BuildRequires:  libqt5-linguist
BuildRequires:  libqt5-qtbase-common-devel
Provides:       %{alt_name}

%description
XaoS is a fast portable real-time interactive fractal zoomer. It
displays the Mandelbrot set (among other escape time fractals) and
allows you to zoom smoothly into the fractal.  Various coloring modes
are provided for both the points inside and outside the selected set.
In addition, switching between Julia and Mandelbrot fractal types and
displaying planes is provided.

%prep
%setup -q -n XaoS-release-%{version}

%build
%qmake5
%make_build STRIP=:

%install
# Empty install target generated by qmake => install files manually
# Binary
install -D --mode 0755 --target-directory %{buildroot}%{_bindir} bin/%{name}

# Data; Datapath forced to %%{alt_name} (not configurable)
install -D --mode 0644 --target-directory %{buildroot}%{_datadir}/%{alt_name}/catalogs catalogs/*.cat
cp --archive examples tutorial %{buildroot}%{_datadir}/%{alt_name}

# Icon, .desktop, AppData
install -D --mode 0644 --target-directory %{buildroot}%{_datadir}/metainfo xdg/%{name}.appdata.xml
install -D --mode 0644 --target-directory %{buildroot}%{_datadir}/applications xdg/%{name}.desktop
install -D --mode 0644 --target-directory %{buildroot}%{_datadir}/pixmaps xdg/%{name}.png

# Man
install -D --mode 0644 --target-directory %{buildroot}%{_mandir}/man6 doc/%{name}.6 

%files
%doc CREDITS.md NEWS doc/README
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{alt_name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man6/%{name}.6%{?ext_man}

%changelog
