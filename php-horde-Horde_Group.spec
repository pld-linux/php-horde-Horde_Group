%define		status		stable
%define		pearname	Horde_Group
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Horde User Groups System
Name:		php-horde-Horde_Group
Version:	1.0.0
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	12c4daadefcb2860183c48fde47a230a
URL:		http://pear.horde.org/package/Horde_Group/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.horde.org)
Requires:	php-horde-Horde_Exception <= 2.0.0
Requires:	php-horde-Horde_Util <= 2.0.0
Requires:	php-pear
Suggests:	php-horde-Horde_Db
Suggests:	php-horde-Horde_Ldap
Conflicts:	php-horde-Horde_Exception = 2.0.0
Conflicts:	php-horde-Horde_Util = 2.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	 pear(Horde/Db.*) pear(Horde/Ldap.*)

%description
Package for managing and accessing the Horde groups system.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc optional-packages.txt
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Horde/Group
%{php_pear_dir}/data/Horde_Group
