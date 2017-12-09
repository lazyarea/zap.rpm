%define name ZAP
%define version 2.7.0
%define src0  https://github.com/zaproxy/zaproxy/releases/download/%{version}/%{name}_%{version}_Linux.tar.gz

Name:	%{name}
Version: %{version}
Release:	1%{?dist}
Summary: zap installer
BuildRoot: %{_tmppath}/%{name}-%{version}-root
#Group:		
License:	Apache
URL:		http://www.lazyarea.com
#Source:	
#Source0:	https://github.com/zaproxy/zaproxy/releases/download/2.7.0/ZAP_2.7.0_Linux.tar.gz
Source:	%{src0}

Requires:	libXtst xorg-x11-xauth firefox
BuildRequires:	libXtst-devel

#BuildRequires:	firefox libXtst libXtst-devel xorg-x11-xauth 
#Requires:	

%description
zap installer

%prep
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD

curl -LO -b "oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/9.0.1+11/jdk-9.0.1_linux-x64_bin.rpm"
yum localinstall jdk-9.0.1_linux-x64_bin.rpm -y

yum install -y firefox libXtst libXtst-devel xorg-x11-xauth 

curl -LO %{src0}
tar zxvf %{name}_%{version}_Linux.tar.gz

#setup -q
%setup -n %{name}_%{version}
#tar zxvf  %{name}_%{version}_Linux.tar.gz
touch configure
chmod 700 configure

%build
#%configure
#make %{?_smp_mflags}


#%install
#make install DESTDIR=%{buildroot}

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD

%files
#%doc

%changelog

