%global milestone .0rc0
%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-rsyslog
%global commit ec3faef4d5336fcfe5d7f425c8248d7eb659391c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-rsyslog
Version:        6.0.1
Release:        0.3%{?milestone}%{?alphatag}%{?dist}
Summary:        Puppet module for rsyslog
License:        ASL 2.0

URL:            https://github.com/voxpupuli/%{upstream_name}

Source0:        https://github.com/voxpupuli/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet-concat
Requires:       puppet >= 2.7.0

%description
Puppet module for rsyslog

%prep
%setup -q -n %{name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/rsyslog/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/rsyslog/



%files
%{_datadir}/openstack-puppet/modules/rsyslog/


%changelog
* Mon Mar 13 2023 RDO <dev@lists.rdoproject.org> 6.0.1-0.3.0rc0.ec3faefgit
- Update to post 6.0.1-rc0 (ec3faef4d5336fcfe5d7f425c8248d7eb659391c)


