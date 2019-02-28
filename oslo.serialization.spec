#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1A541148054E9E38 (infra-root@openstack.org)
#
Name     : oslo.serialization
Version  : 2.28.2
Release  : 45
URL      : http://tarballs.openstack.org/oslo.serialization/oslo.serialization-2.28.2.tar.gz
Source0  : http://tarballs.openstack.org/oslo.serialization/oslo.serialization-2.28.2.tar.gz
Source99 : http://tarballs.openstack.org/oslo.serialization/oslo.serialization-2.28.2.tar.gz.asc
Summary  : Oslo Serialization library
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.serialization-license = %{version}-%{release}
Requires: oslo.serialization-python = %{version}-%{release}
Requires: oslo.serialization-python3 = %{version}-%{release}
Requires: msgpack
Requires: oslo.utils
Requires: pbr
Requires: pytz
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pbr

%description
========================
Team and repository tags
========================
.. image:: https://governance.openstack.org/tc/badges/oslo.serialization.svg
:target: https://governance.openstack.org/tc/ference/tags/index.html

%package license
Summary: license components for the oslo.serialization package.
Group: Default

%description license
license components for the oslo.serialization package.


%package python
Summary: python components for the oslo.serialization package.
Group: Default
Requires: oslo.serialization-python3 = %{version}-%{release}

%description python
python components for the oslo.serialization package.


%package python3
Summary: python3 components for the oslo.serialization package.
Group: Default
Requires: python3-core

%description python3
python3 components for the oslo.serialization package.


%prep
%setup -q -n oslo.serialization-2.28.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551396139
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/oslo.serialization
cp LICENSE %{buildroot}/usr/share/package-licenses/oslo.serialization/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/oslo.serialization/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
