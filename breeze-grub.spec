%define _enable_debug_packages %{nil}
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Summary:	The Breeze theme for the GRUB bootloader
Name:		breeze-grub
Version:	5.21.0
Release:	1
License:	GPL
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/%{name}-%{version}.tar.xz
%ifarch %{ix86} %{x86_64}
Requires:	grub2
%endif
BuildArch:	noarch

%description
This package contains a version of the KDE Breeze theme for
the GRUB bootloader

%files
/boot/grub2/themes/breeze

%prep
%autosetup

%build

%install
mkdir -p %{buildroot}/boot/grub2/themes
cp -a breeze %{buildroot}/boot/grub2/themes/
