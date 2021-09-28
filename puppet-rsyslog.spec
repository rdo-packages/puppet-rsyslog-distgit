%global milestone .0rc0
%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-rsyslog
%global commit dfec1469af837e3f2ee1443a2e62e87fa1e4b759
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-rsyslog
Version:        5.2.1
Release:        0.2%{?milestone}%{?alphatag}%{?dist}
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
* Wed Apr 13 2022 RDO <dev@lists.rdoproject.org> 5.2.1-0.2.0rc0.dfec146git
- Update to post 5.2.1-rc0 (dfec1469af837e3f2ee1443a2e62e87fa1e4b759)


