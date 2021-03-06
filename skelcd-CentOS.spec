#
#
%define skelcdpath %{_prefix}/lib/skelcd
#
#
%global debug_package %{nil}
Name:           skelcd-CentOS
Version:        8
Release:        0
Summary:        Skeleton for CentOS Media Sets
License:        MIT
Group:          Metapackages
Url:            https://github.com/ganapathichidambaram/skelcd-CentOS
Source:         skelcd-CentOS-%{version}.tar.xz

%description
Internal package only, used for CentOS Media sets


%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{?skelcdpath}/CD1/
cp skelcd/* %{buildroot}%{?skelcdpath}/CD1/
cp skelcd/.treeinfo %{buildroot}%{?skelcdpath}/CD1/.treeinfo
cp skelcd/.discinfo %{buildroot}%{?skelcdpath}/CD1/.discinfo


%files
%if %{defined skelcdpath}
%dir %{skelcdpath}
%endif
%{?skelcdpath}/CD1


%changelog
