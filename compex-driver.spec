# TODO: standardize UP/SMP modules build and subpackages naming scheme
Summary:	A Linux network adapter skeleton device driver for Compex RL100ATX-PCI
Summary(pl.UTF-8):	Sterownik do kart sieciowych na płytach Compex RL100ATX-PCI
Name:		RL100ATX-PCI
Version:	1.0
Release:	1
License:	GPL
Group:		Base/Kernel
Source0:	ftp://linuxpl.com/pub/%{name}-%{version}.tar.gz
# Source0-md5:	2d86a4112fd4be9ec078ea1bfc4378ee
URL:		http://www.scyld.com/network/drivers.html
BuildRequires:	rpmbuild(macros) >= 1.118
Requires(post,postun):	/sbin/depmod
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This chip is used on low-end OEM boards. The Compex RL100ATX-PCI board
uses a relabeled version of this chip.

%description -l pl.UTF-8
Sterowniki do tanich kart sieciowych, używanych m.in. na płytach
Compex RL100ATX-PCI.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}/net
install *.o $RPM_BUILD_ROOT/lib/modules/%{_kernel_ver}/net

%clean
rm -rf $RPM_BUILD_ROOT

%post
%depmod %{_kernel_ver}

%postun
%depmod %{_kernel_ver}

%files
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/net/*.o*
