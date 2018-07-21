#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : oslo.serialization
Version  : 2.27.0
Release  : 40
URL      : http://tarballs.openstack.org/oslo.serialization/oslo.serialization-2.27.0.tar.gz
Source0  : http://tarballs.openstack.org/oslo.serialization/oslo.serialization-2.27.0.tar.gz
Summary  : Oslo Serialization library
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.serialization-python3
Requires: oslo.serialization-license
Requires: oslo.serialization-python
Requires: Sphinx
Requires: oslo.utils
Requires: pbr
Requires: pytz
Requires: reno
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

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
Requires: oslo.serialization-python3

%description python
python components for the oslo.serialization package.


%package python3
Summary: python3 components for the oslo.serialization package.
Group: Default
Requires: python3-core

%description python3
python3 components for the oslo.serialization package.


%prep
%setup -q -n oslo.serialization-2.27.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532214217
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/oslo.serialization
cp LICENSE %{buildroot}/usr/share/doc/oslo.serialization/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/oslo.serialization/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
