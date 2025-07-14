Summary:	Synce plugin for OpenSync
Summary(pl.UTF-8):	Wtyczka Synce do OpenSync
Name:		libopensync-plugin-synce
Version:	0.22
Release:	2
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.opensync.org/attachment/wiki/download/%{name}-%{version}.tar.bz2?format=raw
# Source0-md5:	f325b7dd9f273c46e77fb7b337325880
URL:		http://www.opensync.org/
BuildRequires:	glib2-devel >= 2.0
Patch0:		%{name}-mimedir-vlm.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libmimedir-vlm-devel
BuildRequires:	libopensync-devel >= %{version}
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	synce-libsynce-devel
BuildRequires:	synce-rra-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Synce plugin for OpenSync.

%description -l pl.UTF-8
Wtyczka Synce do OpenSync.

%prep
%setup -q
%patch -P0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/opensync/plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/opensync/plugins/synce_plugin.so
%{_datadir}/opensync/defaults/synce-plugin
