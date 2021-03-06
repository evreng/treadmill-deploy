Name:           TreadmillAWS
Version:        %{_version} 
Release:        %{_release}%{?dist}
Summary:        Treadmill AWS

License:        Apache 2.0
URL:            https://github.com/Morgan-Stanley/treadmill
Prefix:         /opt/treadmill
AutoReqProv:    no
Requires:       conntrack-tools iproute libcgroup bridge-utils openldap-clients lvm2 lvm2-libs ipset iptables rrdtool bc docker python34 skarnet treadmill-pid1 treadmill-bind treadmill-tktfwd


%description
Treadmill (AWS)


%prep


%build


%install
cp -r %{_builddir}/opt %{buildroot}/opt

%post


%files
%defattr(-,root,root,-)
/opt/treadmill/*

%changelog

