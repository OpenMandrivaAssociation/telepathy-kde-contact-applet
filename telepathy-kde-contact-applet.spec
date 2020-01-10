%define srcname ktp-contact-applet

Summary:        Telepathy KDE Contact Plasmoid
Name:           telepathy-kde-contact-applet
Version:	0.5.1
Release:        2
Url:            https://projects.kde.org/projects/playground/network/telepathy/telepathy-contact-applet
Source0:        ftp://ftp.gtlib.cc.gatech.edu/pub/kde/unstable/telepathy-kde/%version/src/%srcname-%version.tar.bz2
License:        GPLv2+
Group:          Networking/Instant messaging
BuildRequires:  telepathy-kde-common-internals-devel >= %{version}
Requires:       telepathy-kde-common-internals-core

%description
Telepathy KDE Contact Plasmoid.

%files -f plasma_applet_ktp_contact.lang
%{_kde_libdir}/kde4/plasma_applet_ktp_contact.so
%{_kde_libdir}/kde4/imports/org/kde/telepathy/contactlist/
%{_kde_services}/plasma_applet_ktp_contact.desktop
%{_kde_services}/plasma-applet-ktp-contactlist.desktop
%{_kde_appsdir}/plasma/plasmoids/org.kde.ktp-contact/
%{_kde_appsdir}/plasma/plasmoids/org.kde.ktp.contactlist/

#------------------------------------------------------------------------------

%prep
%setup -q -n %srcname-%version
%autopatch -p1

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang plasma_applet_ktp_contact
