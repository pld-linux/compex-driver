Summary:	A Linux network adapter skeleton device driver for Compex RL100ATX-PCI
Summary(pl):	Sterownik do kart sieciowych na p³ytach Compex RL100ATX-PCI
Name:		RL100ATX-PCI
Version:	1.0
Release:	1
License:	GPL
Group:		Base/Kernel
Source0:	ftp://linuxpl.com/pub/%{name}-%{version}.tar.gz
URL:		http://www.scyld.com/network/drivers.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This chip is used on low-end OEM boards. The Compex RL100ATX-PCI board
uses a relabeled version of this chip.

%description -l pl
Sterowniki do tanich kart sieciowych, u¿ywanych m.in. na p³ytach
Compex RL100ATX-PCI.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}/net 
install *.o $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}/net

%post   
/sbin/depmod -a

%postun 
/sbin/depmod -a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(600,root,root) /lib/modules/%{_kernel_ver}/net/*.o
