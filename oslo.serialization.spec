#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : oslo.serialization
Version  : 1.9.0
Release  : 14
URL      : http://tarballs.openstack.org/oslo.serialization/oslo.serialization-1.9.0.tar.gz
Source0  : http://tarballs.openstack.org/oslo.serialization/oslo.serialization-1.9.0.tar.gz
Summary  : Oslo Serialization library
Group    : Development/Tools
License  : Apache-2.0
Requires: oslo.serialization-python
BuildRequires : Babel-python
BuildRequires : Jinja2
BuildRequires : Pygments
BuildRequires : Sphinx-python
BuildRequires : WebOb-python
BuildRequires : coverage-python
BuildRequires : debtcollector-python
BuildRequires : discover-python
BuildRequires : docutils-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : fixtures-python
BuildRequires : flake8-python
BuildRequires : funcsigs-python
BuildRequires : hacking
BuildRequires : iso8601
BuildRequires : linecache2-python
BuildRequires : markupsafe-python
BuildRequires : mccabe-python
BuildRequires : mock-python
BuildRequires : monotonic-python
BuildRequires : mox3-python
BuildRequires : msgpack-python
BuildRequires : netaddr-python
BuildRequires : oslo.config
BuildRequires : oslo.context-python
BuildRequires : oslo.i18n-python
BuildRequires : oslo.serialization-python
BuildRequires : oslo.utils
BuildRequires : oslosphinx-python
BuildRequires : oslotest-python
BuildRequires : pbr
BuildRequires : pep8
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pyflakes-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-mimeparse-python
BuildRequires : python-subunit
BuildRequires : python3-dev
BuildRequires : pytz-python
BuildRequires : requests-python
BuildRequires : setuptools
BuildRequires : simplejson
BuildRequires : six
BuildRequires : six-python
BuildRequires : stevedore
BuildRequires : testrepository-python
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : tox
BuildRequires : traceback2-python
BuildRequires : unittest2-python
BuildRequires : virtualenv
BuildRequires : wrapt-python

%description
====================
oslo.serialization
====================
.. image:: https://img.shields.io/pypi/v/oslo.serialization.svg
:target: https://pypi.python.org/pypi/oslo.serialization/
:alt: Latest Version

%package python
Summary: python components for the oslo.serialization package.
Group: Default
Requires: Babel-python
Requires: pytz-python
Requires: six-python

%description python
python components for the oslo.serialization package.


%prep
%setup -q -n oslo.serialization-1.9.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python2 setup.py test
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
