Summary:	TPM2 module for OpenSSL
Summary(pl.UTF-8):	Moduł TPM2 dla OpenSSL-a
Name:		openssl-module-tpm2
Version:	1.2.0
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/tpm2-software/tpm2-openssl/releases
Source0:	https://github.com/tpm2-software/tpm2-openssl/releases/download/%{version}/tpm2-openssl-%{version}.tar.gz
# Source0-md5:	ef3548186c501d14e3b1cd1caf95a0de
URL:		https://github.com/tpm2-software/tpm2-openssl
# for tests
#BuildRequires:	cmocka-devel >= 1.0
#BuildRequires:	expect
BuildRequires:	openssl-devel >= 3.0.0
BuildRequires:	pandoc
BuildRequires:	pkgconfig >= 1:0.25
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.673
BuildRequires:	tpm2-tss-devel >= 3.2.0
Requires:	tpm2-tss >= 3.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		modulesdir	%(pkg-config --variable=modulesdir libcrypto)

%description
Provider for integration of TPM 2.0 to OpenSSL 3.0 makes the TPM 2.0
accessible via the standard OpenSSL API and command-line tools, so one
can add TPM support to (almost) any OpenSSL 3.0 based application.

%description -l pl.UTF-8
Moduł dostawcy, integrujący TPM 2.0 z OpenSSL 3.0, umożliwia dostęp do
TPM 2.0 poprzez standardowe API i narzędzia linii poleceń OpenSSL,
dzięki czemu można dodać obsługę TPM do (prawie) każdej aplikacji
opartej na OpenSSL 3.0.

%prep
%setup -q -n tpm2-openssl-%{version}

%build
%configure \
	--disable-silent-rules \
	--with-modulesdir=%{modulesdir}
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{modulesdir}/tpm2.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{modulesdir}/tpm2.so
