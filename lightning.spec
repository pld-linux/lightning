Summary:	A library for dynamic code generation
Summary(pl):	Biblioteka do dynamicznego generowania kodu
Name:		lightning
Version:	1.1.1
Release:	1
License:	LGPL/GPL
Group:		Development
Source0:	ftp://ftp.gnu.org/gnu/lightning/%{name}-%{version}.tar.gz
# Source0-md5:	64aecdf3c4e67d15dd476cfac5d33acb
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/lightning/
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU lightning is a library to aid in making portable programs that
compile assembly code at run time.

%description -l pl
GNU lightning to biblioteka maj±ca pomagaæ w tworzeniu przeno¶nych
programów kompiluj±cych kod w asemblerze w czasie wykonywania.

%prep
%setup -q
%patch -p1

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_includedir}/lightning.h
%{_includedir}/lightning
%{_aclocaldir}/lightning.m4
%{_mandir}/man1/*
%{_infodir}/lightning.info*
