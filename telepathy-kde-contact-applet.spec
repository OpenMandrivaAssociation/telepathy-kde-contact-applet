%define rel 1

Summary:        Telepathy KDE Contact Plasmoid
Name:           telepathy-kde-contact-applet
Version:        0.2.0
Release:        %mkrel %{rel}
Url:            https://projects.kde.org/projects/playground/network/telepathy/telepathy-contact-applet
Source0:        ftp://ftp.gtlib.cc.gatech.edu/pub/kde/unstable/telepathy-kde/%version/src/%name-%version.tar.bz2
License:        GPLv2+
Group:          Graphical desktop/KDE
BuildRequires:  kdelibs4-devel
BuildRequires:  telepathy-qt4-devel

%description
Telepathy KDE Contact Plasmoid.

%files
%{_kde_libdir}/kde4/plasma_applet_telepathy_contact.so
%{_kde_services}/telepathy-contact-applet.desktop
%{_kde_appsdir}/plasma/plasmoids/org.kde.telepathy-contact/contents/frames/away.png
%{_kde_appsdir}/plasma/plasmoids/org.kde.telepathy-contact/contents/frames/busy.png
%{_kde_appsdir}/plasma/plasmoids/org.kde.telepathy-contact/contents/frames/offline.png
%{_kde_appsdir}/plasma/plasmoids/org.kde.telepathy-contact/contents/frames/online.png
%{_kde_appsdir}/plasma/plasmoids/org.kde.telepathy-contact/contents/ui/Avatar.qml
%{_kde_appsdir}/plasma/plasmoids/org.kde.telepathy-contact/contents/ui/Contact.qml
%{_kde_appsdir}/plasma/plasmoids/org.kde.telepathy-contact/contents/ui/DropDownMenu.qml
%{_kde_appsdir}/plasma/plasmoids/org.kde.telepathy-contact/contents/ui/main.qml
#--------------------------------------------------------------------

%prep
%setup -q 

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build



