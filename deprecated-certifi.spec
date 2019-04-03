#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x70FE17F8A643E15B (lukasa@keybase.io)
#
Name     : deprecated-certifi
Version  : 2018.11.29
Release  : 54
URL      : https://files.pythonhosted.org/packages/55/54/3ce77783acba5979ce16674fc98b1920d00b01d337cfaaf5db22543505ed/certifi-2018.11.29.tar.gz
Source0  : https://files.pythonhosted.org/packages/55/54/3ce77783acba5979ce16674fc98b1920d00b01d337cfaaf5db22543505ed/certifi-2018.11.29.tar.gz
Source99 : https://files.pythonhosted.org/packages/55/54/3ce77783acba5979ce16674fc98b1920d00b01d337cfaaf5db22543505ed/certifi-2018.11.29.tar.gz.asc
Summary  : Python package for providing Mozilla's CA Bundle.
Group    : Development/Tools
License  : MPL-2.0
Requires: deprecated-certifi-license = %{version}-%{release}
Requires: deprecated-certifi-python = %{version}-%{release}
Requires: ca-certs
BuildRequires : buildreq-distutils
BuildRequires : buildreq-distutils3
Patch1: 0001-Use-unified-trust-store.patch

%description
Certifi: Python SSL Certificates
================================
`Certifi`_ is a carefully curated collection of Root Certificates for
validating the trustworthiness of SSL certificates while verifying the identity
of TLS hosts. It has been extracted from the `Requests`_ project.

%package legacypython
Summary: legacypython components for the deprecated-certifi package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the deprecated-certifi package.


%package license
Summary: license components for the deprecated-certifi package.
Group: Default

%description license
license components for the deprecated-certifi package.


%package python
Summary: python components for the deprecated-certifi package.
Group: Default

%description python
python components for the deprecated-certifi package.


%prep
%setup -q -n certifi-2018.11.29
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554314618
export MAKEFLAGS=%{?_smp_mflags}
python2 setup.py build -b py2

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/deprecated-certifi
cp LICENSE %{buildroot}/usr/share/package-licenses/deprecated-certifi/LICENSE
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/deprecated-certifi/LICENSE

%files python
%defattr(-,root,root,-)
