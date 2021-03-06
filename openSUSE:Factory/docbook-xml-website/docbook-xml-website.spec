#
# spec file for package docbook-xml-website
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           docbook-xml-website
BuildRequires:  sgml-skel unzip
Summary:        DTD and Stylesheets for Web Site Development
Version:        2.6.0
Release:        61
Group:          Productivity/Publishing/DocBook
Requires:       docbook-xsl-stylesheets xmlcharent docbook_4 sgml-skel
%define regcat /usr/bin/sgml-register-catalog
PreReq:         %{regcat} /usr/bin/xmlcatalog /usr/bin/edit-xml-catalog
PreReq:         sed grep awk
License:        MIT
Url:            http://sourceforge.net/projects/docbook/
Source0:        docbook-website-%{version}.tar.bz2
Source1:        CATALOG.docbook-xml-website
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
A DTD in XML as an extension to DocBook XML and XSL stylesheets to
process it.

%define INSTALL install -m755 -s
%define INSTALL_DIR install -d -m755
%define INSTALL_DATA install -m644
%define INSTALL_SCRIPT install -m755 -o root -g root
%define sgml_dir %{_datadir}/sgml
%define sgml_var_dir /var/lib/sgml
%define sgml_mod_dir %{sgml_dir}/docbook
%define sgml_mod_dtd_dir %{sgml_mod_dir}/dtd
%define sgml_mod_custom_dir %{sgml_mod_dir}/custom
%define sgml_mod_style_dir %{sgml_mod_dir}/stylesheet
%define xml_dir %{_datadir}/xml
%define xml_mod_dir %{xml_dir}/docbook/custom/website/%{version}
%define xml_mod_dtd_dir %{xml_mod_dir}/schema/dtd
%define xml_mod_custom_dir %{xml_mod_dir}/custom
%define xml_mod_style_dir %{xml_mod_dir}/stylesheet
%define xml_mod_style_prod_dir %{xml_mod_style_dir}
%define sgml_config_dir /var/lib/sgml
%define sgml_sysconf_dir %{_sysconfdir}/sgml
%define xml_config_dir /var/lib/xml
%define xml_sysconf_dir %{_sysconfdir}/xml

%prep
%setup -q -n docbook-website-%{version}
# /usr/share/xml/docbook/custom/website/2.6.0/catalog
sed 's|@VERSION@|%{version}|
s|@DIR@|%{xml_mod_dir}|' %{S:1} > CATALOG.%{name}
mv .CatalogManager.properties.example dot.CatalogManager.properties.example
find . -type f -name '\.*' | xargs rm

%build
xmlcatbin=/usr/bin/xmlcatalog
%define FOR_ROOT_CAT for-catalog-%{name}-%{version}.xml
CATALOG=%{xml_mod_dir}/catalog.xml
rm -f %{FOR_ROOT_CAT}.tmp
$xmlcatbin --noout --create %{FOR_ROOT_CAT}.tmp
$xmlcatbin --noout --add "delegateSystem" \
  "http://docbook.sourceforge.net/release/website/" \
  "file://$CATALOG" %{FOR_ROOT_CAT}.tmp
$xmlcatbin --noout --add "delegatePublic" \
  "-//Norman Walsh//DTD Website" \
  "file://$CATALOG" %{FOR_ROOT_CAT}.tmp
# Create tag
sed '/<catalog/a\
  <group id="%{name}-%{version}">
/<\/catalog/i\
  </group>' \
  %{FOR_ROOT_CAT}.tmp > %{FOR_ROOT_CAT}

%install
%{INSTALL_DIR} $RPM_BUILD_ROOT%{xml_mod_dir}
find . -type d -name '.xvpics' | xargs rm -fr
cp -a . $RPM_BUILD_ROOT%{xml_mod_dir}
rm -f $RPM_BUILD_ROOT%{xml_mod_dir}/for-catalog*
# install-dtd.sh -p %{name}-%{version}/schema/dtd \
#   -s $RPM_BUILD_ROOT%{sgml_dir} \
#   -f website.dtd \
#   -i '-//Norman Walsh//DTD Website V%{version}//EN'
# {
#   echo "DTDDECL \"-//Norman Walsh//DTD Website V%{version}//EN\" \"/usr/share/sgml/opensp/xml.dcl\""
#   echo "CATALOG %{sgml_dir}/CATALOG.db41xml"
#   echo "PUBLIC \"-//Norman Walsh//DTD Website V%{version}//EN\" \
# %{sgml_dir}/%{name}-%{version}/schema/dtd/website.dtd"
# } > CATALOG.%{name}
%{INSTALL_DIR} $RPM_BUILD_ROOT%{sgml_config_dir} $RPM_BUILD_ROOT%{sgml_dir}
%{INSTALL_DATA} CATALOG.%{name} $RPM_BUILD_ROOT%{sgml_config_dir}
pushd $RPM_BUILD_ROOT%{sgml_dir}
ln -sf ../../..%{sgml_config_dir}/CATALOG.%{name} CATALOG.%{name}
popd
cat_dir=%{buildroot}/etc/xml
%{INSTALL_DIR} $cat_dir
# %{INSTALL_DATA} %{name}.xml $RPM_BUILD_ROOT/etc/xml/%{name}.xml
%{INSTALL_DATA} %{FOR_ROOT_CAT} $cat_dir
# %define all_cat %{name}-%{version}

%post
if [ -x %{regcat} ]; then
  for c in docbook-xml-website; do
    %{regcat} -a  %{sgml_dir}/CATALOG.$c >/dev/null 2>&1 || true
  done
fi
edit-xml-catalog --group --catalog /etc/xml/suse-catalog.xml \
  --add /etc/xml/%{FOR_ROOT_CAT}

%postun
if [ "$1" = "0" -a -x %{regcat} ]; then
  for c in docbook-xml-website; do
    %{regcat} -r %{sgml_dir}/CATALOG.$c >/dev/null 2>&1 || true
  done
fi
# remove entries only on removal of file
if [ ! -f %{xml_sysconf_dir}/%{FOR_ROOT_CAT} -a -x /usr/bin/edit-xml-catalog ] ; then
  edit-xml-catalog --group --catalog /etc/xml/suse-catalog.xml \
    --del %{name}-%{version}
fi

%files
%defattr(-, root, root)
#%doc README.SuSE
%{xml_dir}/docbook/custom
# %{sgml_dir}
# %{sgml_dir}/Norman_Walsh
%{sgml_dir}/CATALOG.*
%config %{sgml_config_dir}/CATALOG.*
%config %{_sysconfdir}/xml/%{FOR_ROOT_CAT}

%changelog
