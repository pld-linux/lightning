#
# Conditional build:
%bcond_with	disassembler		# jit disassembler using binutils

Summary:	A library for dynamic code generation
Summary(pl.UTF-8):	Biblioteka do dynamicznego generowania kodu
Name:		lightning
Version:	2.2.0
Release:	1
License:	LGPL v3+
Group:		Libraries
Source0:	https://ftp.gnu.org/gnu/lightning/%{name}-%{version}.tar.gz
# Source0-md5:	abf179a9bd6770c9d0e1d501673c6bb7
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/lightning/
%{?with_disassembler:BuildRequires:	binutils-devel}
BuildRequires:	rpmbuild(macros) >= 1.527
BuildRequires:	texinfo
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU lightning is a library to aid in making portable programs that
compile assembly code at run time.

%description -l pl.UTF-8
GNU lightning to biblioteka mająca pomagać w tworzeniu przenośnych
programów kompilujących kod w asemblerze w czasie wykonywania.

%package devel
Summary:	Header files for GNU lightning library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki GNU lightning
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for GNU lightning library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki GNU lightning.

%package static
Summary:	Static GNU lightning library
Summary(pl.UTF-8):	Statyczna biblioteka GNU lightning
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static GNU lightning library.

%description static -l pl.UTF-8
Statyczna biblioteka GNU lightning.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	%{__enable_disable disassembler} \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_libdir}/liblightning.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblightning.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblightning.so
%{_libdir}/liblightning.la
%{_includedir}/lightning
%{_includedir}/lightning.h
%{_infodir}/lightning.info*
%{_pkgconfigdir}/lightning.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/liblightning.a
