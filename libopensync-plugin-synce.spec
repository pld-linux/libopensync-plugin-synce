Summary:	Synce plugin for OpenSync
Name:		libopensync-plugin-synce
Version:	0.22
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://www.opensync.org/attachment/wiki/download/%{name}-%{version}.tar.bz2?format=raw
# Source0-md5:	f325b7dd9f273c46e77fb7b337325880
URL:		http://www.opensync.org/
BuildRequires:	libmimedir-devel
BuildRequires:	libopensync-devel >= %{version}
BuildRequires:	synce-libsynce-devel
BuildRequires:	synce-rra-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Synce plugin for OpenSync.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/opensync/plugins/*.so
%{_libdir}/opensync/plugins/*.la
%{_datadir}/opensync/defaults/*
