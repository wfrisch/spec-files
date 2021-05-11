#
# spec file for package unknown-horizons
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2011 Nelson Marques <nmarques@opensuse.org>
# Copyright (c) Unknown Horizons, http://www.unknown-horizons.org
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


Name:           unknown-horizons
Version:        2019.1
Release:        0
Summary:        An economy and city building game
License:        APL-1.0 AND CC-BY-SA-3.0 AND GPL-2.0-with-font-exception AND MIT AND OFL-1.1
Group:          Amusements/Games/Strategy/Other
URL:            http://www.unknown-horizons.org
Source0:        https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# https://github.com/unknown-horizons/unknown-horizons/pull/2891
Patch0:         unknown-horizons-encoding.patch
# PATCH-FIX-UPSTREAM
Patch1:         0001-replace-deprecated-to-distro-package-2910.patch
# PATCH-FIX-OPENSUSE -- Use python3 without env for rpm detection
Patch2:         rpm-shbang.patch
# PATCH-FIX-UPSTREAM https://github.com/unknown-horizons/unknown-horizons/pull/2943
Patch3:         reproducible.patch
# PATCH-FIX-UPSTREAM https://github.com/unknown-horizons/unknown-horizons/pull/2946
Patch4:         appdata.patch
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fdupes
BuildRequires:  fife-devel >= 0.4.2
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  python3-Cython
BuildRequires:  python3-Pillow
BuildRequires:  python3-distro
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-pathlib
BuildRequires:  python3-typing
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(libexslt)
BuildRequires:  pkgconfig(libxslt)
Requires:       hicolor-icon-theme
Requires:       python3-Pillow
Requires:       python3-PyYAML
Requires:       python3-fife >= 0.4.2
Recommends:     %{name}-lang = %{version}
# python3-enet is only required for multiplayer and the game gracefully handles it not
# being present.
Recommends:     python3-pyenet
BuildArch:      noarch

%description
Unknown Horizons is a 2D realtime strategy simulation with an emphasis on
economy and city building. The player has to expand a small settlement to a strong and
wealthy colony, collect taxes and supply inhabitants with valuable
goods, and increase the power with a well balanced economy and with strategic
trade and diplomacy.

%lang_package

%prep
%autosetup -p1

%build
python3 setup.py build
# For some reason the Atlas generated by setup.py is corrupted. It has more
# entries in the DB than there are image files. Regeneration fixes this.
python3 horizons/engine/generate_atlases.py 2048

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

rm -v %{buildroot}%{_datadir}/locale/stats.json

# -- remove *egg-info
find %{buildroot}%{python_sitelib} -type f -name "*.egg-info" -print -delete

# Install vector icon and remove old one
install -D -m 0644 content/gui/images/logos/uh_no_text.svg \
    %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
rm -v %{buildroot}%{_datadir}/pixmaps/unknown-horizons.xpm

# Remove file only existing to ensure directoy is not dropped by Git
rm -v %{buildroot}%{_datadir}/%{name}/content/gfx/atlas/.keepme

# Remove duplicate license files
rm -v %{buildroot}%{_datadir}/%{name}/content/fonts/{GPL_fontexception,OFL}

# Remove duplicate languages and find correct ones
rm -rfv %{buildroot}%{_datadir}/%{name}/content/lang
%find_lang %{name}
%find_lang %{name}-server

# Fix file permissions
find %{buildroot}%{_datadir}/%{name} -type f -exec chmod 644 \{\} +

%suse_update_desktop_file -i -r -G "A RTS simulation game" %{name} StrategyGame Game

install -D -m 0644 content/packages/%{name}.appdata.xml %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%fdupes %{buildroot}%{python_sitelib}
%fdupes %{buildroot}%{_datadir}

%files
%doc README.md doc/CHANGELOG.md
%license doc/LICENSE doc/AUTHORS.md doc/licenses/
%{_bindir}/unknown-horizons
%{python3_sitelib}/horizons/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/%{name}/
%{_datadir}/icons/*/*/*/%{name}.svg
%{_mandir}/man6/%{name}.6%{?ext_man}

%files lang -f %{name}-server.lang -f %{name}.lang

%changelog