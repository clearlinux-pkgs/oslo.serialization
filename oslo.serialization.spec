#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC12B8E73B30F2FC8 (infra-root@openstack.org)
#
Name     : oslo.serialization
Version  : 4.0.1
Release  : 60
URL      : http://tarballs.openstack.org/oslo.serialization/oslo.serialization-4.0.1.tar.gz
Source0  : http://tarballs.openstack.org/oslo.serialization/oslo.serialization-4.0.1.tar.gz
Source1  : http://tarballs.openstack.org/oslo.serialization/oslo.serialization-4.0.1.tar.gz.asc
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
BuildRequires : buildreq-distutils3
BuildRequires : msgpack
BuildRequires : oslo.utils
BuildRequires : pbr
BuildRequires : pytz

%description
Team and repository tags
        ========================

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
Provides: pypi(oslo.serialization)
Requires: pypi(msgpack)
Requires: pypi(oslo.utils)
Requires: pypi(pbr)
Requires: pypi(pytz)

%description python3
python3 components for the oslo.serialization package.


%prep
%setup -q -n oslo.serialization-4.0.1
cd %{_builddir}/oslo.serialization-4.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1600109761
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/oslo.serialization
cp %{_builddir}/oslo.serialization-4.0.1/LICENSE %{buildroot}/usr/share/package-licenses/oslo.serialization/57aed0b0f74e63f6b85cce11bce29ba1710b422b
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/oslo.serialization/57aed0b0f74e63f6b85cce11bce29ba1710b422b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
