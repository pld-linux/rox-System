# TODO:
# - polish summary and description

%define _name System
Summary:	rox-System - system monitor
Name:		rox-%{_name}
Version:	1.9.1
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/rox/system-%{version}.tar.bz2
# Source0-md5:	5b3aa4e1905e08ea14206d894b6b5580
URL:		http://rox.sourceforge.net/desktop/System
Requires:	libgtop
Requires:	python-ctypes
Requires:	rox >= 2.3
Requires:	rox-Lib2 >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_roxdir	%{_libdir}/rox

%description
rox-System displays information about your system - what processes are
running, the amount of memory they are using and used disk space.

%prep
%setup -q -n system-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_roxdir}/%{_name}/{Help,Messages,images}

cd %{_name}
install .DirIcon AppRun *.py *.xml $RPM_BUILD_ROOT%{_roxdir}/%{_name}
install Help/README $RPM_BUILD_ROOT%{_roxdir}/%{_name}/Help
install Messages/*.gmo $RPM_BUILD_ROOT%{_roxdir}/%{_name}/Messages
install images/*.png $RPM_BUILD_ROOT%{_roxdir}/%{_name}/images

%py_comp $RPM_BUILD_ROOT%{_roxdir}/%{_name}
%py_ocomp $RPM_BUILD_ROOT%{_roxdir}/%{_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc System/Help/Changes
%attr(755,root,root) %{_roxdir}/%{_name}/AppRun
%{_roxdir}/%{_name}/.DirIcon
%{_roxdir}/%{_name}/*.py[co]
%{_roxdir}/%{_name}/*.xml
%{_roxdir}/%{_name}/Help
%dir %{_roxdir}/%{_name}/Messages
%lang(fr) %{_roxdir}/%{_name}/Messages/fr.gmo
%lang(it) %{_roxdir}/%{_name}/Messages/it.gmo
%lang(zh_CN) %{_roxdir}/%{_name}/Messages/zh_CN.gmo
%lang(zh_TW) %{_roxdir}/%{_name}/Messages/zh_TW.gmo
%{_roxdir}/%{_name}/images
