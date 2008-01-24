Summary:	A library for dynamic code generation
Summary(pl.UTF-8):	Biblioteka do dynamicznego generowania kodu
Name:		lightning
Version:	1.2
Release:	1
License:	LGPL/GPL
Group:		Development
Source0:	ftp://ftp.gnu.org/gnu/lightning/%{name}-%{version}.tar.gz
# Source0-md5:	dcd2c46ee4dd5d99edd9930022ad2153
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/lightning/
BuildRequires:	automake
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU lightning is a library to aid in making portable programs that
compile assembly code at run time.

%description -l pl.UTF-8
GNU lightning to biblioteka mająca pomagać w tworzeniu przenośnych
programów kompilujących kod w asemblerze w czasie wykonywania.

%prep
%setup -q
%patch0 -p1

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_includedir}/lightning
%{_aclocaldir}/lightning.m4
%{_mandir}/man1/*
%{_infodir}/lightning.info*
