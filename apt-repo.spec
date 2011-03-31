Name:     apt-repo
Version:  1.0
Release:  alt1

Summary:  Script for manipulation APT repository list
License:  GPLv3+
Group:    System/Configuration/Packaging
URL: 	  http://altlinux.org/apt-repo
Packager: Andrey Cherepanov <cas@altlinux.org> 
BuildArch: noarch

Source: %name-%version.tar
BuildRequires: perl-podlators
Requires:  apt

%description
The apt-repo script allow to show, add and remove APT repositories specified
by address in sources.list(5) format, URL with optional component, branch 
name or task number.

%prep
%setup

%install
install -Dm755 %name %buildroot%_bindir/%name
mkdir -p %buildroot%_man1dir
/usr/bin/pod2man %buildroot%_bindir/%name > %buildroot%_man1dir/%name.1

%find_lang %name

%files -f %name.lang
%doc TODO
%_bindir/%name
%doc %_man1dir/%{name}*

%changelog
* Thu Mar 31 2011 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build in Sisyphus

