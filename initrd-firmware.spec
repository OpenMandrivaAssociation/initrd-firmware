%define name initrd-firmware
%define version 0.2
%define release %mkrel 1
%define drakx-img drakx-installer-images

Summary: Initrd wich contains non-free firmware
Name: %{name}
Version: %{version}
Release: %{release}
Source0: create_initrd_firmware.sh
License: GPL
Group: System/Configuration/Packaging
Url: http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/build_system/bcd
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildrequires: cpio
Buildrequires: atmel-firmware ipw2100-firmware ipw2200-firmware ipw3945-ucode iwlwifi-1000-ucode iwlwifi-3945-ucode iwlwifi-4965-ucode iwlwifi-5000-ucode iwlwifi-5150-ucode iwlwifi-6000-ucode kernel-firmware-extra microcode prism54-firmware radeon-rlc-firmware rt2860-firmware rt2870-firmware rt3090-firmware rt61-firmware rt73-firmware ueagle-firmware zd1201-firmware
Buildrequires: drakx-installer-images
BuildArch: noarch

%description
Initrd wich contains non-free firmware

%prep

%build
cp -vf %{SOURCE0} $RPM_BUILD_DIR/%name-%version
sh $RPM_BUILD_DIR/%name-%version/create_initrd_firmware.sh $RPM_BUILD_DIR/%name-%version

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{drakx-img}/isolinux/alt0
cp -v $RPM_BUILD_DIR/fw.gz %{buildroot}/%{drakx-img}/isolinux/alt0/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{drakx-img}/isolinux/alt0/fw.gz
